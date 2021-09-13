from datetime import date
Y = int(input())
M = int(input())
D = int(input())
f_date = date(Y, M, D)
l_date = date(2021, 9, 13)
delta = l_date - f_date
print(delta)
