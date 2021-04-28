#Finding the value of e upto Nth term

n = int(input("Insert the number of digits you want to see of e : \n "))
i = 1
e = 0
x = 2
z = 3
while i < 100:
    y = 1/(x)
    i +=1
    x = x*z
    z +=1
    e = e+y
e_str = str(e)
f = []
for u in range(2,n+2):
    f.append(e_str[u])
print("e = 2.", end = "")
print("".join(map(str, f)))
input()