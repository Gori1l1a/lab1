sum=int(input("Введите сумму в рублях: "))

banknote_100=sum//100
sum=sum%100

banknote_50=sum//50
sum=sum%50

banknote_10=sum//10
sum=sum%10

banknote_5=sum//5
sum=sum%5

banknote_2=sum//2
sum=sum%2

banknote_1=sum//1
sum=sum%1

print("Для размера потребуется:")

if banknote_100>0:
    print(f"{banknote_100} купюр по 100 рублей.")
if banknote_50>0:
    print(f"{banknote_50} купюр по 50 рублей.")
if banknote_10>0:
   print(f"{banknote_10} купюр по 10 рублей.")
if banknote_5>0:
    print(f"{banknote_5} купюр по 5 рублей.")
if banknote_2>0:
    print(f"{banknote_2} купюр по 2 рублей.")
if banknote_1>0:
    print(f"{banknote_1} купюр по 1 рублей.")
