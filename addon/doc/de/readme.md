# Nummernblock-Navigationsmodus #

# Numpad Nav Mode

* Autor: Luke Davis (Open Source Systems, Ltd.)
* [Stabile Version herunterladen][1]

Numpad Nav Mode is an [NVDA][2] add-on, which allows you to easily switch
your keyboard's numpad between NVDA's navigation controls and the
non-screenreader Windows navigation controls. This can be especially useful
for users migrating from Jaws to NVDA. This add-on also gives granular
control over the numlock key toggle, both when NVDA starts, and optionally
in profiles.

### Erklärung der Navigationsmodi und Funktionen

Die normalen Funktionen des Nummernblock bei deaktivierter Funktion des
Nummernblocks sind: Seite nach oben, Seite nach unten, Home, Ende,
Vier-Wege-Pfeiltasten und eine Löschtaste. NVDA übernimmt jedoch den
Nummernblock vollständig, um Tasten zur Ansicht, Maussteuerung und
Objektnavigationssteuerung bereitzustellen. Dies gilt auch für den
Tastaturmodus am Laptop, der diese Funktionen auch ohne Nummernblock
dupliziert.

Einige Benutzer haben jedoch einen Nummernblock auf dem Laptop und würden
diesen gerne für die Windows-Navigation verwenden (zumindest zeitweise), vor
allem, weil einige Laptops keine Pos1-, Ende- oder andere derartige Tasten
haben. In diesem Fall kann diese NVDA-Erweiterung helfen. Darüber hinaus
finden es manche Benutzer am einem Desktop-PC, die beispielsweise an die
Funktionsweise des Nummernblocks in JAWS gewöhnt sind, manchmal bequemer,
den ihn für diese Tastaturfunktionen zu verwenden, als die normalen
NVDA-Tasten, was diese NVDA-Erweiterung ermöglicht.  Dies gilt auch für den
beliebten JAWS-Befehl Nummernblock-Einfügen+Nummernblock 2 zum Lesen bis zum
Ende, der ein spezieller Funktionswunsch einiger früherer Benutzer diese
NVDA-Erweiterung war.

### Funktionsweise

Bei ausgeschaltetem Nummernblock und in allen Tastaturschemen können Sie
alt+NVDA+Nummernblock plus betätigen, um zwischen den bekannten
NVDA-Navigationsbefehlen sowie den Windows-Navigationsbefehlen zu
wechseln. Zumeist ist Nummernblock plus die obere längere Taste ganz rechts
auf der Tastatur. Die Tastenkombination kann man im Dialog Tastenbefehle
unter Eingabe anpassen.

Beachten Sie, dass diese NVDA-Erweiterung nicht die Verwendung des
Nummernblocks als NVDA-Modifikator deaktiviert, wenn Sie ihn als solchen
eingestellt haben. Wenn Sie diese Funktion wünschen, lassen Sie es dem Autor
bitte wissen, obwohl Sie die Einfügung des Nummernblocks als Modifikator in
den NVDA-Tastatureinstellungen manuell deaktivieren können. Auch die
NVDA-Funktion des Nummernblocks zum Löschen (Taste zwischen Null und Enter)
wird nicht verändert - kontaktieren Sie ebenfalls den Autor, wenn Sie dies
wünschen.

Wenn Sie wollen, dass beim Start von NVDA der Windows-Navigations-Modus
aktiv ist, können Sie dies in den Einstellungen von NVDA festlegen. Gehen
Sie hierzu in die Optionen -> Einstellungen und suchen Sie dort den Eintrag
Nummernblock-Navigations-modus. Dort finden Sie ein Kontrollfeld, welches
ermöglicht, die Windows-Navigation beim NVDA-Start einzuschalten. Um schnell
dort hin zu kommen, drücken Sie NVDA+N, o, e und mehrere male n, bis Sie
"Nummernblock-Navigations-Modus" hören.

### Nummernblock-Features

Standardmäßig wird mit der Taste des Nummernblocks nichts gemacht.

However, if you share your computer with a sighted user who prefers that
numlock always be turned on, but you like having it off so that the numpad
works with NVDA, you may want the numlock to automatically turned off when
NVDA starts.  Alternatively, you may enter a lot of data, and so prefer the
numlock to always be on when you start NVDA.

Gehen Sie in das NVDA-menü, Optionen, Einstellungen, Navigationsmodus des Nummernblocks, und verwenden Sie die Option "Status des Nummernblocks beim Start von NVDA oder beim Laden des Profils". Hier gibt es drei Optionen. Die erste, "Nicht ändern", ist die Standard-Einstellung, die den Nummernblock nicht verändert. Es bleibt in dem Zustand, in dem er sich vor dem Start von NVDA befand.
Die zweite Option, "Nummernblock ausschalten", schaltet den Nummernblock beim Start von NVDA immer aus. Die dritte Option, "Nummernblock einschalten", schaltet den Nummernblock ein, wenn er beim Start von NVDA ausgeschaltet war.
Wenn Sie sich für die zweite oder dritte Option entscheiden, wird der Nummernblock beim Beenden von NVDA in den Zustand zurückgesetzt, in dem er vorher war. Wenn Sie z. B. "Nummernblock ausschalten" auswählen und der Nummernblock beim Start von NVDA eingeschaltet war, wird er während der Benutzung von NVDA ausgeschaltet, aber beim Beenden von NVDA wieder eingeschaltet.

#### Erweiterte Anwendungsfälle

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

### Neue Features

I encourage you to post an [issue][3], or email with any feature
suggestions, or other use cases that I haven't listed here, or just to let
me know you find the add-on useful! But as mentioned above, if you do find
it useful, please leave a [review][4].

### Verlauf

This add-on was the direct result of requests I've heard from users over the
years, and a GitHub discussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). With thanks to
@Qchristensen and @feerrenrut.  The basic implementation of the numlock
features was borrowed from the legacy NumLock Manager add-on, by Noelia Ruiz
(@nvdaes on GitHub), and others. Used with permission.

### Änderungsprotokoll

(Dieses Änderungsprotokoll ist unvollständig. Siehe im Protokoll mit Git für
vollständige Details.)

* 24.1.0: NVDA 2024.X compatibility.
* 23.1.0: Zusätzliche Funktionen zur Verwaltung des Nummernblocks. Bessere
  Protokollierung. Verbesserte Handhabung von Konfigurationsprofilen (WIP).
* 23.0: Kompabilität ab NVDA 2023.1

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode [2]:
https://nvaccess.org/ [3]:
https://github.com/opensourcesys/numpadNavMode/issues/new [4]:
https://github.com/nvaccess/addon-datastore/discussions/2630
