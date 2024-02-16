def reverse(str):
    str2 = []
    for i in range(-1, -len(str)-1, -1):
        str2.append(str[i])
    print(str2)


# str=[]
# print("Please enter the integers: ");
# for i in range(10):
#     num=input()
#     str.append(num)
str = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reverse(str)







