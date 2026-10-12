print("Доступные категории: длина, масса, температура, время")
category = input("Введите тип измерения: ").lower().strip()

if category == "длина":
    from_unit = input("Введите исходную единицу: ").lower().strip()
    to_unit = input("Введите целевую единицу: ").lower().strip()
    value = float(input("Введите значение: "))

    if from_unit == "мм":
        base = value * 0.001
    elif from_unit == "см":
        base = value * 0.01
    elif from_unit == "м":
        base = value
    elif from_unit == "км":
        base = value * 1000
    else:
        print("Ошибка: неизвестная единица!")
        base = None

    if base is not None:
        if to_unit == "мм":
            result = base / 0.001
        elif to_unit == "см":
            result = base / 0.01
        elif to_unit == "м":
            result = base
        elif to_unit == "км":
            result = base / 1000
        else:
            print("Ошибка: неизвестная единица!")
            result = None

        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}")

elif category == "масса":
    print("Доступные единицы: мг, г, кг, т")
    from_unit = input("Введите исходную единицу: ").lower().strip()
    to_unit = input("Введите целевую единицу: ").lower().strip()
    value = float(input("Введите значение: "))

    if from_unit == "мг":
        base = value * 0.000001
    elif from_unit == "г":
        base = value * 0.001
    elif from_unit == "кг":
        base = value
    elif from_unit == "т":
        base = value * 1000
    else:
        print("Ошибка: неизвестная единица!")
        base = None

    if base is not None:
        if to_unit == "мг":
            result = base / 0.000001
        elif to_unit == "г":
            result = base / 0.001
        elif to_unit == "кг":
            result = base
        elif to_unit == "т":
            result = base / 1000
        else:
            print("Ошибка: неизвестная единица!")
            result = None

        if result is not None:
            print(f"{value} {from_unit} = {result:} {to_unit}")

elif category == "температура":
    print("Доступные единицы: цельсий, фаренгейт, кельвин")
    from_unit = input("Введите исходную единицу: ").lower().strip()
    to_unit = input("Введите целевую единицу: ").lower().strip()
    value = float(input("Введите значение: "))

    if from_unit == "цельсий":
        celsius = value
    elif from_unit == "фаренгейт":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "кельвин":
        celsius = value - 273.15
    else:
        print("Ошибка: неизвестная единица!")
        celsius = None

    if celsius is not None:
        if to_unit == "цельсий":
            result = celsius
        elif to_unit == "фаренгейт":
            result = celsius * 9 / 5 + 32
        elif to_unit == "кельвин":
            result = celsius + 273.15
        else:
            print("Ошибка: неизвестная единица!")
            result = None

        if result is not None:
            print(f"{value} {from_unit} = {result:} {to_unit}")

elif category == "время":
    print("Доступные единицы: сек, мин, час, сутки")
    from_unit = input("Введите исходную единицу: ").lower().strip()
    to_unit = input("Введите целевую единицу: ").lower().strip()
    value = float(input("Введите значение: "))

    if from_unit == "сек":
        base = value
    elif from_unit == "мин":
        base = value * 60
    elif from_unit == "час":
        base = value * 3600
    elif from_unit == "сутки":
        base = value * 86400
    else:
        print("Ошибка: неизвестная единица!")
        base = None

    if base is not None:
        if to_unit == "сек":
            result = base
        elif to_unit == "мин":
            result = base / 60
        elif to_unit == "час":
            result = base / 3600
        elif to_unit == "сутки":
            result = base / 86400
        else:
            print("Ошибка: неизвестная единица!")
            result = None

        if result is not None:
            print(f"{value} {from_unit} = {result} {to_unit}")


else:
    print("Ошибка: неизвестная категория измерения!")