# Käyttöohje

## Ohjelman suorittaminen
1. Lataa viimeisin release LINKKI TÄHÄN
2. Asenna riippuvuudet komennolla:
```
poetry install
```
3. Suorita ohjelma juurihakemistossa komennolla:
```
poetry run invoke start
```
## Syötteet
Peli kysyy käyttäjältä syötteitä. Halutuista syötteistä annetaan ohjeita. Jos syöte ei ole halutunlainen, ilmoitetaan siitä virheellä.

Kun ohjelma käynnistetään, tulee ensimmäisenä valikko, jossa käyttäjä voi valita joko uuden pelin tai poistumisen (exit).

![Kuvakaappaus - 2023-08-02 19-16-01](https://github.com/Mimi-ctrl/TiraLabra/assets/56686737/79042c76-5cdb-4955-abdd-21c97fabf62e)

Jos käyttäjä valitsee uuden pelin, ilmestyy seuraava valikko, jossa käyttäjä voi valita haluaako pelata tietokonetta vastaan vai kaksinpeliä.

![Kuvakaappaus - 2023-08-02 19-16-55](https://github.com/Mimi-ctrl/TiraLabra/assets/56686737/1b8a9620-de84-44de-bbc1-172a8e4e2eb2)

Peliä pelataan antamalla halutun sarakkeen numero, johon pelinappula halutaan asettaa.

![Kuvakaappaus - 2023-08-02 19-17-15](https://github.com/Mimi-ctrl/TiraLabra/assets/56686737/c8adc301-0d60-4464-aaf3-52aa00d76a17)

Peli loppuu, kun pelilauta on täynnä tai on saatu yhdistettyä neljä nappulaa peräkkäin. Tämän jälkeen ilmoitetaan mahdollinen voittaja, ja ohjelma päättyy.

![Kuvakaappaus - 2023-08-02 19-17-44](https://github.com/Mimi-ctrl/TiraLabra/assets/56686737/4ede6693-ecd6-4d83-b181-0b641418de65)

### Huom! 
Sovellusta testattu Python 3.10.12 versiolla.
