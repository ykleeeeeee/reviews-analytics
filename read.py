data = []
count = 0
with open ('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 1000 == 0:             # %= 把count 跟 1000 求於數
		    print('第', len(data), '筆')
print('檔案讀取完成,總共有', len(data), '筆資料')





#print(data)           #印出全部留言
#print(data[0])        #印出第一筆留言
#print('----------------------')
#print(data[1])


#求全部留言的全部長度
sum_len = 0
for d in data:
	sum_len = sum_len + len(d)
#	print(sum_len)
print('留言的平均長度為', sum_len/len(data))



#清單篩選，篩選留言長度小於100的留言
new= []
for d in data:
	if len(d) < 100:
		new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '筆提到good')
print(good[0])