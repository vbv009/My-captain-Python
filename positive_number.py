n=list(input().split(','))
n[0]=n[0][1]
n[-1]=n[-1][0]
lst=[]
for num in n:
    if num=='' or num[0]=='-' or num[0]==']' :
        continue
    ele=int(num)
    if ele >= 0:
            ##num==lst
        lst.append(ele)
print(lst)
© 2020 GitHub, Inc.
