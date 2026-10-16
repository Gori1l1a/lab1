sales=[{'name':'banana' ,'price':'100' ,'quantity': '1000',},
    {'name':'apple' ,'price':'80' ,'quantity': '2000',},
    {'name':'orange' ,'price':'75' ,'quantity': '1345',},
    {'name':'grape' ,'price':'220' ,'quantity': '970',},
    {'name':'grape' ,'price':'220' ,'quantity': '100',}
]
profit={}

for i in sales:
   name=i['name']
   price=i['price']
   quantity=i['quantity']
   result=int(price)*int(quantity)
   
   profit[name]=profit.get(name,0)+result

print(profit)

profitable=''
max=0
for name,result in profit.items():
    if result>max:
        max=result
        profitable=name
print(f"Самый выгодный товар:{profitable}, выручка:{max}")

print(f"Кол-во уникальных товаров:{len(profit)}")