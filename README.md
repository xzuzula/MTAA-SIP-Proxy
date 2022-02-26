# Zadanie 1 – SIP Proxy \(telefónna ústredňa\)
Na vašom počítači \(alebo virtuálnom počítači\) sprevádzkujte SIP Proxy,
ktorá umožní prepájanie a realizáciu hovorov medzi štandardnými SIP klientami.

## Implementácia:
Pre implementáciu zadania 1 som sa rozhodol využiť programovací jazyk Python.
Konkrétne sa jedná o verziu `2.7.18`, keďže knižnica ktorú som použil pri implementácií tohto zadania je kompatibilná práve s verziou `2.x`.
Knižnica ktorá implementuje SIP Proxy má názov [SIP Full Proxy][1] od autora [Philippe THIRION][2].
Ďalšie vstavané knižnice ktoré som použil sú: `socket` a `SocketServer`.
Knižnica `socket` slúži na získanie lokálnej IP adresy počítača.
A knižnica `SocketServer` slúži na vytvorenie UDP servera.

## Funkcionalita:
- [x] Základná funkcionalita
- [x] Možnosť zrealizovať konferenčný hovor \(aspoň 3 účastníci\)
- [x] Možnosť presmerovať hovor
- [x] Možnosť realizovať videohovor
- [x] Logovanie / denníka hovorov – kto kedy komu volal, kedy bol ktorý hovor prijatý, kedy bol ktorý hovor ukončený, do ľubovoľného textového súboru v ľubovoľnom formáte
- [x] Úprava SIP stavových kódov z zdrojovom kóde proxy, napr. `486 Busy Here` zmeníte na `486 Obsadene`

## Použitie:
Samotná SIP Proxy sa spúšťa v Pythone `2.x` súborom `main.py`.
Program sa spýta na IP adresu `HOST` a na `PORT` SIP Proxy servera.
Ak chceme pokračovať so základnými nastaveniami tak nám stačí zadať `ENTER` a pokračovať.
Následne sa nám vypíše správa, že server bol spustený na konkrétnej IP adrese a konkrétom porte.
Program ukončíme zastavením procesu.

## Autor:
- Radovan Zuzula

[1]: https://github.com/tirfil/PySipFullProxy
[2]: https://github.com/tirfil
