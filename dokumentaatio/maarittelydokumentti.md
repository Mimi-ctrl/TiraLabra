# Määrittelydokumentti

Opinto-ohjelma: Tietojenkäsittelytieteen kandidaatti

Projektin ohjelmointikieli: Python

Muut ohjelmointikielet: Java

Dokumentaation kieli: Suomi

Muuta: Vertaisarviointi englanniksi onnistuu myös.

Aihe: Connect Four peli, jossa on kaksi pelaajaa. Pelaajat pelaavat 7x6 kokoisella laudalla. Pelin tavoitteena on yhdistää ennen toista pelaajaa neljä oman värin nappulaa.

Toteutus: Teen pelin toimimaan ensin tekstigrafiikkaa käyttävässä käyttöliittymässä ja pyrin myös mahdollisuuksien mukaan muokkaamaan sen graafiseen käyttöliittymään, jos aikataulu sallii.

Algoritmit ja tietorakenteet: MiniMax algoritmi Alfa-Beta-karsinnalla. MiniMaxia tulen käyttämään tekoälyn siirtojen valitsemiseen. MiniMaxin avulla saadaan valitua parhain siirto. Tietorakenteena tulen käyttämään matriisia jossa pidän kirjaa siirroista.

Aika ja tila vaativuus: Minimax-algoritmin aikavaativuus on O(b^d), missä "b" on puun haarojen määrä solmussa ja "d" on puun syvyys eli käsiteltävien pelitilanteiden maksimimäärä. Aikavaativuus kasvaa eksponentiaalisesti syvyyden suhteen.

