def counter(str):
    even=0
    odd=0
    positive=0
    negative=0
    zero=0

    for i in str:
        if(i==0):
            zero=zero+1
        if(i%2==0):
            even=even+1
        if(i%2!=0):
            odd=odd+1
        if(i<0):
            negative=negative+1
        if(i>=0):
            positive=positive+1
    
    print("Number of zeros : ",zero)
    print("Number of positives : ",positive)
    print("Number of negatives : ",negative)
    print("Number of even numbers : ",even)
    print("Number of odd numbers : ",odd)



str=[0,0,0,0,1,2,3,5,6,7,-1,-2,4,-5,-8,9,8,1,8,0];
print("The original array is: ",str)
counter(str)
