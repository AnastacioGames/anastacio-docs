# Range.logic - constantes

Parte de [Range.logic](Range.logic.md).

## KX_TRUE

Valor verdadeiro usado por alguns módulos.

## KX_FALSE

Valor falso usado por alguns módulos.

## KX_SENSOR_INACTIVE

Estado do sensor: desligado.

## KX_SENSOR_JUST_ACTIVATED

Estado do sensor: acabou de ligar neste quadro.

## KX_SENSOR_ACTIVE

Estado do sensor: continua ligado.

## KX_SENSOR_JUST_DEACTIVATED

## KX_ARMSENSOR_STATE_CHANGED

Detecta que a constraint mudou de estado (ativa/inativa)

**Valor:** `0`

## KX_ARMSENSOR_LIN_ERROR_BELOW

Detecta que o erro linear da constraint passou de um limite

**Valor:** `1`

## KX_ARMSENSOR_LIN_ERROR_ABOVE

Detecta que o erro linear da constraint ficou abaixo de um limite

**Valor:** `2`

## KX_ARMSENSOR_ROT_ERROR_BELOW

Detecta que o erro de rotação da constraint passou de um limite

**Valor:** `3`

## KX_ARMSENSOR_ROT_ERROR_ABOVE

Detecta que o erro de rotação da constraint ficou abaixo de um limite

**Valor:** `4`

## KX_PROPSENSOR_EQUAL

Ativa quando a propriedade é igual ao valor do sensor.

**Valor:** `1`

## KX_PROPSENSOR_NOTEQUAL

Ativa quando a propriedade é diferente do valor do sensor.

**Valor:** `2`

## KX_PROPSENSOR_INTERVAL

Ativa quando a propriedade está entre os limites indicados.

**Valor:** `3`

## KX_PROPSENSOR_CHANGED

Ativa quando a propriedade muda

**Valor:** `4`

## KX_PROPSENSOR_EXPRESSION

Ativa quando a expressão confere

**Valor:** `5`

## KX_PROPSENSOR_LESSTHAN

Ativa quando a propriedade é menor que o valor do sensor

**Valor:** `6`

## KX_PROPSENSOR_GREATERTHAN

Ativa quando a propriedade é maior que o valor do sensor

**Valor:** `7`

## KX_RADAR_AXIS_POS_X

Sensor Radar: cone apontando para o eixo +X do objeto.

## KX_RADAR_AXIS_POS_Y

Sensor Radar: cone apontando para o eixo +Y do objeto.

## KX_RADAR_AXIS_POS_Z

Sensor Radar: cone apontando para o eixo +Z do objeto.

## KX_RADAR_AXIS_NEG_X

Sensor Radar: cone apontando para o eixo -X do objeto.

## KX_RADAR_AXIS_NEG_Y

Sensor Radar: cone apontando para o eixo -Y do objeto.

## KX_RADAR_AXIS_NEG_Z

## KX_RAY_AXIS_POS_X

Sensor Ray: raio lançado no eixo +X do objeto.

## KX_RAY_AXIS_POS_Y

Sensor Ray: raio lançado no eixo +Y do objeto.

## KX_RAY_AXIS_POS_Z

Sensor Ray: raio lançado no eixo +Z do objeto.

## KX_RAY_AXIS_NEG_X

Sensor Ray: raio lançado no eixo -X do objeto.

## KX_RAY_AXIS_NEG_Y

Sensor Ray: raio lançado no eixo -Y do objeto.

## KX_RAY_AXIS_NEG_Z

## KX_ACTIONACT_PLAY

Atuador Action: toca a animação uma vez.

## KX_ACTIONACT_PINGPONG

Atuador Action: toca para frente e, na próxima ativação, para trás.

## KX_ACTIONACT_FLIPPER

Atuador Action: toca enquanto ativo e volta ao início quando desliga.

## KX_ACTIONACT_LOOPSTOP

Atuador Action: repete enquanto o sensor estiver ativo.

## KX_ACTIONACT_LOOPEND

Atuador Action: repete e, ao desligar, termina a volta atual.

## KX_ACTIONACT_PROPERTY

## KX_ACT_ARMATURE_RUN

Só garante que a armature será atualizada no próximo frame gráfico. É o único modo contínuo do atuador: roda sozinho uma vez por frame até um controlador pará-lo

**Valor:** `0`

## KX_ACT_ARMATURE_ENABLE

Liga a constraint.

**Valor:** `1`

## KX_ACT_ARMATURE_DISABLE

Desliga a constraint (os valores da constraint em tempo de jogo não são atualizados).

**Valor:** `2`

## KX_ACT_ARMATURE_SETTARGET

Troca o alvo e o subalvo da constraint.

**Valor:** `3`

## KX_ACT_ARMATURE_SETWEIGHT

Muda o peso da constraint (só IK).

**Valor:** `4`

## KX_ACT_ARMATURE_SETINFLUENCE

Muda a influência da constraint.

**Valor:** `5`

## KX_CONSTRAINTACT_NORMAL

Ativa o alinhamento à superfície

## KX_CONSTRAINTACT_DISTANCE

Ativa o controle de distância

## KX_CONSTRAINTACT_LOCAL

A direção do raio segue o eixo local

* Vale para a constraint de campo de força:

## KX_CONSTRAINTACT_DOROTFH

O campo de força também age na rotação

* Vale para as duas:

## KX_CONSTRAINTACT_MATERIAL

Detecta material em vez de propriedade

## KX_CONSTRAINTACT_PERMANENT

Não desativa se o raio não atingir o alvo

Veja `Range.types.KX_ConstraintActuator.limit`

## KX_CONSTRAINTACT_LOCX

Limita a coordenada X.

## KX_CONSTRAINTACT_LOCY

Limita a coordenada Y

## KX_CONSTRAINTACT_LOCZ

Limita a coordenada Z

## KX_CONSTRAINTACT_ROTX

Limita a rotação X

## KX_CONSTRAINTACT_ROTY

Limita a rotação Y

## KX_CONSTRAINTACT_ROTZ

Limita a rotação Z

## KX_CONSTRAINTACT_DIRNX

Define a distância ao longo do eixo X negativo

## KX_CONSTRAINTACT_DIRNY

Define a distância ao longo do eixo Y negativo

## KX_CONSTRAINTACT_DIRNZ

Define a distância ao longo do eixo Z negativo

## KX_CONSTRAINTACT_DIRPX

Define a distância ao longo do eixo X positivo

## KX_CONSTRAINTACT_DIRPY

Define a distância ao longo do eixo Y positivo

## KX_CONSTRAINTACT_DIRPZ

Define a distância ao longo do eixo Z positivo

## KX_CONSTRAINTACT_ORIX

Define a orientação do eixo X

## KX_CONSTRAINTACT_ORIY

Define a orientação do eixo Y

## KX_CONSTRAINTACT_ORIZ

Define a orientação do eixo Z

## KX_CONSTRAINTACT_FHNX

Define o campo de força ao longo do eixo X negativo

## KX_CONSTRAINTACT_FHNY

Define o campo de força ao longo do eixo Y negativo

## KX_CONSTRAINTACT_FHNZ

Define o campo de força ao longo do eixo Z negativo

## KX_CONSTRAINTACT_FHPX

Define o campo de força ao longo do eixo X positivo

## KX_CONSTRAINTACT_FHPY

Define o campo de força ao longo do eixo Y positivo

## KX_CONSTRAINTACT_FHPZ

Define o campo de força ao longo do eixo Z positivo

## KX_DYN_RESTORE_DYNAMICS

Atuador Dynamic: volta a ter física.

## KX_DYN_DISABLE_DYNAMICS

Atuador Dynamic: desliga a física do objeto.

## KX_DYN_ENABLE_RIGID_BODY

Atuador Dynamic: liga o modo corpo rígido (rotação pela física).

## KX_DYN_DISABLE_RIGID_BODY

Atuador Dynamic: desliga o modo corpo rígido.

## KX_DYN_SET_MASS

## KX_GAME_LOAD

Atuador Game: carrega outro arquivo de jogo.

## KX_GAME_START

Atuador Game: inicia outro arquivo de jogo.

## KX_GAME_RESTART

Atuador Game: reinicia o jogo.

## KX_GAME_QUIT

Atuador Game: fecha o jogo.

## KX_GAME_SAVECFG

Atuador Game: salva as propriedades globais em arquivo.

## KX_GAME_LOADCFG

## KX_ACT_MOUSE_OBJECT_AXIS_X

Atuador Mouse (look): gira em torno do eixo X do objeto.

## KX_ACT_MOUSE_OBJECT_AXIS_Y

Atuador Mouse (look): gira em torno do eixo Y do objeto.

## KX_ACT_MOUSE_OBJECT_AXIS_Z

## KX_PARENT_REMOVE

Atuador Parent: tira o objeto do pai.

## KX_PARENT_SET

## KX_RANDOMACT_BOOL_CONST

Atuador Random: verdadeiro/falso fixo.

## KX_RANDOMACT_BOOL_UNIFORM

Atuador Random: verdadeiro ou falso com 50% de chance cada.

## KX_RANDOMACT_BOOL_BERNOUILLI

Atuador Random: verdadeiro com a chance que você definir.

## KX_RANDOMACT_INT_CONST

Atuador Random: número inteiro fixo.

## KX_RANDOMACT_INT_UNIFORM

Atuador Random: inteiro sorteado entre um mínimo e um máximo.

## KX_RANDOMACT_INT_POISSON

Atuador Random: inteiro com distribuição de Poisson (média definida).

## KX_RANDOMACT_FLOAT_CONST

Atuador Random: número decimal fixo.

## KX_RANDOMACT_FLOAT_UNIFORM

Atuador Random: decimal sorteado entre um mínimo e um máximo.

## KX_RANDOMACT_FLOAT_NORMAL

Atuador Random: decimal com distribuição normal (média e desvio).

## KX_RANDOMACT_FLOAT_NEGATIVE_EXPONENTIAL

## KX_SCENE_RESTART

Atuador Scene: reinicia a cena.

## KX_SCENE_SET_SCENE

Atuador Scene: troca para outra cena.

## KX_SCENE_SET_CAMERA

Atuador Scene: troca a câmera ativa.

## KX_SCENE_ADD_FRONT_SCENE

Atuador Scene: adiciona uma cena por cima (overlay, como HUD).

## KX_SCENE_ADD_BACK_SCENE

Atuador Scene: adiciona uma cena por baixo (fundo).

## KX_SCENE_REMOVE_SCENE

Atuador Scene: remove uma cena.

## KX_SCENE_SUSPEND

Atuador Scene: pausa uma cena.

## KX_SCENE_RESUME

## KX_SOUNDACT_PLAYSTOP

Atuador Sound: toca enquanto o sensor estiver ativo e para quando desligar.

**Valor:** `1`

## KX_SOUNDACT_PLAYEND

Atuador Sound: toca o som inteiro uma vez.

**Valor:** `2`

## KX_SOUNDACT_LOOPSTOP

Atuador Sound: repete enquanto o sensor estiver ativo.

**Valor:** `3`

## KX_SOUNDACT_LOOPEND

Atuador Sound: repete e, ao desligar, termina a volta atual.

**Valor:** `4`

## KX_SOUNDACT_LOOPBIDIRECTIONAL

Atuador Sound: toca para frente e para trás em repetição.

**Valor:** `5`

## KX_SOUNDACT_LOOPBIDIRECTIONAL_STOP

**Valor:** `6`

## KX_STEERING_SEEK

Atuador Steering: vai até o alvo.

**Valor:** `1`

## KX_STEERING_FLEE

Atuador Steering: foge do alvo.

**Valor:** `2`

## KX_STEERING_PATHFOLLOWING

**Valor:** `3`

## KX_TRACK_UPAXIS_POS_X

Atuador Track To: eixo +X do objeto fica para cima.

## KX_TRACK_UPAXIS_POS_Y

Atuador Track To: eixo +Y do objeto fica para cima.

## KX_TRACK_UPAXIS_POS_Z

Atuador Track To: eixo +Z do objeto fica para cima.

## KX_TRACK_TRAXIS_POS_X

Atuador Track To: eixo +X do objeto aponta para o alvo.

## KX_TRACK_TRAXIS_POS_Y

Atuador Track To: eixo +Y do objeto aponta para o alvo.

## KX_TRACK_TRAXIS_POS_Z

Atuador Track To: eixo +Z do objeto aponta para o alvo.

## KX_TRACK_TRAXIS_NEG_X

Atuador Track To: eixo -X do objeto aponta para o alvo.

## KX_TRACK_TRAXIS_NEG_Y

Atuador Track To: eixo -Y do objeto aponta para o alvo.

## KX_TRACK_TRAXIS_NEG_Z

## RAS_2DFILTER_BLUR

Atuador 2D Filter: desfoque.

**Valor:** `2`

## RAS_2DFILTER_CUSTOMFILTER

Filtro personalizado; o código é definido pela propriedade shaderText.

**Valor:** `12`

## RAS_2DFILTER_DILATION

Atuador 2D Filter: dilatação (clareia bordas).

**Valor:** `4`

## RAS_2DFILTER_DISABLED

Desliga o filtro que está ativo agora

**Valor:** `-1`

## RAS_2DFILTER_ENABLED

Liga o filtro que foi desligado antes

**Valor:** `-2`

## RAS_2DFILTER_EROSION

Atuador 2D Filter: erosão (escurece bordas).

**Valor:** `5`

## RAS_2DFILTER_GRAYSCALE

Atuador 2D Filter: tons de cinza.

**Valor:** `9`

## RAS_2DFILTER_INVERT

Atuador 2D Filter: cores invertidas.

**Valor:** `11`

## RAS_2DFILTER_LAPLACIAN

Atuador 2D Filter: detecção de bordas (Laplace).

**Valor:** `6`

## RAS_2DFILTER_MOTIONBLUR

Cria e liga filtros prontos

**Valor:** `1`

## RAS_2DFILTER_NOFILTER

Desliga e destrói o filtro que está ativo agora

**Valor:** `0`

## RAS_2DFILTER_PREWITT

Atuador 2D Filter: detecção de bordas (Prewitt).

**Valor:** `8`

## RAS_2DFILTER_SEPIA

Atuador 2D Filter: sépia.

**Valor:** `10`

## RAS_2DFILTER_SHARPEN

Atuador 2D Filter: nitidez.

**Valor:** `3`

## RAS_2DFILTER_SOBEL

**Valor:** `7`

## RAS_2DFILTER_SOBEL

**Valor:** `14`

## ROT_MODE_QUAT

Usa o quaternion do atributo rotation para atualizar a rotação do osso.

**Valor:** `0`

## ROT_MODE_XYZ

Usa euler_rotation e aplica os ângulos nos eixos Z, Y, X do osso, nessa ordem.

**Valor:** `1`

## ROT_MODE_XZY

Usa euler_rotation e aplica os ângulos nos eixos Y, Z, X do osso, nessa ordem.

**Valor:** `2`

## ROT_MODE_YXZ

Usa euler_rotation e aplica os ângulos nos eixos Z, X, Y do osso, nessa ordem.

**Valor:** `3`

## ROT_MODE_YZX

Usa euler_rotation e aplica os ângulos nos eixos X, Z, Y do osso, nessa ordem.

**Valor:** `4`

## ROT_MODE_ZXY

Usa euler_rotation e aplica os ângulos nos eixos Y, X, Z do osso, nessa ordem.

**Valor:** `5`

## ROT_MODE_ZYX

Usa euler_rotation e aplica os ângulos nos eixos X, Y, Z do osso, nessa ordem.

**Valor:** `6`

## CONSTRAINT_TYPE_TRACKTO

Tipo de restrição de bone: Track To (aponta para um alvo).

## CONSTRAINT_TYPE_KINEMATIC

Tipo de restrição de bone: IK (cinemática inversa).

## CONSTRAINT_TYPE_ROTLIKE

Tipo de restrição de bone: Copy Rotation.

## CONSTRAINT_TYPE_LOCLIKE

Tipo de restrição de bone: Copy Location.

## CONSTRAINT_TYPE_MINMAX

Tipo de restrição de bone: Floor (limite mín./máx.).

## CONSTRAINT_TYPE_SIZELIKE

Tipo de restrição de bone: Copy Scale.

## CONSTRAINT_TYPE_LOCKTRACK

Tipo de restrição de bone: Locked Track.

## CONSTRAINT_TYPE_STRETCHTO

Tipo de restrição de bone: Stretch To.

## CONSTRAINT_TYPE_CLAMPTO

Tipo de restrição de bone: Clamp To (prende a uma curva).

## CONSTRAINT_TYPE_TRANSFORM

Tipo de restrição de bone: Transformation.

## CONSTRAINT_TYPE_DISTLIMIT

Veja `Range.types.BL_ArmatureConstraint.ik_type`

## CONSTRAINT_IK_COPYPOSE

A constraint tenta igualar a posição e, se for o caso, a rotação do alvo.

**Valor:** `0`

## CONSTRAINT_IK_DISTANCE

A constraint mantém uma certa distância do alvo, conforme ik_mode

**Valor:** `1`

Veja `Range.types.BL_ArmatureConstraint.ik_flag`

## CONSTRAINT_IK_FLAG_TIP

Ligado quando a constraint age na cabeça do osso e não na ponta

**Valor:** `1`

## CONSTRAINT_IK_FLAG_ROT

Ligado quando a constraint tenta igualar a orientação do alvo

**Valor:** `2`

## CONSTRAINT_IK_FLAG_STRETCH

Ligado quando a armature pode esticar (só os ossos com fator de estiramento > 0.0)

**Valor:** `16`

## CONSTRAINT_IK_FLAG_POS

Ligado quando a constraint tenta igualar a posição do alvo.

**Valor:** `32`

Veja `Range.types.BL_ArmatureConstraint.ik_mode`

## CONSTRAINT_IK_MODE_INSIDE

A constraint tenta manter o osso a no máximo ik_dist do alvo

**Valor:** `0`

## CONSTRAINT_IK_MODE_OUTSIDE

A constraint tenta manter o osso a mais de ik_dist do alvo

**Valor:** `1`

## CONSTRAINT_IK_MODE_ONSURFACE

A constraint tenta manter o osso exatamente a ik_dist do alvo.

**Valor:** `2`

## BL_DST_ALPHA

Fator de mistura (blend) do material: alfa de destino. Usado em setBlending().

## BL_DST_COLOR

Fator de mistura (blend) do material: cor de destino. Usado em setBlending().

## BL_ONE

Fator de mistura (blend) do material: um (cor inteira). Usado em setBlending().

## BL_ONE_MINUS_DST_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de destino. Usado em setBlending().

## BL_ONE_MINUS_DST_COLOR

Fator de mistura (blend) do material: 1 menos a cor de destino. Usado em setBlending().

## BL_ONE_MINUS_SRC_ALPHA

Fator de mistura (blend) do material: 1 menos o alfa de origem. Usado em setBlending().

## BL_ONE_MINUS_SRC_COLOR

Fator de mistura (blend) do material: 1 menos a cor de origem. Usado em setBlending().

## BL_SRC_ALPHA

Fator de mistura (blend) do material: alfa de origem. Usado em setBlending().

## BL_SRC_ALPHA_SATURATE

Fator de mistura (blend) do material: alfa de origem saturado. Usado em setBlending().

## BL_SRC_COLOR

Fator de mistura (blend) do material: cor de origem. Usado em setBlending().

## BL_ZERO

## KX_INPUT_NONE

Estado de tecla/botão: solto.

## KX_INPUT_JUST_ACTIVATED

Estado de tecla/botão: acabou de ser apertado.

## KX_INPUT_ACTIVE

Estado de tecla/botão: continua apertado.

## KX_INPUT_JUST_RELEASED

## KX_ACTION_MODE_PLAY

Toca a ação uma vez.

**Valor:** `0`

## KX_ACTION_MODE_LOOP

Repete a ação em loop.

**Valor:** `1`

## KX_ACTION_MODE_PING_PONG

Toca a ação para a frente e, quando termina, volta para trás.

**Valor:** `2`

## KX_ACTION_BLEND_BLEND

Mistura as camadas por interpolação linear

**Valor:** `0`

## KX_ACTION_BLEND_ADD

Soma as camadas

**Valor:** `1`

## KX_MOUSE_BUT_LEFT

Botão esquerdo do mouse (para o sensor de mouse).

## KX_MOUSE_BUT_MIDDLE

Botão do meio do mouse (para o sensor de mouse).

## KX_MOUSE_BUT_RIGHT

## RM_WALLS

Desenha só as paredes.

## RM_POLYS

Desenha só os polígonos.

## RM_TRIS

Desenha a malha de triângulos.

## VIEWMATRIX

Uniforme de shader com a matriz visão (mundo → câmera). Usado em setUniformDef().

## VIEWMATRIX_INVERSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa. Usado em setUniformDef().

## VIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), inversa transposta. Usado em setUniformDef().

## VIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz visão (mundo → câmera), transposta. Usado em setUniformDef().

## MODELMATRIX

Uniforme de shader com a matriz modelo (objeto → mundo). Usado em setUniformDef().

## MODELMATRIX_INVERSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa. Usado em setUniformDef().

## MODELMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), inversa transposta. Usado em setUniformDef().

## MODELMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo (objeto → mundo), transposta. Usado em setUniformDef().

## MODELVIEWMATRIX

Uniforme de shader com a matriz modelo × visão. Usado em setUniformDef().

## MODELVIEWMATRIX_INVERSE

Uniforme de shader com a matriz modelo × visão, inversa. Usado em setUniformDef().

## MODELVIEWMATRIX_INVERSETRANSPOSE

Uniforme de shader com a matriz modelo × visão, inversa transposta. Usado em setUniformDef().

## MODELVIEWMATRIX_TRANSPOSE

Uniforme de shader com a matriz modelo × visão, transposta. Usado em setUniformDef().

## CAM_POS

Posição da câmera atual

## CONSTANT_TIMER

Uniforme de shader com o tempo do jogo, para animar efeitos.

## EYE

Usa um timer como valor do uniform.

## SHD_TANGENT

## KX_STATE1

Máscara do estado 1 dos logic bricks.

## KX_STATE2

Máscara do estado 2 dos logic bricks.

## KX_STATE3

Máscara do estado 3 dos logic bricks.

## KX_STATE4

Máscara do estado 4 dos logic bricks.

## KX_STATE5

Máscara do estado 5 dos logic bricks.

## KX_STATE6

Máscara do estado 6 dos logic bricks.

## KX_STATE7

Máscara do estado 7 dos logic bricks.

## KX_STATE8

Máscara do estado 8 dos logic bricks.

## KX_STATE9

Máscara do estado 9 dos logic bricks.

## KX_STATE10

Máscara do estado 10 dos logic bricks.

## KX_STATE11

Máscara do estado 11 dos logic bricks.

## KX_STATE12

Máscara do estado 12 dos logic bricks.

## KX_STATE13

Máscara do estado 13 dos logic bricks.

## KX_STATE14

Máscara do estado 14 dos logic bricks.

## KX_STATE15

Máscara do estado 15 dos logic bricks.

## KX_STATE16

Máscara do estado 16 dos logic bricks.

## KX_STATE17

Máscara do estado 17 dos logic bricks.

## KX_STATE18

Máscara do estado 18 dos logic bricks.

## KX_STATE19

Máscara do estado 19 dos logic bricks.

## KX_STATE20

Máscara do estado 20 dos logic bricks.

## KX_STATE21

Máscara do estado 21 dos logic bricks.

## KX_STATE22

Máscara do estado 22 dos logic bricks.

## KX_STATE23

Máscara do estado 23 dos logic bricks.

## KX_STATE24

Máscara do estado 24 dos logic bricks.

## KX_STATE25

Máscara do estado 25 dos logic bricks.

## KX_STATE26

Máscara do estado 26 dos logic bricks.

## KX_STATE27

Máscara do estado 27 dos logic bricks.

## KX_STATE28

Máscara do estado 28 dos logic bricks.

## KX_STATE29

Máscara do estado 29 dos logic bricks.

## KX_STATE30

Veja `Range.types.KX_StateActuator.operation`

## KX_STATE_OP_CLR

Subtrai bits da máscara de estados

**Valor:** `0`

## KX_STATE_OP_CPY

Copia a máscara de estados

**Valor:** `1`

## KX_STATE_OP_NEG

Inverte bits da máscara de estados

**Valor:** `2`

## KX_STATE_OP_SET

Soma bits à máscara de estados

**Valor:** `3`

## KX_GAME_SCREENSHOT

 `constante`

Modo do atuador Game: tira um print da tela.

## KX_JOYSTICK_BUT_A

 `constante`

Botão A do controle.

## KX_JOYSTICK_BUT_B

 `constante`

Botão B do controle.

## KX_JOYSTICK_BUT_BACK

 `constante`

Botão Back/Select do controle.

## KX_JOYSTICK_BUT_GUIDE

 `constante`

Botão Guide (botão central) do controle.

## KX_JOYSTICK_BUT_LEFTSHOUDER

 `constante`

Botão ombro esquerdo (LB) do controle.

## KX_JOYSTICK_BUT_LEFTSTICK

 `constante`

Botão clique do analógico esquerdo do controle.

## KX_JOYSTICK_BUT_PADDOWN

 `constante`

Botão direcional para baixo do controle.

## KX_JOYSTICK_BUT_PADLEFT

 `constante`

Botão direcional para a esquerda do controle.

## KX_JOYSTICK_BUT_PADRIGHT

 `constante`

Botão direcional para a direita do controle.

## KX_JOYSTICK_BUT_PADUP

 `constante`

Botão direcional para cima do controle.

## KX_JOYSTICK_BUT_RIGHTSHOUDER

 `constante`

Botão ombro direito (RB) do controle.

## KX_JOYSTICK_BUT_RIGHTSTICK

 `constante`

Botão clique do analógico direito do controle.

## KX_JOYSTICK_BUT_X

 `constante`

Botão X do controle.

## KX_JOYSTICK_BUT_Y

 `constante`

Botão Y do controle.

## KX_MOUSE_BUT_BUTTON6

 `constante`

Botão 6 do mouse.

## KX_MOUSE_BUT_BUTTON7

 `constante`

Botão 7 do mouse.

## KX_MOUSE_BUT_LEFTTHUMBMOUSE

 `constante`

Botão lateral esquerdo do mouse (polegar).

## KX_MOUSE_BUT_RIGHTTHUMBMOUSE

 `constante`

Botão lateral direito do mouse (polegar).

## KX_MOUSESENSORMODE_BUTTON6

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_BUTTON7

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_LEFTBUTTON

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_LEFTTHUMBMOUSE

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_MIDDLEBUTTON

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_MOVEMENT

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_RIGHTBUTTON

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_RIGHTTHUMBMOUSE

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_WHEELDOWN

*(sem documentação)* `constante`

## KX_MOUSESENSORMODE_WHEELUP

*(sem documentação)* `constante`

## KX_MOVEMENT_ALL_AXIS

 `constante`

Sensor Movement: vigia todos os eixos.

## KX_MOVEMENT_AXIS_NEG_X

 `constante`

Sensor Movement: eixo -X.

## KX_MOVEMENT_AXIS_NEG_Y

 `constante`

Sensor Movement: eixo -Y.

## KX_MOVEMENT_AXIS_NEG_Z

 `constante`

Sensor Movement: eixo -Z.

## KX_MOVEMENT_AXIS_POS_X

 `constante`

Sensor Movement: eixo +X.

## KX_MOVEMENT_AXIS_POS_Y

 `constante`

Sensor Movement: eixo +Y.

## KX_MOVEMENT_AXIS_POS_Z

 `constante`

Sensor Movement: eixo +Z.

## RAS_2DFILTER_BLOOM

 `constante`

Filtro 2D: Bloom.

## RAS_2DFILTER_FXAA

 `constante`

Filtro 2D: FXAA.

## RAS_2DFILTER_LIGHTSCATTER

 `constante`

Filtro 2D: raios de luz (light scattering).

## RAS_2DFILTER_OUTLINE

 `constante`

Filtro 2D: contorno (outline).

## RAS_2DFILTER_SSAO

 `constante`

Filtro 2D: oclusão de ambiente (SSAO).

## RAS_2DFILTER_SSR

 `constante`

Filtro 2D: reflexos em tela (SSR).

## RAS_2DFILTER_TONEMAP

 `constante`

Filtro 2D: tonemap.
