# ModelManager

This is a cross service memory manager for my bots. This ensures bots don't run gpu intensive tasks at the same time and crash eachother. It also provides other helpful functions.

## main.py

This main script runs each of the bots and restarts them on fatal crashes. Fatal crashes are unexpected worst case scenarios, but must be handled somehow. To define paths of bots to start, make a file called "bots.txt" that has the name of the bot and the path of the bot, seperated with "|". At the path, the bot should have a venv and a main.py file.

## vram-helper

This directory contains "vram.py", a file with methods that help manage vram allocation.