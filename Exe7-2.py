from random import randint
l=list()
for i in range(20):
	l=l+[randint(1,100)]
print('a.) ', l)
print('b.) ',sum(l)/len(l))
print('c.) ','The largest number is: ',max(l), ' and the least number is: ', min(l))
l.sort()
print('d.) ', 'The second largest number is: ',l[-2], 'and the second smallest is: ',l[1])
count=0
for item in l:
	if item%2==0:
		count+=1
print('e.) ',count)