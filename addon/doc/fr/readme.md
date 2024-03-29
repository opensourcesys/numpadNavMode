# Numpad Nav Mode #

# Numpad Nav Mode

* Auteur : Luke Davis (Open Source Systems, Ltd.)
* Télécharger [version stable][1]

Numpad Nav Mode est une extension [NVDA][2], qui vous permet de basculer
facilement le pavé numérique de votre clavier entre les commandes de
navigation de NVDA et les commandes de navigation Windows sans lecteur
d'écran. Cela peut être particulièrement utile pour les utilisateurs migrant
de Jaws vers NVDA. Cette extension donne également un contrôle de finesse
sur la bascule de la touche verrouillage numérique, à la fois lorsque NVDA
démarre, et éventuellement dans les profils.

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

Cependant, si vous partagez votre ordinateur avec un utilisateur voyant qui
préfère que le verrouillage numérique soit toujours activé, mais que vous
aimez le désactiver pour que le pavé numérique fonctionne avec NVDA, vous
souhaiterez peut-être que le verrouillage numérique soit automatiquement
désactivé au démarrage de NVDA. Alternativement, vous pouvez saisir beaucoup
de données et préférer donc que le verrouillage numérique soit toujours
activé lorsque vous démarrez NVDA.

 Allez dans le menu NVDA, Préférences,  Paramètres, Numpad Nav Mode et utilisez le sélecteur "État du verrouillage numérique lorsque NVDA démarre ou le profil se charge". Cela a trois options. Le premier, "Ne changez pas", celui-ci est par défaut, et ne touchera pas le verrouillage numérique. Ce sera dans quel que soit le state dans lequel il se trouvait avant le démarrage de NVDA.
La deuxième option, est "Basculer verrouillage numérique désactivé", ce qui désactivera toujours le verrouillage numérique lorsque NVDA démarre. La troisième option "Basculer verrouillage numérique activé", ce qui activera le verrouillage numérique s'il était désactivé lorsque NVDA a démarré.
Si vous choisissez soit la deuxième ou la troisième option, le verrouillage numérique sera restauré dans n'importe quel état dans lequel il se trouvait avant, lorsque vous quittez NVDA. Par exemple, si vous choisissez "Basculer verrouillage numérique désactivé", et le verrouillage numérique était activé lorsque vous avez démarré NVDA: il sera désactivé pendant que vous utilisez NVDA, mais sera  réactivé lorsque vous quittez NVDA.

#### Cas d'utilisation avancée

Si vous utilisez les puissants profils de configuration de NVDA et que vous
souhaitez que le verrouillage numérique s'active automatiquement pendant le
basculement lorsque vous entrez certains profils, procédez comme suit :

* Pendant que dans le "profil normal", accédez au panneau de paramètres
  Numpad Nav Mode décrit ci-dessus. Cochez la case pour "L'état de
  verrouillage numérique initial est dépendant du profil de
  configuration". Cette option n'est pas cochée par défaut.
* Sélectionnez OK.
* Passez au profil où vous voulez que le verrouillage numérique soit
  toujours basculé entre désactivé ou activé.
* Retournez au panneau des paramètres Numpad Nav Mode et sélectionnez
  l'option pour Basculer verrouillage numérique désactivé ou activé, comme
  vous préférez.
* Puis sélectionnez OK. Maintenant, chaque fois que vous entrez ce profil,
  le verrouillage numérique passera automatiquement à l'état souhaité.

Notez qu'il s'agit d'une nouvelle fonctionnalité, et je ne sais pas si
quelqu'un l'a utilisé pour cette fonctionnalité. Si vous en trouvez une,
veuillez envoyer un courriel ou ouvrez [un issue][3], pour me faire savoir
comment vous l'avez trouvé celle-ci.

Ou, mieux encore, laissez un [avis (review)][4] pour l'extension et
commentez-le ici ! Les avis sont très utiles, que vous utilisiez ou non
cette fonctionnalité.

### Nouvelles fonctionnalités

Je vous encourage à envoyer un [issue][3], ou un courriel des suggestions de
fonctionnalités ou d'autres cas d'utilisation que je n'ai pas répertoriés
ici, ou simplement pour me faire savoir que vous trouvez l'extension utile !
Mais comme mentionné ci-dessus, si vous le trouvez utile, veuillez laisser
un [avis (review)][4].

### Histoire

Cette extension est le résultat direct des demandes que j'ai reçues
d'utilisateurs au fil des ans et d'une discussion GitHub dans
[#9549](https://github.com/nvaccess/nvda/issues/9549). Remerciements à
@Qchristensen et @feerrenrut.  L'implémentation de base des fonctionnalités
de numlock  a été empruntée à l'extension NumLock Manager, par Noelia Ruiz
(@nvdaes sur GitHub), et autres. Utilisé avec permission.

### Journal des changements

(Ce journal des changements est incomplet. Voir le journal de Git pour plus
de détails.)

* 24.1.0 : Compatibilité NVDA 2024.X.
* 23.1.0 : Ajout des fonctionnalités de gestion de verrouillage
  numérique. Meilleur journalisation. Manipulation améliorée du profil de
  configuration (WIP).
* 23.0 : compatibilité NVDA 2023.X.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode

[2]: https://nvaccess.org/

[3]: https://github.com/opensourcesys/numpadNavMode/issues/new

[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
