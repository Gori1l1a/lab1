text=input("Введите числа через пробел: ")
parts=text.split()

numbers=[]
for p in parts:
    if "." in p:
        numbers.append(float(p))
    else:
        numbers.append(int(p))

unique=list(set(numbers))
print("уникальные числа:",unique)

repeats=[]
for n in set(numbers):
    if numbers.count(n)>1:
        repeats.append(n)
print("повторяющиеся числа:",repeats)

even=[n for n in numbers if n%2==0]
odd=[n for n in numbers if n%2!=0]
print("четные:",even)
print("нечетные:",odd)


negative=[n for n in numbers if n<0]
print("отрицательные:",negative)

floats=[n for n in numbers if type(n)==float]
print("числа с плавающей точкой:",floats)

total=sum(n for n in numbers if n%5==0)
print("сумма чисел кратных 5:",total)

print("самое большое число:",max(numbers))
print("самое маленькое число:",min(numbers))