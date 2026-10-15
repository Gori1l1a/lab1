a=input("Введите числa: ")
b=input("Введите числa: ")


list1=[]
for p in a.split():
    if "." in p:
        list1.append(float(p))
    else:
        list1.append(int(p))

list2=[]
for p in b.split():
    if "." in p:
        list2.append(float(p))
    else:
        list2.append(int(p))

print("Первый набор:",list1)
print("Второй набор:",list2)

set1=set(list1)
set2=set(list2)

both=set1 & set2

print("Есть в обоих наборах:",list(both))


only1=set1 - set2
only2=set2 - set1
print("только в первом:",list(only1))
print("только во втором:",list(only2))


rest=set1 ^ set2
print("все числа кроме общих:",list(rest))