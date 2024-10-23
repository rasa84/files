# print("------------------1 uzd.---------------------")
#
# file = open('./some-text.txt')
# print(file.read())
#
# file.seek(0)
# print('New text :', file.read())
#
# print(file.closed)
# file.close()
# print(file.closed)
#
# with open('some-text.txt') as file:
#     line = file.readline()
#     print(f"Eilute: {line}")
#     text = file.read()
#     print(text)
#
#     print(file.closed)
# print(file.closed)
#
# with open('./some-text.txt') as file:
#     line = file.readline()
#     print(line)
#     line = file.readline()
#     print(line)
#     line = file.readline()
#     print(line)
#
# with open('./some-text.txt') as file:
#     text = file.readlines()
#     print(text)
#
# with open('./some-text.txt') as file:
#     text = file.readlines()
#     print('All text:', text)
#     # cleaned_text = [line[:-1] for line in text]
#     cleaned_text = [line.rstrip('\n') for line in text]
#     print('Cleaned text:', cleaned_text)
#
# with open('./some-text.txt') as file:
#     text = file.read().splitlines()
#     print(text)
#
# with open('./some-text.txt') as file:
#     print(type(file.read()))
#     file.seek(0)
#     print(type(file.readline()))
#     file.seek(0)
#     print(type(file.readlines()))
#
# lines = []
# with open('./some-text.txt') as file:
#     while True:
#         line = file.readline().rstrip('\n')
#         if not line:
#             break
#         print('Read line:', line)
#         lines.append(line)
#
# print(lines)
#
# lines = []
# with open('./some-text.txt') as file:
#     for line in file:
#         line = line.rstrip('\n')
#         print('Read line:', line)
#         lines.append(line)
#
#     print(lines)
#
# students = []
# with open('./another-text.txt', encoding="utf8") as file:
#     for line in file:
#         line = line.rstrip('\n')
#         split_lines = line.split(';')
#         student = dict(
#             vardas = split_lines[0],
#             pavarde = split_lines[1],
#             amzius = split_lines[2],
#             mokykla = split_lines[3],
#             vidurkis = split_lines[4]
#         )
#         students.append(student)
# print(students)

# print("------------------2 uzd.---------------------")
# with open('./write-text.txt', 'w') as file:
#     file.write('pirma\n')
#     file.write('antra\n')
#     file.write('trecia\n')
#     file.write('ketvirta\n')

# with open('./write-text.txt', 'w') as file:
#     file.write('haha' * 1000)

# file = open('./write-text.txt', 'w')
# file.write('pirma\n')
# file.write('antra\n')
# file.write('trecia')
#
# file.close()
#
# with open('./write-text.txt', 'w') as file:
#     file.write('ANKSCIAU PRIDETAS TEKSTAS\n')
# with open('./write-text.txt', 'w') as file:
#     file.write('labas krabas\n')
# with open('./write-text.txt', 'a') as file:
#     file.write('daugiau teksto\n')
#     file.write('failo papildymas')

# with open('./write-text.txt', 'w') as file:
#     file.write('labas krabas\n')
# with open('./write-text.txt', 'a') as file:
#     file.write('daugiau teksto\n')
#     file.write('failo papildymas')
# with open('./write-text.txt', 'r+') as file:
#     file.write('ar atsiras failo virsuje?\n')
#     file.write('ar atsiras failo virsuje?\n')

# with open('./write-text.txt', 'w') as file:
#     file.write('This is a first line in the text\n')
# with open('./write-text.txt', 'a') as file:
#     file.write('This is a second line in the text')
# with open('./write-text.txt', 'r+') as file:
#     file.write('<<It')
#     file.seek(21)
#     file.write('to ruin >>\n')
#     file.write('<<It')

# print("------------------3 uzd.---------------------")
# cars = []
# with open('./cars.txt') as file:
#     for line in file:
#         line = line.rstrip('\n')
#         split_lines = line.split(';')
#         car = dict(
#             model=split_lines[0],
#             mpg=split_lines[1],
#             cyl=split_lines[2],
#             disp=split_lines[3],
#             hp=split_lines[4]
#         )
#         cars.append(car)
# print(cars)
# with open('./cars.txt', 'a') as file:
#     disp_sum = 0
#     for c in cars:
#         disp_sum += int(c["disp"])
#         print(c["disp"])
#     print(disp_sum)
#     print(len(cars))
#     disp_average = disp_sum / len(cars)
#     file.write(f"Disp average: {disp_average}")

# **************************************************************************
# READERS AND DICTREADER

# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = reader(file) # as list
#     next(csv_reader)
#     for line in csv_reader:
#         # print(line)
#         print(f'studentas(-e) {line[0]} {line[1]} mokosi {line[3]}')

# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = reader(file)
#     data = list(csv_reader) # gaunam viska iskart
#     print(data)
#
# from csv import DictReader
#
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = DictReader(file) # as OrderedDicts
#     for row in csv_reader:
#         print(row)

# from csv import DictReader
#
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         print(f"Studentas(-e) {row['Vardas']} {row['Pavardė']} mokosi {row['Universitetas']}")

# from csv import DictReader
#
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = DictReader(file, delimiter=',') # delimiter leidzia pakeisti skirtuka csv faile
#     for row in csv_reader:
#         print(row)

# from csv import reader
#
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = reader(file, delimiter=',') # delimiter galima naudoti ir su paprastu reader
#     for row in csv_reader:
#         print(row)

# print("------------------4 uzd.---------------------")
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     students = list(csv_reader)
#     average_sum = 0
#     min_student_average = students[0]
#
#     for student in students:
#         average_sum += float(student[4])
#         if student[4] < min_student_average[4]:
#             min_student_average = student
#     average_of_average = round(average_sum / len(students), 2)
#     print(f"Vidurkių vidurkis: {average_of_average}")
#     print(f"Studentas su žemiausiu vidurkiu: {min_student_average[0]} {min_student_average[1]}")

# print("------------------5 uzd.---------------------")
# from csv import DictReader
#
# with open('./auto.csv', encoding='utf8') as file:
#     csv_reader = DictReader(file)
#     cyl_sum = 0
#     cyl_total = 0
#     for row in csv_reader:
#         print(f"Auto model: {row['model']}, cylinders: {row['cyl']}")
#         cyl_sum += int(row["cyl"])
#         cyl_total += 1
#     print(f"cyl average: {cyl_sum/cyl_total}")

# from csv import writer
#
# with open('./fighters.csv', 'w', newline='') as file:
#     csv_writer = writer(file)
#     csv_writer.writerow(['Character', 'Move'])
#     csv_writer.writerow(['Ryu', 'Hadouken'])

# from csv import reader, writer
#
# with open('./cats.csv') as file:
#     csv_reader = reader(file)
#     cats = [[s.upper() for s in row] for row in csv_reader]
#     print(cats)
#
# with open('./cats-upper.csv', 'w', newline='') as file:
#     csv_writer = writer(file)
#     csv_writer.writerows(cats)

# from csv import reader, writer
#
# with open('./cats.csv') as file_read:
#     csv_reader = reader(file_read)
#     with open('./cats2.csv', 'w', newline='') as file_write:
#         csv_writer = writer(file_write)
#         for cat in csv_reader:
#             csv_writer.writerow(cat)

# from csv import DictWriter
#
# with open('./fighters-write.csv', 'w', newline='') as file:
#     headers = ['Character', 'Move']
#     csv_writer = DictWriter(file, fieldnames=headers)
#     csv_writer.writeheader()
#     csv_writer.writerow({
#         "Character": 'Ryu',
#         'Move': 'Hadouken'
#     })

from csv import reader, writer, DictReader, DictWriter

# print("------------------6 uzd.---------------------")
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = reader(file)
#     next(csv_reader)
#     students = list(csv_reader)
#     average_sum = 0
#     student_with_min_average = students[0]
#     student_with_max_age = students[2]
#
#     for student in students:
#         average_sum += float(student[4])
#         if student[4] < student_with_min_average[4]:
#             student_with_min_average = student
#         if student[2] > student_with_max_age[2]:
#             student_with_max_age = student
#     average_of_average = round(average_sum / len(students), 2)
#     print(f"Vidurkių vidurkis: {average_of_average}")
#     print(f"Studentas su žemiausiu vidurkiu: {student_with_min_average[0]} {student_with_min_average[1]}")
#     print(f"Vyriausias studentas: {student_with_max_age[0]} {student_with_max_age[1]}")
#     with open('./students-write.txt', 'w', encoding='utf8', newline='') as file:
#         csv_writer = writer(file)
#         csv_writer.writerow(student_with_min_average)
#         csv_writer.writerow(student_with_max_age)

# print("------------------7 uzd.---------------------")
# with open('./students.csv', encoding='utf8') as file:
#     csv_reader = DictReader(file)
#     best_students = []
#     with open('./students-best.csv', 'w', encoding='utf8', newline='') as file:
#         headers = csv_reader.fieldnames
#         csv_writer = DictWriter(file, fieldnames=headers)
#         csv_writer.writeheader()
#         for row in csv_reader:
#             if float(row['Vidurkis']) > 8:
#                 csv_writer.writerow(row)
