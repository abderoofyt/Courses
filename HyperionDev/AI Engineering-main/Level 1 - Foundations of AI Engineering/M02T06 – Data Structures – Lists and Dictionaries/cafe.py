menu = ['coffee', 'tea', 'egg', 'bread', ]

stock = ['100', '120', '150', '50']

price = ['10', '13', '15', '8']

total_stock = 0
for i in stock: 
    for j in price:
        total_stock += int(i) * int(j)

print("R"+ str(total_stock))
