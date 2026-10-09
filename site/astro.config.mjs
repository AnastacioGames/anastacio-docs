// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

// GitHub Pages: https://<usuario>.github.io/<repositorio>/
// Troque SITE/BASE se o repositório ou o usuário tiverem outro nome.
const SITE = 'https://anastaciogames.github.io';
const BASE = '/anastacio-docs';

export default defineConfig({
	site: SITE,
	base: BASE,
	integrations: [
		starlight({
			title: 'Anastacio Engine',
			description: 'Documentação da API Python da Anastacio Engine',
			logo: { src: './src/assets/cubo.webp', alt: '' },
			favicon: '/favicon.png',
			defaultLocale: 'root',
			locales: { root: { label: 'Português', lang: 'pt-BR' } },
			customCss: ['./src/styles/anastacio.css'],
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/AnastacioGames' }],
			sidebar: [
				{ label: 'Começar', items: ['guias/primeiro-script', 'guias/range-e-bge'] },
				{ label: 'Módulos', items: [{ autogenerate: { directory: 'api/modulos' } }] },
				{ label: 'Range.types', collapsed: true, items: [{ autogenerate: { directory: 'api/types' } }] },
				{ label: 'Projeto', items: ['sobre', 'situacao-da-doc'] },
			],
		}),
	],
});
