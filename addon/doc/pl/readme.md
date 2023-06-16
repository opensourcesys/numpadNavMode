# Numpad Nav Mode #

* Autor: Luke Davis (Open Source Systems, Ltd.)
* Pobierz [wersja stabilna][1]

Numpad Nav Mode to dodatek [NVDA](https://nvaccess.org/), który umożliwia
łatwe przełączanie klawiatury między kontrolkami nawigacyjnymi NVDA a
kontrolkami nawigacji systemu Windows bez czytnika ekranu. Może to być
szczególnie przydatne dla użytkowników migrujących z Jaws do NVDA. Ten
dodatek zapewnia również szczegółową kontrolę nad przełączaniem numlock,
zarówno podczas uruchamiania NVDA, jak i opcjonalnie w profilach.

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

Jeśli jednak dzielisz swój komputer z widzącym użytkownikiem, który woli,
aby numlock był zawsze włączony, ale wolisz, aby klawiatura numeryczna
działała z NVDA, możesz chcieć, aby numlock był automatycznie wyłączany
podczas uruchamiania NVDA.  Alternatywnie, możesz wprowadzić wiele danych,
więc wolisz, aby numlock był zawsze włączony podczas uruchamiania NVDA.

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

Zauważ, że jest to nowa funkcja i nie wiem, czy ktoś ma z niej
skorzystać. Jeśli go znajdziesz, wyślij e-mail lub otwórz
[problem](https://github.com/opensourcesys/numpadNavMode/issues/new), aby
dać mi znać, jak znalazłeś, aby z niego skorzystać.

### Nowe funkcje

Zachęcam do opublikowania [problemu]
(https://github.com/openSourceSys/numpadNavMode/issues/new) lub e-maila z
sugestiami funkcji lub innymi przypadkami użycia, których tutaj nie
wymieniłem, lub po prostu dać mi znać, że dodatek jest przydatny!

### Historia

Ten dodatek był bezpośrednim wynikiem próśb, które widziałem od użytkowników
na przestrzeni lat, oraz dyskusji na GitHub w
[#9549](https://github.com/nvaccess/nvda/issues/9549). Z podziękowaniami dla
@Qchristensen i @feerrenrut.  Podstawowa implementacja funkcji numlock
została zapożyczona ze starszego dodatku NumLock Manager przez Noelię Ruiz
(@nvdaes na GitHub) i innych. Użyte za zgodą.

### Lista zmian

(Ten dziennik zmian jest niekompletny. Zobacz Dziennik Git, aby uzyskać
szczegółowe informacje).

* 23.0: Zgodność z NVDA 2023.X.

* 23.1.0: Dodano funkcje zarządzania numlock. Lepsze
  rejestrowanie. Ulepszona obsługa profili konfiguracji (WIP).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode
