---
title: "Jason Scott's favorite 100"
subject: "Mini-Project in the ABC of Computational Text Analysis"
lang: de-CH
date: 14. Mai 2021
author:
  - name: Josias Bruderer
    affiliation:  Universität Luzern
---

\input{latex/header.tex}

# Einleitung

In den frühen Jahren des Internets war der Informationsaustausch und die Kommunikation nicht gleich einfach gestaltet wie heute. Trotzdem wurde in der Vernetzung ein grosses Potential erkannt und techno-utopische Communities entstanden. Ein Mittel zum Austausch waren Bulletin Board Systeme (BBS), Server auf denen jede und jeder, mit Zugriff zu einem am Telefonnetz angeschlossenen Computer, Texte hoch- und herunterladen konnten.[^1] Jason Scott[^2] unterhält ein Archiv mit einem Umfang von 58'000 solcher Text-Dateien.

Als Vorbereitung für die Hauptseminararbeit[^3], in welcher dieses Archiv zur Beantwortung der Frage nach dem Einfluss der BBS auf die 1996 formulierte «Declaration of the Independence of Cyberspace»[^4] dienen soll, wird in diesem Mini-Project[^5] der verkleinerte Datensatz «favorite 100» untersucht. Konkret soll geprüft werden, ob inhaltliche Auffälligkeiten bestehen, die möglicherweise Rückschlüsse auf Scotts Interessen und seine Biografie zulassen. Dieses Mini-Project soll ebenfalls zur Einschätzung dienen, wie aufwändig die Bereinigung des gesammten Textkorpuses ($N=58'0000$ Dateien) sein wird.

# Methode

Im ersten Schritt solle die Dateien manuell untersucht und dabei Auffälligkeiten festgehalten werden. Diese Auffälligkeiten betreffen Länge, Struktur und Inhalt. (Die Längen werden mittels Python ermittelt.)


# Datensatz

#WIP

* Variation von Spaltenbreite berechnen zur Beurteilung ob Textfile Inhalt «nützlich» ist resp. Text enthält
* Zeichenvariation prüfen: 
    * fast ausschliesslich Sonderzeichen ≃ ASCII Art
    * viele Sonderzeichen ≃ Aufwändig formatiert
    * wenige Sonderzeichen ≃ Fliesstext
* Auffällig: z.T. steht «Read X times» → die Zahlen sind relativ niedrig (i.d.R. <100)
* Ungültige Zeichen kommen häufig vor → z.B. «» → diese müssen gefiltert werden
* textfiles.com führt nebst den Dateien auch eine Beschreibung und Kategorisierung auf. Diese kann für die Analyse nützlich sein.
* Messages usually contain: From: ; Subject: ; Date: ; Organization: 
* Datum: «1991», «1/8/86», «02/25/88», «Copyright 1993 by», careful with telnr «(609)/921-1994», «(n)o copyright!, 1985», «8-25-86», «17 March 1981 13:59 est», «updated 2-12-92», «Date: 1 Mar 89 11:30:05 GMT», «August 2nd 1985», «b-file#1 nov.
1984», «(c) 1984-85 NPI/Appa Teleworks I», «Published       June, 1971»
* remove index.html (and other html files?)
* Gunk in textfiles to take care of, Ex.: _(replacing U for You, 0 for O, Z for S, and similar gunk)_
 
Stichwörter: _Phone Phreaking_

* Der Datensatz ist aufrufbar unter: [http://textfiles.com/100/](http://textfiles.com/100/) 
* Der Datensatz kann heruntergeladen werden unter: [http://archives.textfiles.com/100.zip](http://archives.textfiles.com/100.zip)



# Resultate



# Diskussion



# Fazit


[^1]: Die Funktionen solcher BBS waren weitreichender. Für die in dieser Arbeit geplante Untersuchung stellt diese Funktion allerdings die wichtigste dar.
[^2]: Amerikanischer Archivar, Historiker und Betreiber von textfiles.com sowie Mitwirkender bei archive.org.
[^3]: Link zum Exposé: [https://ipfs.chixodo.xyz/ipfs/QmcU2XbwmzD7hhRxhMaQPgiCtAhWajfAwbaCREEzscHFPE](https://ipfs.chixodo.xyz/ipfs/QmcU2XbwmzD7hhRxhMaQPgiCtAhWajfAwbaCREEzscHFPE)
[^4]: Verfasst von der Electronic Frontier Foundation (EFF)
[^5]: Der Sourcecode ist verfügbar unter: [https://git.makersphere.io/josias/ch.josias.jason-scotts-favorite-100](https://git.makersphere.io/josias/ch.josias.jason-scotts-favorite-100)