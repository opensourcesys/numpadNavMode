# Numpad Nav Mode #

# Numpad Nav Mode

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Pobierz [wersja stabilna][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Objaśnienie i funkcje trybów nawigacji

Normalne funkcje klawiatury numerycznej komputera, z wyłączonym numlockiem,
to: strona w górę, strona w dół, strona główna, koniec, czterokierunkowe
strzałek i usuwania.  Ale NVDA całkowicie przejmuje klawiaturę numeryczną,
aby zapewnić przeglądu, sterowanie myszą i sterowanie nawigacją po
obiektach. Dzieje się tak nawet w trybie klawiatury laptopa, który również
powiela te funkcje na innych niż numeryczne.

Jednak niektórzy użytkownicy mają klawiaturę numeryczną na swoim laptopie i
woleliby używać jej do celów nawigacyjnych systemu Windows (przynajmniej
przez pewien czas), zwłaszcza że niektóre laptopy nie zapewniają klucza
domowego, końcowego lub innych tego typu.  W tym właśnie może pomóc ten
dodatek.  Ponadto niektórzy użytkownicy komputerów stacjonarnych, na
przykład przyzwyczajeni do sposobu działania klawiatury numerycznej w JAWS,
mogą czasami uznać za wygodne używanie klawiatury numerycznej do tych
funkcji klawiatury zamiast zwykłych NVDA, które umożliwia ten dodatek.
Obejmuje to popularne polecenie JAWS NumpadInsert + Numpad2, do odczytu do
końca, które było specyficznym żądaniem funkcji od niektórych wczesnych
użytkowników tego dodatku.

### Jak to działa

Po wyłączeniu numlock, bez względu na to, jakiego układu klawiatury używasz,
ten dodatek pozwoli Ci nacisnąć Alt + NVDA + NumpadPlus (który zwykle jest
długim sekundę po prawej stronie), aby szybko i łatwo przełączać się między
normalnymi kontrolkami nawigacji NVDA a klasycznymi kontrolkami nawigacji
systemu Windows. Ten można ponownie zamapować w obszarze Gesty wprowadzania
w sekcji Wejście.

Zauważ, że ten dodatek nie wyłącza używania klawiatury numerycznej jako
modyfikatora NVDA, jeśli jest tak ustawiona. Jeśli chcesz tej funkcji, daj
mi znać, chociaż możesz ręcznie wyłączyć wkładkę numeryczną jako modyfikator
w ustawieniach klawiatury NVDA. Nie zmienia to również funkcji NVDA numpad
delete (klucz między zerem a enter) - skontaktuj się ze mną, jeśli sobie
tego życzysz.

Jeśli wolisz, aby NVDA uruchamiało się z domyślnie aktywnym trybem nawigacji
systemu Windows, możesz skonfigurować to w konfiguracji NVDA.  Przejdź do
preferencji NVDA, a następnie ustawień i znajdź panel ustawień trybu Numpad
Nav Mode.  Tam będziesz mógł zaznaczyć pole wyboru, aby domyślnie włączyć
tryb nawigacji systemu Windows po uruchomieniu NVDA.  Aby szybko się tam
dostać, naciśnij NVDA+N, P, S, a następnie N jeden lub więcej razy, aż
usłyszysz "Numpad Nav Mode".

### Funkcje Numlock

Domyślnie nic nie jest wykonywane za pomocą numlock.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

 Przejdź do menu NVDA, Preferencje, Ustawienia, Tryb Numpad Nav i użyj selektora "stan numlock podczas uruchamiania NVDA lub ładowania profilu". Ma trzy opcje. Pierwszy, "nie zmieniaj", jest domyślny i nie dotyka numlocka. Będzie w takim stanie, w jakim był przed rozpoczęciem NVDA.
Drugą opcją jest "turn numlock off", która zawsze wyłączy numlock po uruchomieniu NVDA. Trzecia opcja, "Włącz numlock", włączy numlock, jeśli był wyłączony podczas uruchamiania NVDA.
Jeśli wybierzesz drugą lub trzecią opcję, numlock zostanie przywrócony do stanu, w którym był wcześniej, po zamknięciu NVDA. Na przykład, jeśli wybierzesz opcję "Turn numlock off", a numlock był włączony podczas uruchamiania NVDA: zostanie on wyłączony podczas korzystania z NVDA, ale zostanie ponownie włączony po wyjściu z NVDA.

#### Zaawansowane przypadki użycia

Jeśli używasz potężnych profili konfiguracyjnych NVDA i chcesz, aby numlock
włączał się automatycznie po wprowadzeniu niektórych profili, wykonaj
następujące czynności:

* W "normalnym profilu" przejdź do panelu ustawień trybu Numpad Nav
  opisanego powyżej. Zaznacz pole wyboru "Początkowy stan numlock jest
  zależny od profilu konfiguracji". Ta opcja nie jest domyślnie zaznaczona.
* Wybierz przycisk OK.
* Przejdź do profilu, w którym numlock ma być zawsze wyłączony lub włączony.
* Wróć do panelu ustawień trybu Numpad Nav i wybierz opcję Wyłącz lub włącz
  numlock, jak wolisz.
* Następnie wybierz przycisk OK. Teraz, za każdym razem, gdy wejdziesz do
  tego profilu, numlock automatycznie zmieni się na żądany stan.

Note that this is a new feature, and I don't know if anyone has use for this
feature. If you find one, please send an email or open [an issue][3], to let
me know how you have found to make use of it.

Or, better yet, leave a [review][4] for the add-on, and comment on it there!
Reviews are very helpful, whether or not you use that feature.

### Nowe funkcje

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

### Lista zmian

(Ten dziennik zmian jest niekompletny. Zobacz Dziennik Git, aby uzyskać
szczegółowe informacje).

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Dodano funkcje zarządzania numlock. Lepsze
  rejestrowanie. Ulepszona obsługa profili konfiguracji (WIP).
* 23.0: Zgodność z NVDA 2023.X.

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode

[2]: https://nvaccess.org/

[3]: https://github.com/opensourcesys/numpadNavMode/issues/new

[4]: https://github.com/nvaccess/addon-datastore/discussions/2630
