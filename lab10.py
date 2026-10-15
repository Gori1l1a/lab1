price=int(input("Введите сумму покупки: "))
age=int(input("Введите возраст: "))
if_hb=input("Есть ли у вас сегодня др (да/нет): ").lower().strip()
vip=input("Вы являетесь ли вы вип-клиентом (да/нет): ").lower().strip()

discount=0

if price>=  1000:
    print("Вы получите скидку 10%")
    discount+=10

if age>63:
    print("Вы получите скидку 5%")
    discount+=5
    
if if_hb=="да":
    print("Вы получите скидку 5%")
    discount+=5
    
if vip == "да":
    if discount < 15:
        print("Применена VIP-скидка 15% .")
        discount = 15
    else:
        print("VIP-скидка 15% не применяется .")

if discount>25:
    discount=25
     
print(f"Скидка {discount}%")
print(f"Сумма покупки со скидкой {price-price*discount/100} руб.")