if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    sum = 0.00
    
    for i in student_marks[query_name]:
        sum += i
    
    result = sum / len(student_marks[query_name])

    result_formatted = "{:.2f}".format(result)
    print(result_formatted)