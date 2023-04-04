data = list(input())
c_list = []
sum_num = 0

for d in data:
    if d.isdigit():
        sum_num += int(d)
    else:
        c_list.append(d)

if sum_num == 0:
    print("".join(sorted(c_list)))
else:
    print("".join(sorted(c_list)) + str(sum_num))
