# Modus navigacije s numeričkim blokom (Numpad Nav Mode) #

# Numpad Nav Mode

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Preuzmi [stabilnu verziju][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Objašnjenje i funkcije modusa navigacije

Uobičajene funkcije numeričkog bloka na računalu s isključenom numeričkim
blokom su: stranica prema gore, stranica prema dolje, početak, kraj, tipke
sa strelicama i tipka za brisanje. Međutim NVDA u potpunosti preuzima
numerički blok, pružajući tipke za pregled, funkcije miša i funkcije za
kretanja po objektima. To vrijedi čak i u modusu tipkovnice prijenosnog
računala, koji te funkcije također duplicira na tipkama nenumeričkog bloka.

Međutim, neki korisnici na svom prijenosnom računalu imaju numerički blok i
radije bi njega koristili za kretanje u Windowsu, naročito jer neka
prijenosna računala nemaju tipke za početak, kraj i slične tipke. Ovaj
dodatak može pomoći u takvim slučajevima. Uz to, neki korisnici desktop
računala, na primjer oni koji su navikli na način na koji tipkovnica
numeričkog bloka radi u JAWS-u, mogu ponekad smatrati prikladnijim koristiti
tipkovnicu numeričkog bloka za te funkcije tipkovnice umjesto normalnih NVDA
tipki, koje ovaj dodatak omogućuje. To uključuje popularnu JAWS naredbu
NumpadInsert+Numpad2 za čitanje do kraja, što je bila posebna funkcija koju
su zahtijevali neki prvi korisnici ovog dodatka.

### Opis rada

S isključenim numeričkim blokom i bez obzira na korišteni raspored
tipkovnice, ovaj dodatak omogućuje pritiskanje tipki Alt+NVDA+num plus (što
je obično druga dugačka tipka odozdo na desnoj strani) za brzo i jednostavno
prebacivanje između normalnih kontrola navigacije NVDA čitača i klasičnih
Windows kontrola. Ovaj se prečac može promijeniti pod „Ulazne geste” u
odjeljku „Unos”.

Ovaj dodatak ne onemogućava upotrebu tipke insert na numeričkom bloku kao
modifikacijske tipke za NVDA, ako je kao takva postavljena. Tko tu funkciju
želi, može mi se slobodno javiti, iako se upotreba tipke insert na
numeričkom bloku može i ručno isključiti u NVDA postavkama
tipkovnice. Također ne mijenja NVDA funkciju tipke dilit u numeričkom bloku
(tipka između nule i enter) – kontaktiraj me ako to želite.

Pokretanje NVDA čitača sa standardnim Windows modusom navigacije može se
konfigurirati u NVDA konfiguraciji. Idi na NVDA postavke, zatim postavke i
pronađi ploču postavki „Modus navigacije s numeričkim blokom”. Tamo se može
označiti potvrdni okvir za uključivanje Windows modusa navigacije kao
standardnog modus prilikom pokretanja NVDA čitača. Za brzi prijelaz na to
mjesto, pritisni NVDA+N, P, S, a zatim N jednom ili više puta, sve dok ne
čuješ „Modus navigacije s numeričkim blokom”.

### Funkije numeričkog bloka

Standardno se ništa ne radi s tipkom za uključivanje/isključivanje
numeričkog bloka.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

 Go to NVDA menu, Preferences, Settings, Numpad Nav Mode, and use the "state of numlock when NVDA starts or profile loads" selector. This has three options. The first, "do not change", is the default, and won't touch the numlock. It will be in whatever state it was in before NVDA started.
The second option, is "turn numlock off", which will always turn the numlock off when NVDA starts. The third option, "Turn numlock on", will turn the numlock on if it was off when NVDA started.
If you choose either the second or third option, the numlock will be restored to whatever state it was in before, when you exit NVDA. For example, if you choose "Turn numlock off", and numlock was on when you started NVDA: it will be turned off while you use NVDA, but will be turned back on when you exit NVDA.

#### Advanced use cases

If you use NVDA's powerful configuration profiles, and you would like the
numlock to automatically turn on when you enter certain profiles, do the
following:

* While in the "normal profile", go to the Numpad Nav Mode settings panel
  described above. Check the box for "Initial numlock state is configuration
  profile dependent". This option is unchecked by default.
* Select OK.
* Change to the profile where you want numlock to be always turned off or
  on.
* Go back to the Numpad Nav Mode settings panel, and select the option to
  Turn numlock off or on, as you prefer.
* Then select OK. Now, whenever you enter this profile, the numlock will
  automatically change to the desired state.

Note that this is a new feature, and I don't know if anyone has use for this
feature. If you find one, please send an email or open [an issue][3], to let
me know how you have found to make use of it.

Or, better yet, leave a [review][4] for the add-on, and comment on it there!
Reviews are very helpful, whether or not you use that feature.

### Nove funkcije

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Povijest

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Zapis promjena

(Ovaj zapis promjena nije potpun. Pogledaj Git zapise za detalje.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Dodane su funkcije upravljanja za uključivanje/isključivanje
  numeričkog bloka. Bolje zapisivanje. Poboljšano rukovanje konfiguracijskim
  profilom (rad u tijeku).
* 23.0: NVDA 2023.X kompatibilnost.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode

[2]: https://nvaccess.org/

[3]: https://github.com/opensourcesys/numpadNavMode/issues/new

[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
