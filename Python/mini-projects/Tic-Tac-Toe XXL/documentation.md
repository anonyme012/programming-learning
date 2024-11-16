# Tic-Tac-Toe XXL Documentation

A GUI interface to play Tic-Tac-Toe but on a bigger grid, against a player near to you, online or against the computer.

## Summary
- [Use Guide](#use-guide)
- [Features](#features)
- [Technologic Stack](#technologic-stack)
- [Prerequisites](#prerequisites)
- [Troubleshooting](#troubleshooting)
- [Game Rules](#game-rules)
- [Improvements](#improvements)
- [Interface](#interface)
- [About](#about)
- [Licence](#licence)

## Use guide
1. Launch the script by running in your terminal / command-line : 
```
python3 path/to/tic_tac_toe_xxl.py
```
2. To start a game, select the grid size, the adversary type, if you want a timer and other fields if they appears.
3. Click on "Start".
4. To play, when it's your turn, you simply had to click on the box you want and your shape will appears.
5. If you want to stop the game, by saving or not, simply click on "Quit" and choose "Save" or "Do not save".
5. When the game is finished, the result will appears and it will purposes you to download the game transcript.

## Features
- 3 game modes : 
    - Against a local player
    - Against an online player
    - Aigainst the computer with 5 difficulty levels : 
        - Very Easy
        - Easy
        - Medium
        - Hard
        - Expert
- Configurable grid size from 3 x 3 to 30 x 30
- Configurable points for line length
- Configurable game mode : 
    - 1 point match
    - Contest with points counter
- Editables players names with text and police.
- Configurable IP of online player
- Simple tutorial
- Light / Dark mode
- Coloured Interface
- Game saving and loading functionnality with file
- Optional time limit for each turn

## Technologic Stack
- Python 3
- `socket` library
- Tkinter
- ...

## Prerequisites

To execute this script you need : 
- A computer with Windows, MacOS or Linux
- Python 3 or newer (normally preinstalled with your OS) : [Install Link](https://www.python.org/downloads/)
- The `tkinter` Python package. To install it : 

**Windows :**
```
...
```
**MacOS :**
```
...
```
**Linux :**
```
...
```
- ...
- If you want to play online : a stable internet connection

## Troubleshooting
The program may not working. If it's your case, try this solutions : 
- Check if you saatisfy the [Requirements](#prerequisites).
- Check if the Python script isn't blocked by your antivirus
- Reinstall Python

If you are using the online game mode, try that solutions : 
- Check your internet connection
- Check if your firewall has not blocked the Internet connection
- Check the IP of your adversary

If the issue remains unresolved, please file a bug report.

## Game Rules
Before starting, players select the grid size and the number of symbols in a row required to win. Standard modes might include a 3x3 grid with three symbols in a row to win, a 5x5 grid needing four in a row, and a 10x10 grid needing five. A "Custom Mode" allows players to pick any grid size and winning line length.

The game is turn-based, with players taking turns to place their symbol (X or O) in any empty cell on the grid. An optional Timed Mode gives players a time limit per move, adding to the challenge. 

Players earn points by completing a line of the defined length. They can choose to award more points for longer line lengths.
For example : for a 15x15 grid, you can decide to award 1 point if the line measures 5 shapes, but 2 if it measures 6.
Warning : If your line has already been counted, you will not be able to earn points by enlarging the same line.

The game ends when the grid is filled and then we count the points. The winner is who have he more points. In case of ex-aequo, there is no winner, resulting in a draw.

## Improvements
- Animations of : 
    - Winning and losing
    - Shape placement
- Add a *Champion* difficulty level with a real AI tthat learns of its games.

## Interface
...

## About
I created this software in my spare time as part of my self-taught learning of the Python programming language.
I used the `socket`, `...` modules and Python 3.13 (latest version at the time of writing).
Once my skills in this area are broader, I would like to add some features as described in [# Improvements](#improvements).

## Licence

MIT License

Copyright (c) [2024] [Nil / anonyme012 (https://github.com/anonyme012)]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.