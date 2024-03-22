# Numpad Nav Mode #

# Numpad Nav Mode

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Descargar [versión estable][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

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

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

 Ve al menú NVDA, Preferencias, Opciones, Numpad Nav Mode, y usa el selector "Estado del bloqueo numérico cuando arranca NVDA o se carga un perfil". Tiene tres opciones. La primera, "No modificar", es la que viene por defecto y no tocará el bloqueo numérico. Lo dejará en el estado que se encontraba cuando se inició NVDA.
La segunda opción, "Desactivar bloqueo numérico", desactivará siempre el bloqueo numérico cuando se inicie NVDA. La tercera opción, "Activar bloqueo numérico", activará el bloqueo numérico si estaba desactivado cuando se inició NVDA.
Si eliges tanto la segunda como la tercera opción, se restaurará el bloqueo numérico a su estado anterior al salir de NVDA. Por ejemplo, si eliges "Desactivar bloqueo numérico", y estaba encendido cuando iniciaste NVDA, se apagará mientras uses NVDA, pero se volverá a activar al salir.

#### Casos de uso avanzados

If you use NVDA's powerful configuration profiles, and you would like the
numlock to automatically turn on when you enter certain profiles, do the
following: * While in the "normal profile", go to the Numpad Nav Mode
settings panel described above. Check the box for "Initial numlock state is
configuration profile dependent". This option is unchecked by default.  *
Select OK.  * Change to the profile where you want numlock to be always
turned off or on.  * Go back to the Numpad Nav Mode settings panel, and
select the option to Turn numlock off or on, as you prefer.  * Then select
OK. Now, whenever you enter this profile, the numlock will automatically
change to the desired state.

Note that this is a new feature, and I don't know if anyone has use for this
feature. If you find one, please send an email or open [an issue][3], to let
me know how you have found to make use of it.

Or, better yet, leave a [review][4] for the add-on, and comment on it there!
Reviews are very helpful, whether or not you use that feature.

### Nuevas funciones

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Historial

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Registro de cambios

(Este registro de cambios está incompleto. Usa git log para obtener todos
los detalles.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: se añaden funciones de gestión del bloqueo numérico. Mejorado el
  registro. Mejorado el manejo de perfiles de configuración (WIP).
* 23.0: compatibilidad con NVDA 2023.x.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode [2]:
https://nvaccess.org/ [3]:
https://github.com/opensourcesys/numpadNavMode/issues/new [4]:
https://github.com/nvaccess/addon-datastore/discussions/2630
