import { defineCollection, z } from 'astro:content';
import { docsLoader } from '@astrojs/starlight/loaders';
import { docsSchema } from '@astrojs/starlight/schema';

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				// Páginas que descrevem o código da engine: arquivos que a página resume e o commit
				// da engine em que foi conferida. tools/checar_engine.py compara os dois.
				fontes: z.array(z.string()).optional(),
				conferido: z.string().optional(),
			}),
		}),
	}),
};
