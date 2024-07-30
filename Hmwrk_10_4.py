from threading import Thread
import queue
import time

class Table:
    is_busy = True
    def __init__(self,number):
        self.number = number

    def get_num(self):
        return self.number


class Cafe:
    queue = queue.Queue()
    def __init__(self,tables):
        self.tables = tables


    def customer_arrival(self):
        threads = []
        for i in range(1,21):
            time.sleep(1)
            th = Thread(target=Cafe.serve_customer, args = (self, i))
            print(f"Посетитель № {i} прибыл")
            th.start()
            threads.append(th)
        for thread in threads:
            thread.join()


    def serve_customer(self, customer):
        threads2 = []
        self.customer = customer
        Cafe.queue.put(self.customer)
        for t in self.tables:
            if t.is_busy == True:
                num_table = Table.get_num(t)
                th2 = Customer(Cafe.queue.get(),num_table)
                t.is_busy = False
                th2.start()




                threads2.append(th2)

        for thread in threads2:
            thread.join()
            t.is_busy = True


        if t.is_busy == False:
            print(f"Посетитель {self.customer} ожидает свободный стол")





class Customer(Thread):
    def __init__(self,num_thread,num_table):
        super().__init__()
        self.num_thread = num_thread
        self.num_table = num_table

    def run(self):
        print(f"Посетитель № {self.num_thread} сел за стол № {self.num_table}")
        time.sleep(5)
        print(f"посетитель № {self.num_thread} покушал и ушел (Стол № {self.num_table} свободен)")


table1 = Table(1)
table2 = Table(2)
table3 = Table(3)
tables = [table1, table2, table3]
cafe = Cafe(tables)
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()
customer_arrival_thread.join()
