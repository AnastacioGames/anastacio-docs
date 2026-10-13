// Barra lateral da API: módulos com resumo curto e Range.types em categorias.
import { readdirSync } from 'node:fs';

const slug = (s) => s.toLowerCase().replace(/[^a-z0-9_-]/g, '');

const MODULOS = [
	['logic', 'Cena, objetos, tempo e teclado', 'Scene, objects, time and keyboard'],
	['render', 'Janela, tela e gráficos', 'Window, screen and graphics'],
	['events', 'Teclas e botões (constantes)', 'Keys and buttons (constants)'],
	['constraints', 'Juntas e restrições físicas', 'Physics joints and constraints'],
	['texture', 'Texturas de vídeo e imagem', 'Video and image textures'],
	['imgui', 'Interface de depuração', 'Debug interface'],
	['network', 'Multiplayer', 'Multiplayer'],
	['network.steam', 'Multiplayer via Steam (opcional)', 'Multiplayer over Steam (optional)'],
];

// O texto do resumo vem do CSS (anastacio.css), que escolhe data-desc ou data-desc-en pelo idioma.
export const modulos = MODULOS.map(([nome, desc, descEn]) => ({
	label: `Range.${nome}`,
	slug: `api/modulos/${slug(nome)}`,
	attrs: { 'data-desc': desc, 'data-desc-en': descEn },
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

const CATEGORIAS_EN = {"Objetos e cena": "Objects and scene", "Malha e material": "Mesh and material", "Render e efeitos": "Rendering and effects", "Animação e armadura": "Animation and armature", "Física": "Physics", "Entrada": "Input", "Som": "Sound", "Sensores": "Sensors", "Controladores": "Controllers", "Atuadores": "Actuators", "Base e valores": "Base and values", "Outros": "Other"};

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
	.map(([label, items]) => ({ label, translations: { en: CATEGORIAS_EN[label] }, collapsed: true, items }));
