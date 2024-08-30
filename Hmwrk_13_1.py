import time
import asyncio

async def start_strongman(name, power):
    print(f"Силач {name} начал соревнования")
    # k =
    for i in range(1,5):
        await asyncio.sleep(6 - power)
        print(f"Силач {name} поднял шар номер {i}")
    print(f"Силач {name} закончил соревнования")

async def start_tournament():
    task_1 = asyncio.create_task(start_strongman("Павел", 5))
    task_2 = asyncio.create_task(start_strongman("Илья", 3))
    task_3 = asyncio.create_task(start_strongman("Егор", 2))
    await task_1
    await task_2
    await task_3


asyncio.run(start_tournament())