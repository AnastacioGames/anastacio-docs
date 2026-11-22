# KX_AnimationEvent

Classe `Range.types.KX_AnimationEvent`.

```python
# Mostra quantas vezes cada evento da animação disparou.
import Range

own = Range.logic.getCurrentController().owner

for event in own.animationEventManager.events:
    print(event.triggers, event.getFireCount())
```

# Sem documentação da Range

Estes itens existem na engine mas não estavam na documentação da Range. Os marcados **novo na Anastacio** foram adicionados pela Anastacio Engine.

### getFireCount(index=-1)

 `método`

Quantas vezes o gatilho de número `index` disparou. Com -1, soma todos os gatilhos.

**Retorna:** `int`

### triggers

 `atributo · só leitura`

Lista dos frames da animação em que o evento dispara.
