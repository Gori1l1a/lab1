age=int(input("возраст заемщика: "))
income=float(input("ежемесячный доход: "))
credit=float(input("сумма кредита: "))
term=int(input("срок кредита в месяцах: "))
history=input("кредитная история(отличная/хорошая/удовлетворительная/плохая): ").strip().lower()
guarantors=input("поручители(да/нет): ").strip().lower()
collateral=input("залог(да/нет): ").strip().lower()

total_income=income*term
debt_ratio=credit/total_income

print("отношение кредита к доходу:",round(debt_ratio,2))

score=0

if debt_ratio<0.3:
    score=score+1
elif debt_ratio<0.6 :
    score=score+2
elif debt_ratio<0.9:
    score=score+3
else:
    score=score+4

if history=="отличная":
    score=score+0
elif history=="хорошая":
    score=score+1
elif history== "удовлетворительная":
    score=score+2
else:
    score=score+3

if guarantors=="да":
    score=score-1

if collateral=="да":
    score=score-1

if age<21 or age>65:
    score=score+1

if score<=1:
    category="низкий"
    rate=12.5
    decision="кредит одобрить"
    
elif score<=3:
    category="средний"
    rate=16.0
    decision="кредит одобрить с осторожностью"
    
elif score<=5:
    category="высокий"
    rate=21.5
    decision="скорее отклонить"
    
else:
    category="критический"
    rate=0
    decision="кредит отклонить"

print("категория риска:",category)

if rate>0:
    print("процентная ставка:",rate,"%")
else:
    print("процентная ставка: не предлагается")

print("рекомендация:",decision)