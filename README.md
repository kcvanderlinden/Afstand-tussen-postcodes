# Afstand tussen postcodes
Het berekenen van de afstand (hemelsbreed) tussen twee postcodes (1234 AB formaat). Hiervoor wordt allereerst een postcode omgezet naar een coördinaat en op basis van twee coördinaten wordt de afstand berekend.

## Hoe gebruiken?
Eén Python-package is van belang: <code>pip install pandas</code>

1. Plaats de gezipte map en het Python bestand in de folder waarin je het gaat gebruiken. 
2. Pak de gezipte folder uit in deze map zodat je in je werkmap een folder hebt met de naam <code>POSTCODE COORDINATEN DATASETS</code> met daarin twee bestanden: <code>NL.txt NL_full.txt</code>.
3. Importeer de functie vanuit <code>distance_calc_by_postals.py</code> in je eigen script door <code>from distance_calc_by_postals import distance_between_postals</code> 
4. Roep de functie aan door <code>distance_between_postals(postcode_1, postcode_2)</code>
5. Resultaat is de afstand tussen beide postcodes hemelsbreed als een Float.
