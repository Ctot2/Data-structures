from Queues import *

def game_loop():
    f = open("challengeOnly.txt", "r")
    f_list = f.readlines()
    f_queue = Queue()
    for i in f_list:
        f_queue.enqueue(i)

    while True:
        x = input("choose one: 1. input match 2. print standings 3. exit")
        if x == "3":
            break
        elif x == "1":
            x = f_queue.dequeue().split()
            print("red alliance: ", x[0:3])
            print("blue alliance: ", x[3:6])
            rtr = int(input("input the red team's ranking points: "))
            btr = int(input("input the blue team's ranking points: "))

game_loop()