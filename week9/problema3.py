# -*- coding: utf-8 -*-

inputed_value = "start"
all_students = []

while inputed_value != "":
    if inputed_value != "start":
        all_students.append( (sum([float(input()) for i in range(2)])/2, inputed_value) )
    inputed_value = input("")

all_students.sort(key=lambda x: x[0], reverse=True)

[print(f"{student[1]} - {student[0]:.2f}") for student in all_students]