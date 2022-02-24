#coding:utf-8
from itertools import count
sum="总人名单用 | 分开"
arrive="上课实到人员 你可以使用ocr进行识别"
sum=sum.split('|')
count=0
list=[]
for i in sum:
    if i not in arrive:
        list.append(i)
        count+=1
        
print("本堂课缺勤人数："+str(count)+'\n缺勤人员为:')
print(list)

