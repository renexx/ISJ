# 1. úloha z predmetu skriptovacie jazyky implementácia je v jazyku python
## Zadanie


Dopište definici regulárního výrazu **inbetween** (místo ...), aby odpovídal pozicím, na něž se má ve jménech typu **camelCaseName** vložit **_** při převodu na **snake_case_name**.

Dopište definici regulárního **pat** (místo ...), aby odpovídal *buď jménu, před kterým je titul [Pp]rof. nebo [Dd]oc. a za ním následuje ", Ph.D.",* nebo **jinému případu.**
Oddělovačem je čárka, za kterou následuje alespoň jeden bílý znak.
pisoval chybu).

## Vysvetlenie

Zkusím ale vysvětlit řešení úkolu i touto formou:
1. Úloha - je potreba použit lookahead a lookbehind
2. Úloha - je potrebné použit "trik"  "The Greatest Regex Trick Ever" - http://www.rexegg.com/regex-best-trick.html
myšlienka tohto triku je taká, že ak sa chceme zbaviť špecifickej možnosti, tak ju preskočime a to pomocou konštrukcie NotThis|(GetThis) to čo chceme uzavrieme do zátvoriek buď pomocou group(1) alebo pomocou findall
Napríklad ak chceme nájsť všetky výskyty slova Tarzan okrem takej možnosti kde je "Tarzan" tak to bude "Tarzan"|(Tarzan)
