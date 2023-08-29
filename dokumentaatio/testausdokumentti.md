# Testausdokumentti

## Testin suorittaminen
GitHub Actions suorittaa testit automaattisesti. 

Unit testit pääsee suorittamaan juurihakmistossa komennoilla:
```
poetry shell
```
```
poetry run invoke test
```

Testikattavuusraportin saa komennoilla:
```
poetry shell
```
```
poetry run invoke coverage-report
```

## Yksikkötestauksen kattavuusraportti
![Kuvakaappaus - 2023-08-29 19-11-13](https://github.com/Mimi-ctrl/TiraLabra/assets/56686737/8808b1ae-3f48-4f16-9b8d-642e326882d0)

## Mitä testattu
Game luokan testit varmistavat, että metodit toimivat oikein. Nämä metodit tarkistavat kelvolliset sarakkeet, laskevat pelinappulat, tunnistavat täydet pelilaudat, havaitsevat voittotilanteet (mukaan lukien pystysuora, vaakasuora ja vinottainen), sekä käsittelevät virheelliset syötteet pelisilmukassa. Nämä testit varmistavat yhdessä pelilogiikan ja siihen liittyvien metodien tarkkuuden ja luotettavuuden.

Ai luokan testit varmistavat metodien oikean toiminnan, kuten alustuksen, siirtojen generoinnin, voittoon johtavien siirtojen tunnistamisen (vaakasuora, pystysuora, vinottainen), linjojen arvioinnin, parhaan siirron löytämisen minimaxin avulla, sekä varmistavat tekoälyn päätöksentekologiikan asianmukaisen toiminnan.

Main luokan testit varmistavat, että funktio toimii oikein valitun pelitilan ja siihen liittyvien pelisilmukoiden kanssa.

Menu luokan testit varmistavat, että funktiot käsittelevät oikein erilaisia syötteitä ja valintoja, sekä palauttavat odotetut tulokset valittujen vaihtoehtojen mukaisesti.
