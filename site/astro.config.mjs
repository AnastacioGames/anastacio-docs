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
				es: { label: 'Español', lang: 'es' },
				ru: { label: 'Русский', lang: 'ru' },
			},
			customCss: ['./src/styles/anastacio.css'],
			components: { Header: './src/components/Header.astro' },
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/AnastacioGames' }],
			sidebar: [
				{ label: 'Começar', translations: { en: 'Getting started', es: 'Empezar', ru: 'Начало работы' }, items: ['guias/primeiro-script', 'guias/range-e-bge'] },
				{
					label: 'Exportar o jogo',
					translations: { en: 'Exporting the game', es: 'Exportar el juego', ru: 'Экспорт игры' },
					items: ['exportar/visao-geral', 'exportar/rangearmor', 'exportar/web', 'exportar/android'],
				},
				{
					label: 'Recursos',
					translations: { en: 'Features', es: 'Recursos', ru: 'Возможности' },
					items: ['guias/receitas', 'guias/clima', 'guias/camera-fx', 'guias/load-mode', 'guias/veiculos', 'guias/multiplayer', 'guias/idiomas', 'guias/smart-components'],
				},
				{ label: 'Módulos', translations: { en: 'Modules', es: 'Módulos', ru: 'Модули' }, items: modulos },
				{ label: 'Range.types', collapsed: true, items: types },
				{ label: 'Projeto', translations: { en: 'Project', es: 'Proyecto', ru: 'Проект' }, items: ['sobre', 'situacao-da-doc'] },
			],
		}),
	],
});
