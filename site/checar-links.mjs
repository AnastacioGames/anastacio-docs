// Confere os links internos do site gerado (dist/). Sai com erro se algum aponta para página ou arquivo inexistente.
// Uso: npm run build && npm run checar-links
import { readdirSync, readFileSync, existsSync, statSync } from 'node:fs';
import { join, dirname, posix } from 'node:path';

const DIST = new URL('./dist/', import.meta.url).pathname.replace(/^\/([A-Za-z]:)/, '$1');
const BASE = '/anastacio-docs/';

function htmls(pasta) {
	return readdirSync(pasta, { withFileTypes: true }).flatMap((e) => {
		const p = join(pasta, e.name);
		return e.isDirectory() ? htmls(p) : e.name.endsWith('.html') ? [p] : [];
	});
}

function existe(caminhoUrl) {
	if (!caminhoUrl.startsWith(BASE)) return true; // fora do site
	const rel = decodeURIComponent(caminhoUrl.slice(BASE.length));
	const alvo = join(DIST, rel);
	if (existsSync(alvo) && statSync(alvo).isFile()) return true;
	return existsSync(join(alvo, 'index.html'));
}

const quebrados = [];
for (const arq of htmls(DIST)) {
	const html = readFileSync(arq, 'utf8');
	const urlPagina = BASE + arq.slice(DIST.length).replace(/\\/g, '/').replace(/index\.html$/, '');
	for (const m of html.matchAll(/\s(?:href|src)="([^"#?]*)[^"]*"/g)) {
		const link = m[1];
		if (!link || /^(https?:|mailto:|data:|javascript:|\/\/)/.test(link)) continue;
		const abs = link.startsWith('/') ? link : posix.join(posix.dirname(urlPagina + 'x'), link) + (link.endsWith('/') ? '/' : '');
		if (!existe(abs)) quebrados.push(`${urlPagina} -> ${link}`);
	}
}

const unicos = [...new Set(quebrados)];
if (unicos.length) {
	console.error(`${unicos.length} link(s) quebrado(s):`);
	for (const q of unicos) console.error('  ' + q);
	process.exit(1);
}
console.log('links internos OK');
