T = int(input())
a = T//1000
b = (T - a*1000)//100
c = (T - (a*1000+b*100))//10
d = T - (a*1000+b*100+c*10)
print(a+b+c+d)
