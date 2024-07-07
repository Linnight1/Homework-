# Использование %
team1_name = "Волшебники данных"
team2_name = "Мастера кода"
team1_num = 5
print("В команде %s участников:%s" % (team1_name,team1_num))
team2_num = 6
print("Итого сегодня в командах участников:%s и %s!" % (team1_num,team2_num))

#Использование format():

score_2 = 42
print("Команда {} решили задач: {}!".format(team1_name,score_2))
team1_time = 18015.2
print("{} решили задачи за {} c!".format(team1_name,team1_time))

# Использование f-строк:

score_1 = 40
print(f"Команды решили {score_1} и {score_2} задач")

if score_1 > score_2:
    challenge_result = "Победа команды: "
    print(f"{challenge_result}{team1_name}")
if score_1 < score_2:
    challenge_result = "Победа команды: "
    print(f"{challenge_result}{team2_name}")
else:
    challenge_result = "Победила дружба!"
    print(challenge_result)


tasks_total = 82
time_avg = 350.4
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!")
