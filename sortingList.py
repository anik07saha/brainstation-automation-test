student_list = []
student_count = int(input())
item_in_a_row = 3
for i in range(0, student_count):
    list_item = list(map(str.strip,input().strip().split()))[:item_in_a_row]

    student_list.append(list_item)


print(student_list)