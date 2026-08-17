# PO_test

Et lille demo-projekt i Python, der viser hvordan man læser et produktkatalog
fra en CSV-fil og laver en simpel analyse — udelukkende med Pythons
standardbibliotek. Ingen pandas, ingen eksterne afhængigheder.

## Indhold

| Fil | Beskrivelse |
| --- | --- |
| `data/produkter.csv` | Datasæt med 10 fiktive produkter |
| `analyse.py` | Læser CSV'en og printer antal produkter og gennemsnitspris pr. kategori |
| `hej.py` | Minimalt "hello world"-script |

## Datasættet

`data/produkter.csv` er en kommasepareret fil med en header-linje og 10 rækker.

| Kolonne | Type | Beskrivelse | Eksempel |
| --- | --- | --- | --- |
| `sku` | tekst | Unikt varenummer | `SKU-1001` |
| `navn` | tekst | Produktets navn | `Trådløs mus` |
| `kategori` | tekst | Produktkategori (Elektronik, Køkken, Kontor, Fritid) | `Elektronik` |
| `pris` | decimaltal | Stykpris i DKK | `199.95` |
| `lager` | heltal | Antal enheder på lager | `42` |

Filen er gemt i UTF-8 og bruger punktum som decimalseparator.

## Krav

- Python 3.8 eller nyere (ingen pakkeinstallation nødvendig)

## Sådan kører du analysen

Stå i projektets rodmappe og kør:

```bash
python3 analyse.py
```

På Windows:

```bash
python analyse.py
```

Eksempel på output:

```
Produktanalyse (10 produkter)

Kategori         Antal      Gns. pris
-------------------------------------
Elektronik           3      466.15 kr
Fritid               1      599.00 kr
Kontor               3      172.82 kr
Køkken               3      162.65 kr
-------------------------------------
I alt               10      300.39 kr
```

Scriptet finder datafilen relativt til `analyse.py`, så det virker også hvis du
kalder det med en fuld sti, fx `python3 /sti/til/PO_test/analyse.py`.

## hej.py

```bash
python3 hej.py
```

Output:

```
Hej fra PO_test
```
