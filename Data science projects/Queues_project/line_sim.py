import time
from Queues import *

def one_line(my_queue):
    ticks = 0
    customer_number = int(input("how many cutomers do you want?")) - 1
    customer = 0
    my_queue.enqueue(customer)
    customer += 1
    while my_queue.size() > 0:
        time.sleep(0.01)
        ticks += 1
        if my_queue.size() > 0 and ticks % 5 == 0 and customer <= customer_number:
            my_queue.enqueue(customer)
            customer += 1
            print("a new person joined the line")
        if my_queue.size() > 0 and ticks % 12 == 0:
            output_number = my_queue.look()
            my_queue.dequeue()
            print("cashier one checked out customer #", output_number)
        if my_queue.size() > 0 and ticks % 19 == 0:
            output_number = my_queue.look()
            my_queue.dequeue()
            print("cashier two checked out customer #", output_number)
        if my_queue.size() > 0 and ticks % 25 == 0:
            output_number = my_queue.look()
            my_queue.dequeue()
            print("cashier three checked out customer #", output_number)

    print(ticks)

#unfortunately, I didn't get to the 2 lines part