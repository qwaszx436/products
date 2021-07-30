#檢查檔案
import os
product = []
if os.path.isfile('product.csv'):
	print('有歷史檔案')
	#讀取資料
	with open('product.csv', 'r', encoding = 'utf-8')as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			product.append([name , price])
else:
	print('沒有歷史檔案')

	#輸入新商品
	while True:
		name = input('請輸入商品名稱')
		if name == 'q':
			break
		price = input('請輸入商品價格')
		product.append([name, price])
	print(product)
	#寫入資料
	with open('product.csv', 'w', encoding = 'utf-8') as f:
		f.write('商品' + ',' + '價格' + '\n')
		for p in product:
			f.write(p[0] + ',' + p[1] + '\n')
