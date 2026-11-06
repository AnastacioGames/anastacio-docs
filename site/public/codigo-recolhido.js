// Esconde os exemplos do começo da página atrás de um único botão "Mostrar mais".
// Sem JavaScript o código aparece inteiro. O botão Copiar sempre copia tudo.
(() => {
	const LINHAS_VISIVEIS = 5;
	const RECOLHER_ACIMA_DE = 7; // blocos até esse tamanho ficam inteiros
	const TEXTOS = {
		pt: ['Mostrar mais', 'Mostrar menos'],
		en: ['Show more', 'Show less'],
		es: ['Mostrar más', 'Mostrar menos'],
		ru: ['Показать больше', 'Показать меньше'],
	};
	const [mais, menos] = TEXTOS[document.documentElement.lang.slice(0, 2)] ?? TEXTOS.pt;

	// Só os exemplos do começo da página. Os trechos dentro de cada função ficam à vista,
	// junto do texto que explicam.
	const titulo = document.querySelector('.sl-markdown-content :is(h2, h3)');
	const blocos = [...document.querySelectorAll('.sl-markdown-content .expressive-code')].filter(
		(bloco) => !titulo || bloco.compareDocumentPosition(titulo) & Node.DOCUMENT_POSITION_FOLLOWING,
	);
	if (!blocos.length) return;

	const [primeiro, ...resto] = blocos;
	const frame = primeiro.querySelector('.frame');
	const pre = primeiro.querySelector('pre');
	const linhas = primeiro.querySelectorAll('.ec-line');
	const longo = linhas.length > RECOLHER_ACIMA_DE;
	if (!resto.length && !longo) return;
	const altura = longo ? linhas[LINHAS_VISIVEIS].getBoundingClientRect().top - pre.getBoundingClientRect().top : 0;

	// Um botão só: mostra o começo do primeiro código e abre ou esconde todos juntos.
	const botao = document.createElement('button');
	botao.type = 'button';
	botao.className = 'ae-mostrar-codigo';

	const recolher = (sim) => {
		if (longo) {
			frame.classList.toggle('ae-recolhido', sim);
			pre.style.maxHeight = sim ? `${altura}px` : '';
		}
		for (const bloco of resto) bloco.classList.toggle('ae-oculto', sim);
		botao.textContent = sim ? mais : menos;
		botao.setAttribute('aria-expanded', String(!sim));
		botao.dataset.recolhido = String(sim);
	};
	botao.addEventListener('click', () => {
		const recolhendo = botao.dataset.recolhido !== 'true';
		recolher(recolhendo);
		// Ao fechar tudo, não deixa o leitor perdido mais abaixo na página.
		if (recolhendo && frame.getBoundingClientRect().top < 0) {
			frame.scrollIntoView({ block: 'center' });
		}
	});
	primeiro.after(botao);
	recolher(true);
})();
