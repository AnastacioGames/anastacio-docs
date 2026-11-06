// Recolhe os blocos de código longos e põe um único botão "Mostrar mais" na página.
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

	const blocos = [];
	for (const bloco of document.querySelectorAll('.expressive-code')) {
		const frame = bloco.querySelector('.frame');
		const pre = bloco.querySelector('pre');
		const linhas = bloco.querySelectorAll('.ec-line');
		if (!frame || !pre || linhas.length <= RECOLHER_ACIMA_DE) continue;
		const altura = linhas[LINHAS_VISIVEIS].getBoundingClientRect().top - pre.getBoundingClientRect().top;
		blocos.push({ frame, pre, altura });
	}
	if (!blocos.length) return;

	// Um botão só por página, embaixo do primeiro bloco recolhido, que abre e fecha todos os blocos juntos.
	const botao = document.createElement('button');
	botao.type = 'button';
	botao.className = 'ae-mostrar-codigo';

	const recolher = (sim) => {
		for (const { frame, pre, altura } of blocos) {
			frame.classList.toggle('ae-recolhido', sim);
			pre.style.maxHeight = sim ? `${altura}px` : '';
		}
		botao.textContent = sim ? mais : menos;
		botao.setAttribute('aria-expanded', String(!sim));
	};
	botao.addEventListener('click', () => {
		// Mantém na tela o bloco que o leitor está vendo, já que os de cima mudam de altura.
		const referencia = blocos.find(({ frame }) => frame.getBoundingClientRect().bottom > 0)?.frame;
		const topo = referencia?.getBoundingClientRect().top;
		recolher(!blocos[0].frame.classList.contains('ae-recolhido'));
		if (referencia) window.scrollBy({ top: referencia.getBoundingClientRect().top - topo, behavior: 'instant' });
	});
	blocos[0].frame.after(botao);
	recolher(true);
})();
