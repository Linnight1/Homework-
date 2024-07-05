def custom_write(file_name, strings):
    file = open(file_name, "a",encoding = "utf-8")
    result_dict = {}
    count = 0
    for i in strings:
        a = file.tell()
        file.write(i + "\n")
        count += 1
        result_dict[count,a] = i
    file.close()
    return result_dict
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('Strings.txt', info)
for elem in result.items():
  print(elem)



