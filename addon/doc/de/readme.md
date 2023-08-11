# Nummernblock-Navigationsmodus #

* Autor: Luke Davis (Open Source Systems, Ltd.)
* [Stabile Version herunterladen][1]

Dies ist eine [NVDA-Erweiterung](https://nvaccess.org/), mit dem Sie den
Nummernblock der Tastatur einfach zwischen der Navigationssteuerung von NVDA
und der Windows-Navigationssteuerung für Nicht-Screenreader umschalten
können. Dies kann besonders für Benutzer nützlich sein, die von JAWS auf
NVDA umsteigen. Mit dieser NVDA-Erweiterung können Sie auch die Umschaltung
der Taste des Nummernblocks genau steuern, sowohl beim Start von NVDA als
auch optional in einem Konfigurationsprofil.

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

Wenn Sie den Computer jedoch mit einem sehenden Benutzer teilen, der es
vorzieht, dass die Funktion des Nummernblocks immer eingeschaltet ist, Sie
sie aber ausschalten möchten, damit der Nummernblock mit NVDA funktioniert,
möchten Sie vielleicht, dass die Funktion des Nummernblocks beim Start von
NVDA automatisch ausgeschaltet wird. Oder Sie geben viele Daten ein und
möchten, dass der Nummernblock beim Start von NVDA immer eingeschaltet ist.

Gehen Sie in das NVDA-menü, Optionen, Einstellungen, Navigationsmodus des Nummernblocks, und verwenden Sie die Option "Status des Nummernblocks beim Start von NVDA oder beim Laden des Profils". Hier gibt es drei Optionen. Die erste, "Nicht ändern", ist die Standard-Einstellung, die den Nummernblock nicht verändert. Es bleibt in dem Zustand, in dem er sich vor dem Start von NVDA befand.
Die zweite Option, "Nummernblock ausschalten", schaltet den Nummernblock beim Start von NVDA immer aus. Die dritte Option, "Nummernblock einschalten", schaltet den Nummernblock ein, wenn er beim Start von NVDA ausgeschaltet war.
Wenn Sie sich für die zweite oder dritte Option entscheiden, wird der Nummernblock beim Beenden von NVDA in den Zustand zurückgesetzt, in dem er vorher war. Wenn Sie z. B. "Nummernblock ausschalten" auswählen und der Nummernblock beim Start von NVDA eingeschaltet war, wird er während der Benutzung von NVDA ausgeschaltet, aber beim Beenden von NVDA wieder eingeschaltet.

#### Erweiterte Anwendungsfälle

Wenn Sie die leistungsstarken NVDA-Konfigurationsprofile verwenden und
möchten, dass die Funktion des Nummernblocks automatisch aktiviert wird,
wenn Sie bestimmte Profile eingeben, gehen Sie wie folgt vor:

* Rufen Sie im "normalen Profil" die oben beschriebene Einstellung für den
  Navigationsmodus des Nummernblocks auf. Aktivieren Sie das
  Kontrollkästchen "Der anfängliche Numlock-Zustand ist abhängig vom
  Konfigurationsprofil". Diese Option ist standardmäßig nicht markiert.

* Klicken Sie auf die Schaltfläche "OK".

* Wechseln Sie zu dem Profil, in dem die Funktion des Nummernblocks immer
  aktiviert oder deaktiviert sein soll.

* Gehen Sie zurück in die Einstellungen für den Navigationsmodus des
  Nummernblocks und wählen Sie die Option Nummernblock aus- oder
  einschalten, je nach Wunsch.

* Klicken Sie dann auf die Schaltfläche "OK". Wenn Sie nun dieses Profil
  eingeben, wechselt der Nummernblock automatisch in den gewünschten
  Zustand.

Beachten Sie, dass dies eine neue Funktion ist, und es ist ungewiss, ob
jemand diese Funktion nutzt. Wenn Sie jemanden finden, schicken Sie mir
bitte eine E-Mail oder melden Sie [ein
Problem](https://github.com/opensourcesys/numpadNavMode/issues/new), um
mitzuteilen, wie Sie es nutzen.

### Neue Features

Ich ermutige Sie, eine
[Fehlerbericht](https://github.com/openSourceSys/numpadNavMode/issues/new)
zu posten oder mir eine E-Mail mit Vorschlägen zu Funktionen oder anderen
Anwendungsfällen zu schicken, die ich hier nicht aufgeführt habe, oder mich
einfach wissen zu lassen, dass Sie die NVDA-Erweiterung nützlich finden!

### Verlauf

Diese NVDA-Erweiterung war das direkte Ergebnis von Anfragen, die ich im
Laufe der Jahre von Benutzern erhalten habe, und einer GitHub-Diskussion in
[#9549](https://github.com/nvaccess/nvda/issues/9549). Mit Dank an
@Qchristensen und @feerrenrut. Die grundlegende Implementierung der
Nummernblock-Funktionen wurde von Noelia Ruiz (@nvdaes auf GitHub) und
anderen aus dem älteren Nummernblock-Managern übernommen. Mit Erlaubnis
verwendet.

### Änderungsprotokoll

(Dieses Änderungsprotokoll ist unvollständig. Siehe im Protokoll mit Git für
vollständige Details.)

* 23.0: Kompabilität ab NVDA 2023.1

* 23.1.0: Zusätzliche Funktionen zur Verwaltung des Nummernblocks. Bessere
  Protokollierung. Verbesserte Handhabung von Konfigurationsprofilen (WIP).

[[!tag dev stable]]

[1]: https://www.nvaccess.org/addonStore/legacy?file=numpadNavMode
