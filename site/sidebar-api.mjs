// Barra lateral da API: módulos com resumo curto e Range.types em categorias.
import { readdirSync } from 'node:fs';

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9_-]/g, '');

const MODULOS = [
	['logic', 'Cena, objetos, tempo e teclado'],
	['render', 'Janela, tela e gráficos'],
	['events', 'Teclas e botões (constantes)'],
	['constraints', 'Juntas e restrições físicas'],
	['texture', 'Texturas de vídeo e imagem'],
	['imgui', 'Interface de depuração'],
	['network', 'Multiplayer'],
	['network.steam', 'Multiplayer via Steam (opcional)'],
];

export const modulos = MODULOS.map(([nome, desc]) => ({
	label: `Range.${nome}`,
	slug: `api/modulos/${slug(nome)}`,
	attrs: { 'data-desc': desc, title: desc },
}));

// A primeira regra que casar define a categoria.
const CATEGORIAS = [
	['Objetos e cena', /^(KX_(GameObject|Scene|Camera|LightObject|FontObject|NavMeshObject|WorldInfo|BoundingBox|LibLoadStatus|PythonComponent|BatchGroup|LodLevel|LodManager)|SCA_IObject)$/],
	['Malha e material', /^(KX_(Mesh|MeshBuilder|MeshBuilderSlot|PolyProxy|VertexProxy|BlenderMaterial|ParticleSystem)|BL_(Shader|Texture)|Texture)$/],
	['Render e efeitos', /^(KX_(2DFilter\w*|CubeMap|PlanarMap|TextureRenderer))$/],
	['Animação e armadura', /^(BL_Armature\w*|KX_Animation\w*)$/],
	['Física', /^KX_(CharacterWrapper|VehicleWrapper|ConstraintWrapper|CollisionContactPoint)$/],
	['Entrada', /^(KX_(Python(Keyboard|Mouse|Joystick|Motion)|InputSystem|InputTable)|SCA_InputEvent)$/],
	['Som', /^KX_Speaker$/],
	['Sensores', /Sensor$/],
	['Controladores', /Controller$/],
	['Atuadores', /Actuator$/],
	['Base e valores', /^(EXP_\w+|SCA_ILogicBrick)$/],
];

const nomes = readdirSync(new URL('./src/content/docs/api/types', import.meta.url))
	.filter((f) => f.endsWith('.md'))
	.map((f) => f.slice(0, -3))
	.sort();

const grupos = new Map(CATEGORIAS.map(([c]) => [c, []]));
grupos.set('Outros', []);
for (const n of nomes) {
	const cat = CATEGORIAS.find(([, re]) => re.test(n))?.[0] ?? 'Outros';
	grupos.get(cat).push({ label: n, slug: `api/types/${slug(n)}` });
}

export const types = [...grupos]
	.filter(([, items]) => items.length)
	.map(([label, items]) => ({ label, collapsed: true, items }));
