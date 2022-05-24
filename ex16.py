def verifica_multiplo(n):
    if n % 5 == 0:
        return n
    else:
        print(n)
        n += 1
        return verifica_multiplo(n)

def gradingStudents(grades):
    new_arr = []
    
    for x in grades:
        if x < 38:
            new_arr.append(x)
        else:
            multiple = verifica_multiplo(x)
            sub = multiple - x
            if sub < 3:
                new_arr.append(multiple)
            else:
                new_arr.append(x)

    return new_arr

   
grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)

print(result)