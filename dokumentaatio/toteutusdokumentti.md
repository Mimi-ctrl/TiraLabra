# Toteutusdokumentti
## Ohjelman yleisrakenne
```mermaid
graph TD;
    MENU-->EXIT;
    MENU-->MODE;
    MODE-->AI;
    MODE-->PLAYER_2;
    AI-->WINNER;
    PLAYER_2-->WINNER;
```
```mermaid
sequenceDiagram
    participant User
    participant Menu
    participant Game
    participant Ai

    User ->> Menu: print_menu()
    Menu -->> User: Selection

    User ->> Menu: game_mode()
    Menu -->> User: Mode

    User ->> Game: game_loop() [mode = 2]
    Game ->> Game: Run game loop

    User ->> Ai: game_loop() [mode = 1]
    Ai ->> Ai: Run AI game loop
```

## Saavutetut aika- ja tilavaativuudet
Lisään kun valmis.
## Puutteita ja parannusehdotuksia
* Pelin toteutus pygamella.
* Mahdollisuus aloittaa uusipeli pelin päätyttyä.
* Mahdollisuus poistua pelistä muulloinkin kuin valikossa.
* Ai:n tehostaminen.
## Lähteitä
* https://tiralabra.github.io/2023_loppukesa/
* https://en.wikipedia.org/wiki/Connect_Four
* https://en.wikipedia.org/wiki/Minimax
