symbols = '@№$%^&*()'
name_file = input('Название файла: ')
if name_file[0] in symbols:
    print('Ошибка: название начинается на один из специальных символов')
if name_file.encode() != '.txt' or name_file.encode() != '.docx':
    print('Ошибка: неверное расширение файла. Ожидалось .txt или .docx')
