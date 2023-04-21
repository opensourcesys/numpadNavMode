# Numpad Nav Mode #

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Descargar [versión estable][1]

Numpad Nav Mode es un complemento para [NVDA](https://nvaccess.org) que
permite cambiar fácilmente el bloque numérico de tu teclado entre los
controles de navegación de NVDA y los controles de navegación de Windows sin
lector de pantalla. Esto puede ser especialmente útil para usuarios que
migran de Jaws a NVDA. Este complemento también proporciona control sobre el
estado de la tecla bloqueo numérico, tanto cuando NVDA se inicia como,
opcionalmente, cuando se activan perfiles.

### Explicación y características de los modos de navegación

Las funciones normales del bloque numérico de un pc, con el bloqueo numérico
desactivado, son: retroceso de página, avance página, inicio, fin, las
cuatro flechas, y una tecla suprimir. Sin embargo, NVDA toma el control por
completo sobre el bloque numérico para proporcionar teclas de revisión,
controles del ratón y controles de navegación por objetos. Esto se aplica
incluso en el modo de teclado portátil, que duplica estas funciones en
teclas ajenas al teclado numérico para quienes no tienen uno.

Sin embargo, algunos usuarios disponen de bloque numérico en el teclado de
su portátil, y preferirían usarlo para navegar por Windows (al menos durante
algún tiempo), especialmente porque algunos portátiles no proporcionan
inicio, fin, u otras teclas similares. Aquí es donde este complemento puede
ayudar. Además, algunos usuarios de ordenadores de escritorio, como los que
están acostumbrados al comportamiento del bloque numérico en JAWS, pueden
encontrar conveniente a veces usar el bloque numérico para dichas funciones
de teclado en vez de las teclas normales, cosa que este complemento
permite. Esto incluye la orden popular de JAWS insert del teclado numérico+2
del teclado numérico para leer hasta el final, que fue una petición concreta
de funcionalidad de algunos de los primeros usuarios de este complemento.

### Cómo funciona

Con el bloqueo numérico desactivado, sin importar la disposición de teclado
que uses, este complemento te permitirá pulsar alt+NVDA+más del teclado
numérico (normalmente la segunda tecla larga que está arriba a la derecha),
para pasar fácil y rápidamente entre los controles de navegación de NVDA y
los controles clásicos de navegación de Windows. Se puede reasignar esta
tecla desde el diálogo Gestos de entrada, bajo la categoría Entrada.

Ten en cuenta que este complemento no desactiva el uso de la tecla insert
del teclado numérico como tecla modificadora, si la has configurado así. Si
quieres esa función dímelo, aunque puedes desactivar manualmente insert del
teclado numérico como tecla modificadora desde las opciones de teclado de
NVDA. Tampoco cambia el comportamiento de la tecla suprimir del bloqueo
numérico con NVDA (la tecla entre 0 e intro). Contacta conmigo si quieres
esta función.

Si prefieres que NVDA arranque con el modo de navegación de Windows activado
por defecto, puedes configurarlo desde las opciones. Ve a las preferencias
de NVDA, Opciones, y busca el panel de opciones de Numpad Nav Mode. Allí
podrás seleccionar una casilla de verificación para activar el modo de
navegación de Windows por defecto al arrancar NVDA. Para llegar allí
rápidamente, pulsa NVDA+n, p, o, y luego n una o más veces hasta que oigas
"Numpad Nav Mode".

### Funciones del bloqueo numérico

Por defecto, no se hace nada con la tecla del bloqueo numérico.

Sin embargo, si compartes tu ordenador con un usuario vidente que prefiere
que el bloque numérico siempre esté activo, pero te gusta tenerlo apagado
para que el bloque numérico funcione con NVDA, te puede interesar que el
bloqueo numérico se desactive cuando NVDA arranque. De forma alternativa,
puedes querer introducir muchos datos, y preferir que el bloqueo numérico
esté activo al iniciar NVDA.

 Ve al menú NVDA, Preferencias, Opciones, Numpad Nav Mode, y usa el selector "Estado del bloqueo numérico cuando arranca NVDA o se carga un perfil". Tiene tres opciones. La primera, "No modificar", es la que viene por defecto y no tocará el bloqueo numérico. Lo dejará en el estado que se encontraba cuando se inició NVDA.
La segunda opción, "Desactivar bloqueo numérico", desactivará siempre el bloqueo numérico cuando se inicie NVDA. La tercera opción, "Activar bloqueo numérico", activará el bloqueo numérico si estaba desactivado cuando se inició NVDA.
Si eliges tanto la segunda como la tercera opción, se restaurará el bloqueo numérico a su estado anterior al salir de NVDA. Por ejemplo, si eliges "Desactivar bloqueo numérico", y estaba encendido cuando iniciaste NVDA, se apagará mientras uses NVDA, pero se volverá a activar al salir.

#### Casos de uso avanzados

Si utilizas los potentes perfiles de configuración de NVDA, y te gustaría
activar el bloqueo numérico automáticamente al activar ciertos perfiles, haz
lo siguiente:

* Estando en el "perfil normal", ve al panel de opciones de Numpad Nav Mode
  descrito más arriba. Marca la casilla "El estado inicial del bloqueo
  numérico es dependiente del perfil". Esta opción viene desmarcada por
  defecto.

* Pulsa Aceptar.

* Cambia al perfil donde quieres que siempre se encienda o se apague el
  bloqueo numérico.

* Vuelve al panel de opciones de Numpad Nav Mode, y selecciona la opción que
  prefieras, encender o apagar el bloqueo numérico.

* Después pulsa Aceptar. Ahora, siempre que se active el perfil en cuestión,
  el bloqueo numérico cambiará al estado deseado.

Ten en cuenta que esta es una nueva función, y no sé si alguien la usará. Si
descubres un uso útil, envía un correo o abre [una
incidencia](https://github.com/opensourcesys/numpadNavMode/issues/new) para
explicarme cómo la has usado.

### Nuevas funciones

Te invito a que abras una
[incidencia](https://github.com/openSourceSys/numpadNavMode/issues/new) o me
escribas por correo electrónico para sugerirme nuevas funciones, o cualquier
otro caso de uso que no se haya enumerado aquí, ¡o simplemente para decirme
lo útil que encuentras este complemento!

### Historial

Este complemento es el resultado directo de peticiones que he visto de los
usuarios a lo largo de los años, y un debate en GitHub en la incidencia
[#9549](https://github.com/nvaccess/nvda/issues/9549). Muchas gracias a
@Qchristensen y @feerrenrut. La implementación básica de las funciones del
bloqueo numérico se tomó prestada del complemento antiguo Numblock Manager,
de Noelia Ruiz (@nvdaes en GitHub) y otros. Se usa con permiso.

### Registro de cambios

(Este registro de cambios está incompleto. Usa git log para obtener todos
los detalles.)

* 23.0: compatibilidad con NVDA 2023.x.

* 23.1.0: se añaden funciones de gestión del bloqueo numérico. Mejorado el
  registro. Mejorado el manejo de perfiles de configuración (WIP).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode
