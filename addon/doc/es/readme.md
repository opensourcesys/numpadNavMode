# Numpad Nav Mode #

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Descargar [versión estable][1]

Numpad Nav Mode es un complemento para [NVDA](https://nvaccess.org) que
permite cambiar fácilmente el bloque numérico de tu teclado entre los
controles de navegación de NVDA y los controles de navegación de Windows sin
lector de pantalla.

Las funciones normales del bloque numérico de un pc, con el bloqueo numérico
desactivado, son: retroceso de página, avance página, inicio, fin, las
cuatro flechas, y una tecla suprimir. Sin embargo, NVDA toma el control
sobre el bloque numérico para proporcionar teclas de revisión, controles del
ratón y controles de navegación por objetos. Esto se aplica incluso en el
modo de teclado portátil, que duplica estas funciones en teclas ajenas al
teclado numérico para quienes no tienen uno.

Sin embargo, algunos usuarios disponen de bloque numérico en el teclado de
su portátil, y preferirían usarlo para navegar por Windows, especialmente
porque algunos portátiles no proporcionan inicio, fin, u otras teclas
similares. Aquí es donde este complemento puede ayudar. Además, algunos
usuarios de ordenadores de escritorio pueden encontrar conveniente a veces
usar el bloque numérico para dichas funciones de teclado en vez de las
teclas normales, cosa que este complemento permite.

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
NVDA.

Si prefieres que NVDA arranque con el modo de navegación de Windows activado
por defecto, puedes configurarlo desde las opciones. Ve a las preferencias
de NVDA, Opciones, y busca el panel de opciones de Numpad Nav Mode. Allí
podrás seleccionar una casilla de verificación para activar el modo de
navegación de Windows por defecto al arrancar NVDA. Para llegar allí
rápidamente, pulsa NVDA+n, p, o, y luego n una o más veces hasta que oigas
"Numpad Nav Mode".

### Nuevas funciones

Te invito a que me escribas por correo electrónico para sugerirme nuevas
funciones, o cualquier otro caso de uso que no se haya enumerado aquí, ¡o
simplemente para decirme lo útil que encuentras este complemento!

### Inspiración

Este complemento es el resultado directo de peticiones que he visto de los
usuarios a lo largo de los años, y un debate en GitHub en la incidencia
[#9549](https://github.com/nvaccess/nvda/issues/9549). Muchas gracias a
@Qchristensen y @feerrenrut.

[[!tag dev stable]]

[1]: https://addons.nvda-project.org/files/get.php?file=numpadNav
