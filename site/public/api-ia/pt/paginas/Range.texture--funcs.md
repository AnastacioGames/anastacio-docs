# Range.texture - métodos e funções

Parte de [Range.texture](Range.texture.md).

## play()

Toca (reinicia) o vídeo.

**Retorna:** Se o vídeo estava pronto ou parado.

**Tipo do retorno:** bool

## pause()

Pausa o vídeo.

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

## stop()

Para o vídeo (play toca de novo desde o início).

**Retorna:** Se o vídeo estava tocando.

**Tipo do retorno:** bool

## refresh(buffer=None, format="RGBA", timestamp=-1.0)

Atualiza o vídeo: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str
- **`timestamp`**: Um timestamp opcional (em segundos desde o início do filme) do frame a copiar para o buffer.
  - tipo: float

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

## refresh(buffer=None, format="RGBA")

Atualiza a imagem: pega o status e, se quiser, copia o frame para um buffer externo.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** veja `FFmpeg Video and Image Status`_.

**Tipo do retorno:** int

## reload(newname=None)

Recarrega a imagem, ou seja, abre de novo.

- **`newname`**: Caminho para uma nova imagem (opcional).
  - tipo: str

## load(imageBuffer, width, height)

Carrega a imagem de um buffer.

- **`imageBuffer`**: Buffer de onde carregar a imagem.
  - tipo: `Buffer` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura da imagem a carregar.
  - tipo: int
- **`height`**: Altura da imagem a carregar.
  - tipo: int

## plot(imageBuffer, width, height, positionX, positionY, mode=IMB_BLEND_COPY)

Atualiza o buffer da imagem.

- **`imageBuffer`**: Buffer de onde carregar os dados novos.
  - tipo: `Buffer`, `ImageBuff` or Python object implementing the buffer protocol (f.ex. bytes)
- **`width`**: Largura dos dados a carregar.
  - tipo: int
- **`height`**: Altura dos dados a carregar.
  - tipo: int
- **`positionX`**: Borda esquerda da região onde desenhar.
  - tipo: int
- **`positionY`**: Borda de cima da região onde desenhar.
  - tipo: int
- **`mode`**: Modo de desenho; veja `Image Blending Modes`_.
  - tipo: int

## refresh(buffer=None, format="RGBA")

Atualiza a imagem: renderiza e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é renderizada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

## getSource(id)

Pega a fonte de imagem.

- **`id`**: Identificador da fonte a pegar.
  - tipo: str

**Retorna:** Fonte de imagem.

**Tipo do retorno:** one of... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## getWeight(id)

Pega o peso da fonte de imagem.

- **`id`**: Identificador da fonte.
  - tipo: str

**Retorna:** Peso da fonte.

**Tipo do retorno:** int

## refresh(buffer=None, format="RGBA")

Atualiza a imagem: calcula e copia a imagem para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é calculada e copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

## setSource(id, image)

Define a fonte de imagem; todas as fontes precisam ter o mesmo tamanho.

- **`id`**: Identificador da fonte a definir.
  - tipo: str
- **`image`**: Fonte de imagem do tipo... * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`

## setWeight(id, weight)

Define o peso da fonte de imagem; a soma dos pesos deve ser 256 para ter intensidade de cor completa na saída.

- **`id`**: Identificador da fonte.
  - tipo: str
- **`weight`**: Peso da fonte.
  - tipo: int

## render()

Renderiza a cena, mas ainda não extrai os pixels. A função volta assim que os comandos de render são enviados à GPU. O render continua assíncrono na GPU enquanto o host faz outras tarefas. Para terminar o render, chame `refresh` diretamente ou atualize a textura da qual este objeto é a fonte. Este método serve para fazer render assíncrono com o melhor desempenho: chame render() no frame n e refresh() no frame n+1, para dar o máximo de tempo à GPU para renderizar enquanto a game engine faz outras tarefas.

**Retorna:** True se o render foi iniciado, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

## refresh()

## refresh(buffer, format="RGBA")

Atualiza: renderiza e, se quiser, copia a imagem para um buffer externo, depois invalida o conteúdo atual. O render pode ter sido iniciado antes com o método `render`; nesse caso esta função só espera as operações de render terminarem. Chamada sem argumento, os pixels não são extraídos, mas o render com certeza está completo quando a função volta. Isso só faz sentido com render fora da tela num alvo de textura (veja `offScreenCreate`).

- **`buffer`**: Um objeto que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type of sufficient size
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

**Retorna:** True se o render terminou, False se não dá para renderizar (por exemplo, a câmera está ativa)

**Tipo do retorno:** bool

## refresh(buffer=None, format="RGBA")

Atualiza: copia a viewport para um buffer externo (opcional) e depois invalida o conteúdo atual.

- **`buffer`**: Um objeto opcional que implementa o buffer protocol. Se for passado, a imagem é copiada para o buffer, que precisa ser grande o bastante, senão uma exceção é levantada. A transferência para o buffer é ideal se a imagem não precisar de processamento, o que acontece com `flip=False, alpha=True, scale=False, whole=True, depth=False, zbuff=False` e nenhum filtro.
  - tipo: any buffer type
- **`format`**: Um especificador opcional do formato da imagem copiada para o buffer. Os únicos valores válidos são "RGBA" ou "BGRA"
  - tipo: str

## play()

Inicia a captura depois de criar o objeto.

**Retorna:** True se a captura começou, False se não.

**Tipo do retorno:** bool

## pause()

Para a captura temporariamente. Use play() para reiniciar.

**Retorna:** True se a captura foi pausada, False se não.

**Tipo do retorno:** bool

## stop()

Para a captura.

**Retorna:** True se a captura foi parada, False se não.

**Tipo do retorno:** bool

## close()

Fecha a textura dinâmica e restaura a original.

## refresh(refresh_source, timestamp=-1.0)

Atualiza a textura a partir da fonte.

- **`refresh_source`**: Se também deve atualizar a fonte de imagem da textura.
  - tipo: bool
- **`timestamp`**: Se a textura controla um objeto VideoFFmpeg: timestamp (em segundos desde o início do filme) do frame a carregar; serve para sincronizar vídeo e som passando `time` a ele (opcional).
  - tipo: float

## close()

Fecha o dispositivo DeckLink e libera todos os recursos. Depois deste método, o objeto não pode ser reativado; é preciso destruí-lo e criar um novo objeto DeckLink para reiniciar a saída.

## refresh(refresh_source,ts)

Este método precisa ser chamado com frequência para atualizar o frame de saída no dispositivo DeckLink.

- **`refresh_source`**: True se o buffer de imagem das fontes deve ser invalidado depois de usado para calcular o frame de saída. Isso faz a imagem de origem ser recalculada no próximo refresh, que normalmente é o desejado. False se o buffer da fonte deve continuar válido e ser reaproveitado no próximo refresh. Repare que o dispositivo DeckLink guarda o frame de saída e repete até o host mandar um novo. Então não é preciso atualizar o objeto DeckLink se você sabe que a fonte de imagem não mudou.
  - tipo: bool
- **`ts`**: O timestamp passado ao objeto de fonte de imagem para calcular a imagem. Se não for passado, é usado o relógio da BGE.
  - tipo: float

## getLastError()

Último erro que aconteceu numa função de Range.texture.

**Retorna:** A descrição do último erro que aconteceu numa função de Range.texture.

**Tipo do retorno:** str

## imageToArray(image, mode)

Devolve um `Buffer` com a imagem atual guardada num objeto de fonte de textura.

- **`image`**: Objeto de fonte de imagem do tipo: * `VideoFFmpeg` * `ImageFFmpeg` * `ImageBuff` * `ImageMirror` * `ImageMix` * `ImageRender` * `ImageViewport`
- **`mode`**: Argumento opcional com o formato de pixel. - Use os caracteres R, G e B para os 3 canais de cor, A para o canal alpha, 0 para forçar um canal fixo em 0 e 1 para forçar um canal fixo em 255. Exemplos: - "BGR" devolve 3 bytes por pixel com os canais azul, verde e vermelho nessa ordem. - "RGB1" devolve 4 bytes por pixel com os canais vermelho, verde e azul nessa ordem e o alpha forçado em 255. - O modo especial "F" devolve a imagem como array de float. Ele só deve ser usado para pegar o buffer de profundidade dos objetos `ImageViewport` e `ImageRender`. O modo padrão é "RGBA".
  - tipo: str

**Retorna:** Um objeto que representa a imagem como array de bytes de uma dimensão, de tamanho (pixel_size*width*height), linha por linha a partir de baixo da imagem. O tamanho e o formato do pixel vêm do parâmetro mode. No modo 'F', o array é de float, de uma dimensão, de tamanho (width*height).

**Tipo do retorno:** `Buffer`

## materialID(object, name)

Devolve um valor numérico que pode ser usado em `Texture` para criar uma textura dinâmica.

O valor corresponde a um número interno de material que usa a textura identificada por name. name é uma string com o nome da textura com prefixo `IM`, se você quiser identificar a textura diretamente. Isto funciona para tex face básica e para material, desde que o material tenha um canal de textura usando essa textura na primeira posição da pilha de texturas. name também pode ter o prefixo `MA`, para identificar a textura pelo material. Nesse caso, o material precisa ter um canal de textura na primeira posição.

Se o objeto não tiver um material que corresponda a name, é gerado um erro em tempo de execução. Use try/except para pegar a exceção.

Ex.: `Range.texture.materialID(obj, 'IMvideo.png')`

- **`object`**: O game object que usa a textura que você quer tornar dinâmica.
  - tipo: `KX_GameObject`
- **`name`**: Nome da textura/material que você quer tornar dinâmico.
  - tipo: str

**Retorna:** O número interno do material.

**Tipo do retorno:** int

## setLogFile(filename)

Define o nome de um arquivo de texto onde as mensagens de erro em tempo de execução serão gravadas, além de aparecerem no console Python. Só os erros específicos do módulo VideoTexture são gravados nesse arquivo; erros comuns não são.

- **`filename`**: Nome do arquivo de log de erros.
  - tipo: str

**Retorna:** -1 se o parâmetro name for inválido (não for string); senão, 0.

**Tipo do retorno:** int
