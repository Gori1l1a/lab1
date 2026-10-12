secret_number=67

print("Угадай число от 1 до 100")
while True:
    
    a=int(input("Введите число:"))
    if a<secret_number:
        print("Больше!")
    elif a>secret_number:
        print("Меньше!")
    else:
        print("Вы угадали!")
        break
        
