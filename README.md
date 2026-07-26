# Jungle Adventure Game

A text-based adventure game developed in **Python** as the **Level 2 Graduation Project** for the **Digital Egypt Cubs Initiative (DECI) 2025**. Players explore a dangerous jungle, survive random encounters, and search for hidden treasures across five progressively challenging levels.

## Gameplay

The objective is to survive the jungle by completing all five levels.

At each level, the player can explore one of three locations:

* House
* Cave
* Forest


One location contains a hidden treasure, while the others may lead to dangerous enemy encounters. Finding the treasure allows the player to advance to the next level.

## Enemies

During the adventure, players may encounter random enemies, including:

* Gorilla
* Giant Snake
* Jungle Bandit
* Massive Spider
* Swarm of Wasps

For each encounter, the player chooses to:

* **Fight** – Success depends on probability, which decreases as the levels progress.
* **Run** – Avoid combat, but with a chance of falling into a trap.

## Health System

* The player starts with **100 health**.
* Winning or escaping an encounter may reward a small amount of health by finding berries.
* Losing an encounter ends the game.

## Features

* Five progressively challenging levels
* Random treasure locations
* Random enemy encounters
* Random treasure values
* Health recovery system
* Difficulty scaling across levels
* Input validation for user choices
* Replay option after the game ends
* Modular implementation using reusable Python functions

## Technologies Used

* Python 3
* `random`
* `time`

## Programming Concepts

This project demonstrates the use of:

* Functions
* Loops
* Conditional statements
* Lists
* Randomization
* User input validation
* Game loops
* State management
* Return values
* Modular programming

## How to Run

1. Clone this repository.
  ```bash
   git clone https://github.com/nadagazzar/adventure_game.git
```
```bash
   cd adventure_game
```
2. Ensure Python 3 is installed.
3. Run the program:

```bash
python adventure_game.py
```

## Winning the Game

Complete all five levels by finding the treasure at each level while surviving enemy encounters. After the game ends, players have the option to start a new adventure.

