from threading import Thread
import queue
import time


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Cafe:


    def __init__(self, tables):
        self.queue = queue.Queue()

        self.tables = tables

    def customer_arrival(self):

        for i in range(1, 21):
            print(f"Посетитель № {i} прибыл")
            self.serve_customer(i)
            time.sleep(1)




    def serve_customer(self, customer):
        self.customer = customer
        threads = []

        for t in self.tables:
            if t.is_busy == True:
                t.is_busy = False
                th = Customer(self.customer, self.queue, t)
                th.start()

                threads.append(th)
                break
        else:
            print(f"Посетитель {self.customer} ожидает свободный стол")
            self.queue.put(self.customer)



class Customer(Thread):
    def __init__(self, num_customer, queue, num_table):
        super().__init__()
        self.num_customer = num_customer
        self.num_table = num_table
        self.queue = queue

    def run(self):
        if self.queue.empty:
            print(f"Посетитель № {self.num_customer} занял стол номер {self.num_table.number}")
            time.sleep(5)
            print(f"Посетитель № {self.num_customer} покушал и ушел")
            self.num_table.is_busy = True
        if self.queue.empty == False:
            Cafe.serve_customer(self.queue.get())
            self.queue.put(self.num_customer)



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()






