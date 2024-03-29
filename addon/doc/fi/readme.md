# Laskinnäppäimistön navigointitila #

# Laskinnäppäimistön navigointitila

* Tekijä: Luke Davis (Open Source Systems, Ltd.)
* Lataa [vakaa versio][1]

Laskinnäppäimistön navigointitila on [NVDA][2]-lisäosa, jonka avulla voit
helposti vaihtaa näppäimistön laskinosan NVDA:n navigointikomentojen ja
Windowsin liikkumiskomentojen välillä. Tästä voi olla hyötyä 1erityisesti
JAWSista NVDA:han siirtyville käyttäjille. Tämä lisäosa mahdollistaa myös
Numlock-näppäimen tilanvaihdon hallinnan sekä NVDA:n käynnistyessä että
valinnaisesti profiileissa.

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

Huom: Tämä lisäosa ei poista käytöstä laskinnäppäimistön Insertiä
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

Jos kuitenkin jaat tietokoneen näkevän käyttäjän kanssa, joka haluaa, että
Num Lock on aina käytössä, mutta itse pidät sitä poissa käytöstä, jotta
laskinnäppäimistö toimisi NVDA:n kanssa, saatat haluta, että Num Lock on
automaattisesti poissa käytöstä NVDA:n käynnistyessä. Vaihtoehtoisesti
saatat syöttää paljon tietoja ja haluat, että Num Lock on aina käytössä
käynnistäessäsi NVDA:n.

Siirry NVDA-valikkoon, valitse Asetukset -> Asetukset -> Laskinnäppäimistön navigointitila ja käytä "Numlockin tila NVDA:n käynnistyessä tai profiilin latautuessa" -valitsinta. Siinä on kolme vaihtoehtoa. Ensimmäinen, "Älä vaihda", ei vaihda Numlockin tilaa, ja se on oletusarvoisesti valittuna. Se on siinä tilassa, jossa se oli ennen NVDA:n käynnistymistä.
Toinen vaihtoehto on "Poista Numlock käytöstä", joka poistaa Numlocking käytöstä aina NVDA:n käynnistyessä. Kolmas vaihtoehto, "Ota Numlock käyttöön", ottaa Numlockin käyttöön, mikäli se ei ollut käytössä NVDA:n käynnistyessä.
Jos valitset joko toisen tai kolmannen vaihtoehdon, Numlock palautetaan NVDA:ta suljettaessa siihen tilaan, jossa se oli aiemmin. Esimerkiksi jos valitset "Poista Numlock käytöstä" -vaihtoehdon ja Numlock oli käytössä käynnistäessäsi NVDA:n, se poistetaan käytöstä NVDA:ta käyttäessäsi mutta otetaan uudelleen käyttöön, kun suljet NVDA:n.

#### Edistynyt käyttö

Jos käytät NVDA:n tehokkaita asetusprofiileja ja haluat Numlockin käyttöön
automaattisesti tiettyjen profiilien ollessa aktiivisia, tee seuraavasti:

* Kun "normaalit asetukset" -profiili on aktiivisena, siirry
  Laskinnäppäimistön navigointitilan asetuspaneeliin, joka on kuvailtu
  edellä. Valitse "Numlockin alkutila on riippuvainen asetusprofiilista"
  -valintaruutu. Tämä asetus ei ole oletusarvoisesti valittuna.
* Valitse OK.
* Vaihda profiiliin, jossa haluat Numlockin olevan aina pois käytöstä tai
  käytössä.
* Siirry takaisin Laskinnäppäimistön navigointitilan asetuspaneeliin ja
  valitse Numlockin käytöstä poistava tai käyttöön ottava asetus.
* Valitse OK. Nyt kun otat tämän profiilin käyttöön, Numlockin tila vaihtuu
  automaattisesti haluamaksesi.

Huom: Tämä on uusi ominaisuus, enkä tiedä, onko kellään sille käyttöä. Jos
löydät sille käyttökohteen, lähetä sähköpostia tai tee [raportti][3], jossa
kerrot, miten käytät sitä.

Vielä parempi on, jos jätät [arvostelun][4] lisäosalle ja kommentoit sitä
siellä! Arvostelut ovat erittäin hyödyllisiä, käytitpä kyseistä ominaisuutta
tai et.

### Uudet ominaisuudet

Kehotan tekemään [ongelmaraportin][3], tai lähettämään sähköpostitse
mahdollisia ominaisuusehdotuksia tai muita käyttötapauksia, joita ei tässä
ole lueteltu, tai vain ilmoittamaan, että lisäosa on hyödyllinen! Mutta
kuten yllä on mainittu, jos pidät tätä lisäosaa hyödyllisenä, ole hyvä ja
jätä [arvostelu][4].

### Historia

Tämä lisäosa on suora tulos pyynnöistä, joita tekijä on saanut vuosien
varrella käyttäjiltä sekä GitHub-keskustelussa
[#9549](https://github.com/nvaccess/nvda/issues/9549). Kiitos @Qchristensen
ja @feerrenrut. Numlock-ominaisuuksien perustoteutus on lainattu vanhasta
NumLock Manager -lisäosasta, jonka on tehnyt Noelia Ruiz (GitHubissa
@nvdaes) yhteistyössä muiden kanssa. Käyttölupa saatu.

### Muutosloki

(Tämä muutosloki on epätäydellinen. Katso lisätietoja Git-lokista.)

* 24.1.0: NVDA 2024.x -yhteensopivuus.
* 23.1.0: Lisätty Numlockin hallintaominaisuudet. Parempi lokin
  tallennus. Paranneltu asetusprofiilien käsittely (työn alla).
* 23.0: NVDA 2023.x -yhteensopivuus.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode

[2]: https://nvaccess.org/

[3]: https://github.com/opensourcesys/numpadNavMode/issues/new

[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
