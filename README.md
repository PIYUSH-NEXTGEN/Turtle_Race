# 🐢 Turtle Race Game 

A multi-round turtle racing game built using Python's turtle module.


### Gameplay  -
Multiple turtles race from left to right.
Randomized movement creates unpredictable outcomes
User places a bet before each race

*Scoreboard System* - 
Tracks round number.
Maintains leaderboard (wins per turtle).
Updates dynamically after each race.

*Leader Tracking* - 
Displays current leading turtle during the race
Detects ties in real time

*Winner Animation* - 
Winning turtle performs a spin animation.
Visual feedback improves engagement.
Turtles reset after each round.

## Tech Stack - 
| Component      | Technology                     |
|---------------|-------------------------------|
| Language      | Python                        |
| Graphics      | Turtle Graphics (`turtle`)    |
| Randomization | `random` module               |
| Animation     | `time` module                 |

## How the Game Works -
The game initializes:
Screen.
Scoreboard.
Leader display.
User is prompted to bet on a turtle name.

Race begins:
Each turtle moves forward by a random distance.
Leader is updated dynamically.

Race ends when:
A turtle crosses the finish line.

System updates:
Winner is announced
Scoreboard is updated
Winner animation plays
Game loops to next round

