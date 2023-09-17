data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:             # %= 把count 跟 1000 求於數
		    print('第', len(data), '筆')
print(len(data))

#print(data)           #印出全部留言
print(data[0])        #印出第一筆留言
print('----------------------')
print(data[1])
