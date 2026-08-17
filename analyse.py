"""Simpel analyse af produktkataloget i data/produkter.csv.

Printer antal produkter pr. kategori samt gennemsnitsprisen — både pr.
kategori og for hele kataloget. Bruger kun standardbiblioteket.
"""

import csv
import sys
from collections import defaultdict
from pathlib import Path

CSV_STI = Path(__file__).parent / "data" / "produkter.csv"


def laes_produkter(sti):
    """Læser CSV'en og returnerer en liste af produkter med pris/lager som tal."""
    with open(sti, newline="", encoding="utf-8") as f:
        produkter = []
        for linjenr, raekke in enumerate(csv.DictReader(f), start=2):
            try:
                raekke["pris"] = float(raekke["pris"])
                raekke["lager"] = int(raekke["lager"])
            except (TypeError, ValueError) as fejl:
                raise ValueError(f"Ugyldig værdi i linje {linjenr}: {fejl}") from fejl
            produkter.append(raekke)
    return produkter


def opsummer_pr_kategori(produkter):
    """Returnerer {kategori: (antal, gennemsnitspris)} sorteret efter kategori."""
    priser = defaultdict(list)
    for produkt in produkter:
        priser[produkt["kategori"]].append(produkt["pris"])
    return {
        kategori: (len(p), sum(p) / len(p))
        for kategori, p in sorted(priser.items())
    }


def dansk_pris(vaerdi):
    """Formaterer et beløb med to decimaler og dansk decimalkomma."""
    return f"{vaerdi:.2f}".replace(".", ",")


def main():
    if not CSV_STI.exists():
        print(f"Fandt ikke datafilen: {CSV_STI}", file=sys.stderr)
        return 1

    produkter = laes_produkter(CSV_STI)
    if not produkter:
        print("Datafilen indeholder ingen produkter.", file=sys.stderr)
        return 1

    opsummering = opsummer_pr_kategori(produkter)

    print(f"Produktanalyse ({len(produkter)} produkter)\n")
    print(f"{'Kategori':<15}{'Antal':>7}{'Gns. pris':>15}")
    print("-" * 37)
    for kategori, (antal, gns) in opsummering.items():
        print(f"{kategori:<15}{antal:>7}{dansk_pris(gns):>12} kr")
    print("-" * 37)

    samlet_gns = sum(p["pris"] for p in produkter) / len(produkter)
    print(f"{'I alt':<15}{len(produkter):>7}{dansk_pris(samlet_gns):>12} kr")
    return 0


if __name__ == "__main__":
    sys.exit(main())
