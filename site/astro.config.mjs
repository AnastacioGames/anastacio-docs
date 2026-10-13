// @ts-check
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { modulos, types } from './sidebar-api.mjs';

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
			locales: {
				root: { label: 'Português', lang: 'pt-BR' },
				en: { label: 'English', lang: 'en' },
			},
			customCss: ['./src/styles/anastacio.css'],
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/AnastacioGames' }],
			sidebar: [
				{ label: 'Começar', translations: { en: 'Getting started' }, items: ['guias/primeiro-script', 'guias/range-e-bge'] },
				{
					label: 'Exportar o jogo',
					translations: { en: 'Exporting the game' },
					items: ['exportar/visao-geral', 'exportar/rangearmor', 'exportar/web', 'exportar/android'],
				},
				{
					label: 'Recursos',
					translations: { en: 'Features' },
					items: ['guias/receitas', 'guias/clima', 'guias/camera-fx', 'guias/load-mode', 'guias/veiculos'],
				},
				{ label: 'Módulos', translations: { en: 'Modules' }, items: modulos },
				{ label: 'Range.types', collapsed: true, items: types },
				{ label: 'Projeto', translations: { en: 'Project' }, items: ['sobre', 'situacao-da-doc'] },
			],
		}),
	],
});
