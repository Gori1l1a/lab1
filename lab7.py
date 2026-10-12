b_min=60
b_sms=30
b_gig=1024
b_price=24.99

min=0.89
sms=0.59
gig=0.79

f_min=int(input("Введите количество израсходованных минут: "))
f_sms=int(input("Введите количество израсходованных SMS: "))
f_gig=int(input("Введите количество израсходованных мб: "))

extra_minutes = max(0, f_min - b_min)
extra_sms = max(0, f_sms - b_sms)
extra_gig = max(0, f_gig - b_gig)

cost_minutes = extra_minutes * min
cost_sms = extra_sms * sms
cost_gig = extra_gig * gig

result=(b_price+cost_gig+cost_minutes+cost_sms)*0.02+(b_price+cost_gig+cost_minutes+cost_sms)

if extra_minutes > 0:
    print(f"Дополнительные минуты ({extra_minutes} шт.): {cost_minutes} руб.")
if extra_sms > 0:
    print(f"Дополнительные SMS ({extra_sms} шт.): {cost_sms} руб.")
if extra_gig > 0:
    print(f"Дополнительный интернет ({extra_gig} Мб): {cost_gig} руб.")

print(f"Итого к оплате: {result} руб.")