str1=[0,2,4,6,8]
str2=[1,3,5,7,9]
str3=[]
size=len(str1)+len(str2)

i=0
index1=0
index2=0
while i<size:
    if(i%2==0):
        str3.append(str1[index1])
        index1=index1+1
    else:
        str3.append(str2[index2])
        index2=index2+1
    i+=1
    
print("The merged array is :",str3) 


