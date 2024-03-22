# Numpad Nav Mode #

# Numpad Nav Mode

* Auteur : Luke Davis (Open Source Systems, Ltd.)
* Télécharger [version stable][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Modes de navigation, explication et fonctionnalités

Les fonctions normales du pavé numérique du PC, avec le verrouillage
numérique désactivé, sont les suivantes : page précédente, page suivante,
début, fin, les quatre touches fléchées directionnelles et la touche de
suppression. Mais NVDA prend complètement en charge le pavé numérique, pour
fournir des touches de révision, des commandes de souris et des commandes de
navigation dans les objets. Cela est vrai même en mode clavier d'ordinateur
portable, qui duplique ces fonctions sur des touches sans pavé numérique
pour ceux qui n'ont pas de pavé numérique.

Cependant, certains utilisateurs ont un pavé numérique sur leur ordinateur
portable et préféreraient l'utiliser à des fins de navigation Windows (au
moins une partie du temps), en particulier parce que certains ordinateurs
portables ne fournissent pas de touches début, fin ou autres de ce
type. C'est là que cette extension peut vous aider. De plus, certains
utilisateurs de bureau, , par exemple ceux habitués à la façon dont le pavé
numérique fonctionne dans JAWS, peuvent parfois trouver plus pratique
d'utiliser le pavé numérique pour ces fonctions du clavier plutôt que les
touches de NVDA normales, ce que cette extension permet. Cela inclut la
populaire  commande JAWS NumpadInsert+Numpad2, pour lire jusqu'à la fin, qui
était une demande de fonctionnalité spécifique de certains premiers
utilisateurs de cette extension.

### Comment ça marche

Avec verrouillage numérique désactivé, quelle que soit la disposition du
clavier que vous utilisez, cette extension vous permettra d'appuyer sur
Alt+NVDA+pavnumPlus (qui est généralement la longue touche en haut à
droite), pour basculer rapidement et facilement entre les contrôles de
navigation NVDA normale et les contrôles de navigation classiques de
Windows. Cette touche peut être remappée sous Gestes de commande, dans la
section Entrée.

Notez que cette extension ne désactive pas l'utilisation de l'insertion du
pavé numérique en tant que modificateur NVDA, si vous l'avez défini comme
tel. Si vous voulez cette fonctionnalité, faites-le moi savoir, bien que
vous puissiez désactiver manuellement l'insertion du pavé numérique en tant
que modificateur dans les paramètres de clavier NVDA.  Il ne modifie pas non
plus la fonction NVDA de Numpad Delete (touche entre zéro et Entrée)--
contactez-moi si vous le souhaitez.

Si vous préférez que NVDA démarre avec le mode de navigation Windows actif
par défaut, vous pouvez le configurer dans la configuration de NVDA. Accédez
aux préférences de NVDA, puis aux paramètres, et recherchez le panneau des
paramètres Numpad Nav Mode. Là, vous pourrez sélectionner une case à cocher
pour activer le mode de navigation Windows par défaut lorsque vous démarrez
NVDA. Pour vous y rendre rapidement, appuyez une ou plusieurs fois sur
NVDA+N, P, S, puis sur N jusqu'à ce que vous entendiez "Numpad Nav Mode".

### Fonctionnalités de verrouillage numérique

Par défaut, rien n'est fait avec la touche verrouillage numérique.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

 Allez dans le menu NVDA, Préférences,  Paramètres, Numpad Nav Mode et utilisez le sélecteur "État du verrouillage numérique lorsque NVDA démarre ou le profil se charge". Cela a trois options. Le premier, "Ne changez pas", celui-ci est par défaut, et ne touchera pas le verrouillage numérique. Ce sera dans quel que soit le state dans lequel il se trouvait avant le démarrage de NVDA.
La deuxième option, est "Basculer verrouillage numérique désactivé", ce qui désactivera toujours le verrouillage numérique lorsque NVDA démarre. La troisième option "Basculer verrouillage numérique activé", ce qui activera le verrouillage numérique s'il était désactivé lorsque NVDA a démarré.
Si vous choisissez soit la deuxième ou la troisième option, le verrouillage numérique sera restauré dans n'importe quel état dans lequel il se trouvait avant, lorsque vous quittez NVDA. Par exemple, si vous choisissez "Basculer verrouillage numérique désactivé", et le verrouillage numérique était activé lorsque vous avez démarré NVDA: il sera désactivé pendant que vous utilisez NVDA, mais sera  réactivé lorsque vous quittez NVDA.

#### Cas d'utilisation avancée

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

### Nouvelles fonctionnalités

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Histoire

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Journal des changements

(Ce journal des changements est incomplet. Voir le journal de Git pour plus
de détails.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0 : Ajout des fonctionnalités de gestion de verrouillage
  numérique. Meilleur journalisation. Manipulation améliorée du profil de
  configuration (WIP).
* 23.0 : compatibilité NVDA 2023.X.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode [2]:
https://nvaccess.org/ [3]:
https://github.com/opensourcesys/numpadNavMode/issues/new [4]:
https://github.com/nvaccess/addon-datastore/discussions/2630
