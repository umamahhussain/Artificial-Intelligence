def sum(str):
    sum=0

    for i in str:
        sum=sum+i
       
    return (sum)


def prod(str):
    prod=1

    for i in str:
        prod=prod*i

    return prod

def largest(str):
    large=str[0]

    for i in str:
        if(i>large):
            large=i
    
    return large

def smallest(str):
    small=str[0]

    for i in str:
        if(i<small):
            small=i

    return small

str = [1, 1, 2,3,1,2]
print(sum(str))
print(prod(str))
print(largest(str))
print(smallest(str))
