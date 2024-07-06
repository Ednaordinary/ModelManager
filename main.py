import subprocess
import threading
from vramhelper import vram

# This main script runs each of the bots and restarts them on fatal crashes. Fatal crashes are unexpected worst case scenarios, but must be handled somehow. To define paths of bots to start, make a file called "bots.txt" that has the name of the bot and the path of the bot, seperated with "|". At the path, the bot should have a venv and a main.py file.


bots = []
with open("bots.txt", "r") as bot_file:
    bots = [(x[:-1].split("|")[0].strip(), x[:-1].split("|")[1].strip()) for x in bot_file.readlines()]

print(bots)

def bot_thread(name, path):
    path = path[:-1] if path[-1] == "/" else path
    while True:
        process = subprocess.Popen("./venv/bin/python3 ./main.py", stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, cwd=path, universal_newlines=True)
        for line in iter(process.stdout.readline, b''):
            if line.strip() != "":
                with open("./logs/" + name + ".log", "a") as log_file:
                    log_file.write(line)
        exitcode = process.wait()
        print(name, "exited!")
        vram.deallocate(name)
        if exitcode != 0:
            with open("./logs/" + name, "a") as log_file:
                log_file.write("Warning! Process exited with code " + str(exitcode))
        else:
            with open("./logs/" + name, "a") as log_file:
                log_file.write("Process exited normally.")

bot_threads = []
for bot in bots:
    bot_threads.append(threading.Thread(target=bot_thread, args=[bot[0], bot[1]]))

for thread in bot_threads:
    thread.start()
for thread in bot_threads:
    thread.join()