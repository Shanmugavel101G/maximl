import math
str1=input()
count=0
length=len(str1)
if length>=1 and length<=pow(10,5):
    res_str=[]
    for i in range(len(str1)):
        if str1[i-1]!=str1[i] and str1[i] not in res_str:
            res_str.append(str1[i])
    #print(res_str)
count=len(res_str)
print(count)
