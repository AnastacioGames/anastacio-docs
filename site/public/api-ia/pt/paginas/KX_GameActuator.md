# KX_GameActuator

Classe base: [`SCA_IActuator`](SCA_IActuator.md)

O atuador de jogo carrega um novo arquivo .blend, reinicia o .blend atual ou fecha o jogo.

```python
# Reinicia o jogo.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_RESTART
cont.activate(act)
```

```python
# Abre outro arquivo de jogo.
import Range

cont = Range.logic.getCurrentController()
act = cont.actuators["Game"]

act.mode = Range.logic.KX_GAME_START
act.fileName = "//level2.range"
cont.activate(act)
```

## fileName

o novo arquivo .blend a carregar.

**Tipo:** string

### mode

O modo deste atuador. Pode ser uma `destas constantes`

**Tipo:** Int

## Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### extensionName

 `atributo`

Extensão do arquivo usado pelos modos de salvar/carregar o jogo.

### saveLocation

 `atributo`

Pasta onde o atuador salva e carrega o jogo.
