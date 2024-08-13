def custom_write(file_name, strings):
    file_name = open(file_name,'a',encoding='utf-8')
    strings_positions = dict()
    strings_number = 1
    for i in strings:
        strings_positions_keys = tuple()
        begin_string = file_name.tell()
        file_name.write(i)
        strings_positions_keys = (strings_number,begin_string)
        file_name.write('\n')
        strings_positions[strings_positions_keys] = i
        strings_number += 1
    file_name.close()
    return strings_positions








info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)