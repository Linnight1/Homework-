import datetime
import multiprocessing
def read_info(name):
    all_data = []
    name = open(file,"r")
    all_data.append(name.readlines())

filenames = [f'./file {number}.txt' for number in range(1, 5)]
start = datetime.datetime.now()
for file in filenames:
    read_info(file)
end = datetime.datetime.now()
time = end - start
print(f" Линейный: {time}")

if __name__ == "__main__":
    start2 = datetime.datetime.now()
    with multiprocessing.Pool(processes = 4) as pool:

        pool.map(read_info, filenames)
    end2 = datetime.datetime.now()
    time2 = end2 - start2

    print(f" Многопроцессорный: {time2}")



