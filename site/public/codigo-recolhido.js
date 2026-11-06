// Recolhe os blocos de código longos e põe um botão "Mostrar mais" embaixo.
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

	for (const bloco of document.querySelectorAll('.expressive-code')) {
		const frame = bloco.querySelector('.frame');
		const pre = bloco.querySelector('pre');
		const linhas = bloco.querySelectorAll('.ec-line');
		if (!frame || !pre || linhas.length <= RECOLHER_ACIMA_DE) continue;

		const altura = linhas[LINHAS_VISIVEIS].getBoundingClientRect().top - pre.getBoundingClientRect().top;
		const botao = document.createElement('button');
		botao.type = 'button';
		botao.className = 'ae-mostrar-codigo';

		const recolher = (sim) => {
			frame.classList.toggle('ae-recolhido', sim);
			pre.style.maxHeight = sim ? `${altura}px` : '';
			botao.textContent = sim ? mais : menos;
			botao.setAttribute('aria-expanded', String(!sim));
		};
		botao.addEventListener('click', () => {
			const recolhendo = !frame.classList.contains('ae-recolhido');
			recolher(recolhendo);
			// Ao fechar um bloco comprido, não deixa o leitor perdido mais abaixo na página.
			if (recolhendo && frame.getBoundingClientRect().top < 0) {
				frame.scrollIntoView({ block: 'center' });
			}
		});
		frame.after(botao);
		recolher(true);
	}
})();
