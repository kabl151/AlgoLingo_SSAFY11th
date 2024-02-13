class_num = 0
total_grade = 0

for _ in range(20):
    arr = list(map(str, input().split()))
    if arr[2] == "P":
        pass
    elif arr[2] == "A+":
        total_grade += float(arr[1]) * 4.5
        class_num += float(arr[1])
    elif arr[2] == "A0":
        total_grade += float(arr[1]) * 4.0
        class_num += float(arr[1])
    elif arr[2] == "B+":
        total_grade += float(arr[1]) * 3.5
        class_num += float(arr[1])
    elif arr[2] == "B0":
        total_grade += float(arr[1]) * 3.0
        class_num += float(arr[1])
    elif arr[2] == "C+":
        total_grade += float(arr[1]) * 2.5
        class_num += float(arr[1])
    elif arr[2] == "C0":
        total_grade += float(arr[1]) * 2.0
        class_num += float(arr[1])
    elif arr[2] == "D+":
        total_grade += float(arr[1]) * 1.5
        class_num += float(arr[1])
    elif arr[2] == "D0":
        total_grade += float(arr[1]) * 1.0
        class_num += float(arr[1])
    else:
        class_num += float(arr[1])

print(f'{total_grade / class_num:.6f}')
        