# Range.logic - atributos

Parte de [Range.logic](Range.logic.md).

## globalDict

Um dicionário que é mantido quando outro arquivo blend é carregado; serve para guardar inventário e outras variáveis entre cenas e arquivos blend. Ele também pode ser gravado num arquivo e carregado depois com os atuadores de carregar/salvar jogo.

> **Note:**
só tipos nativos do Python, como int/string/bool/float/tuplas/listas, podem ser salvos; GameObjects, atuadores etc. não funcionam como esperado.

## keyboard

O teclado atual, dentro de um objeto `SCA_PythonKeyboard`.

## mouse

O mouse atual, dentro de um objeto `SCA_PythonMouse`.

## motion

Os sensores de movimento do aparelho (giroscópio, acelerômetro, inclinação), dentro de um objeto `KX_PythonMotion`.

## joysticks

Lista dos `SCA_PythonJoystick` conectados. O tamanho da lista é o número máximo de joysticks suportados. Se não houver joystick numa posição, ela vale None.

## inputSystem

Os mapas de entrada do jogo, um `KX_InputSystem`. Eles são carregados dos arquivos JSON da pasta KeyMapping, ao lado do arquivo do jogo.
