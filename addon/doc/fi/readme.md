# Laskinnäppäimistön navigointitila #

# Numpad Nav Mode

* Tekijä: Luke Davis (Open Source Systems, Ltd.)
* Lataa [vakaa versio][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Navigointitilojen selitykset ja ominaisuudet

Tavalliset PC:n laskinnäppäimistön toiminnot Numlockin ollessa pois käytöstä
ovat: Page up, Page down, Home, End, nelisuuntaiset nuolinäppäimet sekä
Del-näppäin.  Mutta NVDA ottaa laskinnäppäimistön kokonaan käyttöönsä
tarjotakseen tekstintarkastelukomennot, hiiritoiminnot sekä
objektinavigointikomennot. Tämä pätee jopa kannettavien tietokoneiden
näppäimistöasettelussa, joka kahdentaa nämä toiminnot muihin kuin
laskinnäppäimistön näppäimiin niille, joilla ei ole laskinnäppäimistöä.

Joillakin käyttäjillä on kuitenkin kannettavissaan numeronäppäimistö, ja he
haluavat mieluummin käyttää sitä Windowsin navigointitarkoituksiin,
varsinkin koska joissakin kannettavissa tietokoneissa ei ole Home-, End- tai
muita vastaavia näppäimiä. Tällaisissa tilanteissa tästä lisäosasta on
apua. Lisäksi joillekin pöytäkoneen käyttäjille, esim. sellaisille, jotka
ovat tottuneet tapaan, jolla laskinnäppäimistö toimii JAWSissa, voi joskus
olla kätevää käyttää numeronäppäimiä näihin näppäimistötoimintoihin
tavallisten NVDA-näppäinten sijaan, jonka tämä lisäosa mahdollistaa. Näihin
sisältyy suosittu JAWS-komento laskinnäppäimistön Insert+laskinnäppäimistön
2 lukemiseen kohdistimen nykyisestä kohdasta tekstin loppuun saakka, joka
oli tämän lisäosan varhaisten käyttäjien erityinen ominaisuuspyyntö.

### Kuinka se toimii

Kun Numlock on poissa päältä, riippumatta siitä, mitä näppäimistöasettelua
käytät, tämän lisäosan avulla voit painaa Alt+NVDA+laskinnäppäimistön plus
(joka on yleensä pitkä näppäin toiseksi ylimpänä oikealla) siirtyäksesi
nopeasti ja helposti normaalin NVDA-navigoinnin ja perinteisen
Windows-navigoinnin välillä. Tämä näppäin on mahdollista uudelleenmäärittää
Näppäinkomennot-valintaikkunan Syöttö-kategoriassa.

Huom: Tämä lisäosa ei poista käytöstä numeronäppäimistön Insertiä
NVDA-näppäimenä, jos olet ottanut sen käyttöön. Ilmoita minulle, jos haluat
tämän ominaisuuden, vaikka sen voikin poistaa käytöstä manuaalisesti NVDA:n
näppäimistöasetuksista. Tämä lisäosa ei myöskään muuta laskinnäppäimistön
deleten (0- ja Enter-näppäinten välissä) NVDA-toiminnallisuutta. Ota
yhteyttä, jos haluat tämän ominaisuuden.

Jos haluat NVDA:n käynnistyvän oletusarvoisesti Windows-navigointitilassa,
voit määrittää sen NVDA:n asetuksista. Valitse NVDA-valikosta Asetukset ->
Asetukset, ja etsi sitten Laskinnäppäimistön navigointitila -vaihtoehto,
joka avaa lisäosan asetuspaneelin. Sieltä voit valita valintaruudun, joka
ottaa oletusarvoisesti käyttöön Windows-navigointitilan NVDA:n
käynnistyessä. Pääset asetuspaneeliin nopeasti painamalla NVDA+N, A, A ja
sitten kerran tai useammin L, kunnes kuulet "Laskinnäppäimistön
navigointitila".

### Numlockin ominaisuudet

Oletusarvoisesti Numlock-näppäimelle ei tehdä mitään.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

Siirry NVDA-valikkoon, valitse Asetukset -> Asetukset -> Laskinnäppäimistön navigointitila ja käytä "Numlockin tila NVDA:n käynnistyessä tai profiilin latautuessa" -valitsinta. Siinä on kolme vaihtoehtoa. Ensimmäinen, "Älä vaihda", ei vaihda Numlockin tilaa, ja se on oletusarvoisesti valittuna. Se on siinä tilassa, jossa se oli ennen NVDA:n käynnistymistä.
Toinen vaihtoehto on "Poista Numlock käytöstä", joka poistaa Numlocking käytöstä aina NVDA:n käynnistyessä. Kolmas vaihtoehto, "Ota Numlock käyttöön", ottaa Numlockin käyttöön, mikäli se ei ollut käytössä NVDA:n käynnistyessä.
Jos valitset joko toisen tai kolmannen vaihtoehdon, Numlock palautetaan NVDA:ta suljettaessa siihen tilaan, jossa se oli aiemmin. Esimerkiksi jos valitset "Poista Numlock käytöstä" -vaihtoehdon ja Numlock oli käytössä käynnistäessäsi NVDA:n, se poistetaan käytöstä NVDA:ta käyttäessäsi, mutta otetaan uudelleen käyttöön, kun suljet NVDA:n.

#### Edistynyt käyttö

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

### Uudet ominaisuudet

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Historia

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Muutosloki

(Tämä muutosloki on epätäydellinen. Katso lisätietoja Git-lokista.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Lisätty Numlockin hallintaominaisuudet. Parempi lokin
  tallennus. Paranneltu asetusprofiilien käsittely (työn alla).
* 23.0: NVDA 2023.x -yhteensopivuus.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode [2]:
https://nvaccess.org/ [3]:
https://github.com/opensourcesys/numpadNavMode/issues/new [4]:
https://github.com/nvaccess/addon-datastore/discussions/2630
