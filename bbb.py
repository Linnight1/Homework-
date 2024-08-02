from threading import Thread
import queue
import time


class Table:

    def __init__(self, number):
        self.number = number
        self.is_busy = True


class Cafe:
    queue = queue.Queue()

    def __init__(self, tables):

        self.tables = tables

    def customer_arrival(self):

        for i in range(1, 21):
            time.sleep(1)
            print(f"Посетитель № {i} прибыл")

            self.serve_customer(i)

    def serve_customer(self, customer):
        self.customer = customer
        threads = []

        for t in self.tables:
            if t.is_busy == True:
                if Cafe.queue.empty() == True:
                    th = Customer(self.customer, t)

                    th.start()

                    break
                if Cafe.queue.empty() == False:
                    print(f"{self.customer} ожидает свободный стол")
                    Cafe.queue.put(self.customer)
                    th = Customer(Cafe.queue.get(), t)
                    th.start()

                    break

        if t.is_busy == False:
            print(f"Посетитель {self.customer} ожидает свободный стол")
            Cafe.queue.put(self.customer)





class Customer(Thread):
    def __init__(self, num_customer, num_table):
        super().__init__()
        self.num_customer = num_customer
        self.num_table = num_table

    def run(self):
        print(f"Посетитель № {self.num_customer} занял стол номер {self.num_table.number}")
        self.num_table.is_busy = False
        time.sleep(5)

        print(f"Посетитель № {self.num_customer} покушал и ушел")
        self.num_table.is_busy = True



table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()






