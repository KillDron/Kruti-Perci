t = 0
N = ""
P = ""
ID = input()
for i in ID:
    if i != " " and t == 0:
        N += i
    elif i == " ":
        t += 1
    else:
        P += i
print(P,N)
