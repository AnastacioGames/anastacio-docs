# Range.texture - constantes

Parte de [Range.texture](Range.texture.md).

## SOURCE_ERROR

Status da fonte de vídeo ou imagem: erro ao abrir ou ler o arquivo ou dispositivo (valor -1). É um dos valores possíveis de `status`.

## SOURCE_EMPTY

Status da fonte: ainda sem conteúdo carregado (valor 0). É um dos valores possíveis de `status`.

## SOURCE_READY

Status da fonte: carregada e pronta para tocar (valor 1). É um dos valores possíveis de `status`.

## SOURCE_PLAYING

Status da fonte: em reprodução (valor 2). É um dos valores possíveis de `status`.

## SOURCE_STOPPED

Status da fonte: parada ou pausada depois de tocar (valor 3). É um dos valores possíveis de `status`.

## IMB_BLEND_MIX

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Mistura normal: a origem é colocada por cima do destino conforme o alpha dela. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_ADD

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Soma as cores da origem às do destino (máximo 255). O alpha do destino não muda. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_SUB

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Subtrai as cores da origem das do destino (mínimo 0). O alpha do destino não muda. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_MUL

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Multiplica as cores do destino pelas da origem, o que escurece. O alpha do destino não muda. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_LIGHTEN

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Fica com o mais claro entre origem e destino em cada canal de cor. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_DARKEN

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Fica com o mais escuro entre origem e destino em cada canal de cor. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_ERASE_ALPHA

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Não mexe nas cores: diminui o alpha do destino conforme o alpha da origem, o que apaga a região. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_ADD_ALPHA

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Não mexe nas cores: aumenta o alpha do destino conforme o alpha da origem (máximo 255). O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_OVERLAY

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Overlay, como nos editores de imagem: multiplica nas sombras do destino e usa screen nas luzes. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_HARDLIGHT

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Hard Light, como nos editores de imagem. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_COLORBURN

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Color Burn, como nos editores de imagem: escurece o destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_LINEARBURN

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Linear Burn: soma origem e destino e subtrai 255 (mínimo 0), o que escurece. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_COLORDODGE

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Color Dodge, como nos editores de imagem: clareia o destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_SCREEN

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Screen: inverte, multiplica e inverte de novo, o que clareia. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_SOFTLIGHT

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Soft Light, como nos editores de imagem: versão suave do overlay. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_PINLIGHT

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Pin Light, como nos editores de imagem. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_VIVIDLIGHT

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Vivid Light, como nos editores de imagem. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_LINEARLIGHT

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Linear Light, como nos editores de imagem. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_DIFFERENCE

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Diferença: valor absoluto da diferença entre origem e destino em cada canal. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_EXCLUSION

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Exclusão: parecida com a diferença, com menos contraste. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_HUE

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Pega o matiz da origem e mantém a saturação e o valor do destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_SATURATION

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Pega a saturação da origem e mantém o matiz e o valor do destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_LUMINOSITY

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Pega o valor (brilho) da origem e mantém o matiz e a saturação do destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_COLOR

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`. Pega o matiz e a saturação da origem e mantém o valor (brilho) do destino. O efeito é ponderado pelo alpha da imagem de origem; onde ele é 0, nada muda.

## IMB_BLEND_COPY

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot` (valor padrão): copia a origem por cima do destino, com RGB e alpha, sem mesclar.

## IMB_BLEND_COPY_RGB

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`: copia só as cores (RGB) da origem e mantém o alpha do destino.

## IMB_BLEND_COPY_ALPHA

Modo de mesclagem para o argumento `mode` de `ImageBuff.plot`: copia só o alpha da origem e mantém as cores do destino.
