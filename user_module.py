def sum(a,b):
    return a+b

def min(a,b):
    return a-b
# k=6
# for i in range(k+1,0,-1):
#     for j in range(0,i-1):
#         print(j,end ='')
#     print('')
# sta = 1
# sto = 2
# cur = sto
# for row in range(2, 6):
#     for col in range(sta, sto):
#         cur -= 1
#         print(cur, end=' ')
#     print("")
#     sta = sto
#     sto += row
#     cur = sto

rows = 5
k = 5 * rows - 2
for i in range(rows, -1, -1):
    for j in range(k, 0, -1):
        print(end=" ")
    k = k + 1
    for j in range(0, i + 1):
        print("*", end=" ")
    print("")