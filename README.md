# Generator_LoremIpsum

## Spuštění/Stáhnutí
Možnosti jak spustit LoremIpsum generator:
1. Založte si novou složku, následně složku otevřete. Po otevření si spusťe nový terminal. Následne do terminalu napište git clobe <URL repitory>
2. Stáhněte si soubor Impsumgenerator, vyberte složku a otevřete.
3. Zkopírujte kod, otevřete VS code a do jakékoliv složky.py vložte zkopírovaný kod.
## Funkčnost
Proto, aby jste mohli spustit LoremIpsum generator budete potřebovat pouze terminal. Pokud máte již jeden otevřený použíte jej, pokud ne vytvořte si nový. Jakmile máte úkon splěný, stačí kliknou na "Run Python File" a program se spustí.
## Postup
Jako první jsem si vytvořil 3 seznamy, tyto seznamy obsaují slabiky a samostatná písmena. Dále jsem si importoval knihovnu random. Pomocí cyklu while True jsem udělal nekonečný cyklus který provádí, že prvně vybere random slabiku nebo písmeno ze seznamu, to mi vytvoří proměnou, do které se sečtou dané slabiky. Následně tyto slabiky smaže z listu aby se neopakovaly a nově vytvořené slovo přidá do listu, který byl ze zaačátku prázdný. Celý cyklus se zastaví, jakmile je jeden seznam slabik prázdný. Tento proces se opakuje ještě 2x. Vzniká tak jeden seznam slov z náhodně vybraných slabik. Tento seznam se každým spuštením vždy změní.
Dalši věc co byla potřeba ošetřit bylo, aby se mi generovali random věty s random počtem slov. Dále jsem uvažoval, aby jsi uživatel mohl zadat kolik chce celkem bloků vygenerovat a kolik chce v jednom bloku vět. Využil jsem proto nově naučenou funkci nested loop (vnořený cyklus). Jako prvně jsem si určil random počet slov ve větě pomocí funkce randint. Následně jsem vytvořil vnořený cyklus - první cyklus mi určuje kolik chce uživatel bloků, další pak určuje kolik vět chce v jednom cyklu. následně jsem vytvořil proměnou "veta". Pomocí funkce sample jsem vytvořil aby se v seznamu slova promíchala, funkce k pak značí random počet slov ve větě. Celej příkaz jsem ukončil tak že jsem přidal funkci join, ta mi udělala, že se mezi slovy vytvoří mezera a navíc jsem učinil, že se "veta" chová jako string. Následně jsem použil funkci capitalize, ta mi způsobila, že každá nová věta začne velkým písmenem tu jsem uložil do proměnné "text". Následně jsem text printnul a za něj dal tečku, aby každá věta tečkou skončila. Pro větší přehlednost jsem nakonec přidal lajnu z pomlček.
