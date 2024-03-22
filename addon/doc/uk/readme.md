# Numpad Nav Mode (Режим навігації за допомогою цифрової клавіатури) #

# Numpad Nav Mode

* Автор: Luke Davis (Open Source Systems, Ltd.)
* Завантажити [стабільну версію][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Пояснення та особливості режимів навігації

Звичайними функціями цифрової клавіатури комп’ютера з вимкненою клавішею
numlock є: сторінка вгору, сторінка вниз, додому, вкінець, клавіші зі
стрілками в чотирьох напрямках і клавіша видалення.  Але NVDA повністю
перебирає на себе функції цифрової клавіатури, надаючи клавіші для
перегляду, керування мишею та навігації по об'єктах. Це стосується навіть
режиму клавіатури ноутбука, яка також дублює ці функції на клавішах, що не
належать до цифрової клавіатури.

Однак деякі користувачі мають на своєму ноутбуці цифрову клавіатуру і
воліють використовувати її для навігації у Windows (принаймні деякий час),
особливо тому, що деякі ноутбуки не мають клавіш "Додому", "Вкінець" або
інших подібних клавіш.  Саме тут може знадобитися цей додаток.  Крім того,
деяким користувачам настільних комп’ютерів, наприклад тим, хто звик до
роботи цифрової клавіатури в JAWS, іноді може бути зручно використовувати
цифрову клавіатуру для цих функцій клавіатури, а не звичайні клавіші NVDA,
які вмикає цей додаток.  Сюди входить популярна JAWS-команда
NumpadInsert+Numpad2, для читання до кінця, що було особливим побажанням
деяких перших користувачів цього додатка.

### Як це працює

Якщо numlock вимкнено, незалежно від того, яку розкладку клавіатури ви
використовуєте, цей додаток дозволить вам натиснути Alt+NVDA+NumpadPlus
(зазвичай це довга клавіша, друга праворуч), щоб швидко і легко перемикатися
між звичайними елементами керування навігацією NVDA і класичними елементами
керування навігацією Windows. Цю клавішу можна перепризначити у пункті Жести
вводу у розділі Введення.

Зауважте, що цей додаток не вимикає використання insert numpad як
модифікатора клавіатури NVDA, якщо вона у вас встановлена як така. Якщо вам
потрібна ця функція, будь ласка, дайте мені знати, хоча ви можете вручну
вимкнути клавішу insert як модифікатор у налаштуваннях клавіатури NVDA. Це
також не змінює функцію клавіш numpad delete (клавіша між нулем і
enter)--зв'яжіться зі мною, якщо ви бажаєте це зробити.

Якщо ви бажаєте, щоб NVDA початково запускалася з активним режимом навігації
Windows, ви можете налаштувати це в налаштуваннях NVDA. Перейдіть до
параметрів NVDA, потім до налаштувань і знайдіть панель налаштувань (Режим
навігації за допомогою цифрової клавіатури). Там ви зможете встановити
прапорець, щоб увімкнути режим навігації Windows під час запуску NVDA.

### Функції Numlock

Початково клавіша numlock нічого не робить.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

 Перейдіть до меню NVDA, Параметри, Налаштування, Режим навігації за допомогою цифрової клавіатури і скористайтеся комбінованим списком "Стан numlock під час запуску NVDA або завантаження профілю". Тут є три варіанти. Перший, початково "не змінювати" не стосується numloc. Він залишиться у тому стані, у якому був до запуску NVDA.  Другий варіант — «вимкнути numlock», який завжди вимикатиме numlock під час запуску NVDA. Третій варіант, «Увімкнути numlock», увімкне numlock, якщо він був вимкнений під час запуску NVDA.  Якщо ви виберете другий або третій варіант, numlock буде відновлено до того стану, у якому він був раніше, коли ви вийдете з NVDA. Наприклад, якщо ви вибрали «Вимкнути numlock», а numlock було ввімкнено під час запуску NVDA: він буде вимкнений, поки ви використовуєте NVDA, але знову ввімкнеться, коли ви вийдете з NVDA.

#### Розширені варіанти використання

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

### Нові функції

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Історія

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Журнал змін

(Цей журнал змін неповний. Дивіться журнал Git для повної інформації.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Added numlock management features. Better logging. Improved config
  profile handling (WIP).
* 23.0: NVDA 2023.X compatibility.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode [2]:
https://nvaccess.org/ [3]:
https://github.com/opensourcesys/numpadNavMode/issues/new [4]:
https://github.com/nvaccess/addon-datastore/discussions/2630
