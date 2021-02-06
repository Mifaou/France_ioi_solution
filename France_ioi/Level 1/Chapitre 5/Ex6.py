a=int(input())
b=int(input())
z=a+b
if z>=10:
    print("Taxe spéciale ! ")
    print("36")
else:
    print("Taxe régulière")
    print(a*2+b*2)