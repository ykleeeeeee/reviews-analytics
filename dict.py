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


#篩選快寫法
good = [d for d in data if 'good' in d]  #d=印出原始資料
#good = [1 for d in data if 'good' in d] #把資料轉換成1
print(good)

bad = ['bad' in d for d in data]   #'bad' in d 是一個運算，提到bad = true or false 
print(bad)
#bad = []
#for d in data:
#	bad.append('bad' in d')
print(data[0])


# 文字計數
wc = {} # word_count
for d in data:
    words = d.split()       #用空白鍵作分割時遇到連續的空白不會切成空字串
    for word in words:
        if word in wc:
            wc[word] += 1   #把目前的次數+1
        else:
            wc[word] = 1    #新增新的KEY進WC字典


for word in wc:
	if wc[word] > 1000000:
		print(word, wc[word])

print(len(wc))
print(wc['Allen'])

while True:
	word = input('請問你想查什麼字: ')
	if word == 'q':
	    break
	if word in wc:
		print(word, '出現過的次數為: ',wc[word])
	else:
		print('沒有出現過這個字喔')

print('感謝使用')
