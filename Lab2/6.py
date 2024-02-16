import math
def palindrome(str):

    j=0
    flag=0
    for i in range(-1, math.floor((-len(str)-1)/2), -1):
        if(str[j]!=str[i]):
            flag = 1
        
        if(flag==1):
            break
        else:
            j=j+1
    
    if(flag==1) :
        return("Sorry not a palindrome")
    else:
        return("Yayy issa a palindrome")


str="racecar"
str2="car"

print(palindrome(str))
print(palindrome(str2))