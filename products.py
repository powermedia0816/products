# 讀取檔案
products = []
with open('products.csv' , 'r' , encoding='utf-8')as f:
	for line in f:
		if "商品,價格" in line:
			continue
		name, price = line.strip().split(',')
		products.append([name,price])
print(products)
# 使用者輸入
while True:
	name = input("請輸入商品名稱:")
	if name == 'q': 
		break
	price = int(input("請輸入商品價格:"))
	products.append([name,price])
print(products)
#印出購買紀錄
for p in products: #了解二維清單中儲存的每個東西
	print(p[0], '的價格是：', p[1])
# 寫入檔案
with open('products.csv', 'w' , encoding = 'utf-8') as f:
	f.write('商品,價格\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')