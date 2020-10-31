---
title: "Stopwatch Game Challenge"
author: MrJohnsonComputing
keywords:
  - 
  - 
  - 
  - 
  - 
  - 
id: 20201031170138
tags: #python
...
# Stopwatch Game Challenge
The program chooses a random amount of seconds between 5 and 20. The player has to press start, wait for that amount of seconds, and then press stop. The program takes the difference between how long the player took and how long it should have been and adds it to their score.

For example, if the player was told to wait for 10 seconds, but only waited for 8, they would have a score of 2. 
If the player waited for 12 instead of 8, they would still have a score of 2, as they were still 2 away from 10.

There should be 5 rounds, each round a new random number between 5 and 20 is picked. 

The player ia told their total at the end.

The smaller the score the better.

## Extension
### 1
While the program is running, keep track of the player's name and their highscores. At the end of each game, print out the top 5 highscorea.
### 2
Write the highscores to a file, so they are not lost when the game is closed. You should eb reading fron this file aswell in order to display the highscores.