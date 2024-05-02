products = []
while True:
	name = input("請輸入商品名稱:")
	if name == 'q': 
		break
	price = int(input("請輸入商品價格:"))
	products.append([name,price])
print(products)

for p in products: #了解二維清單中儲存的每個東西
	print(p[0], '的價格是：', p[1])

with open('products.csv', 'w' ) as f:
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')