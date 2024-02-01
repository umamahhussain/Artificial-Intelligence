def median(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)
    size3 = size1 + size2
    arr3 = [0] * size3
    index=0;

    for i in range(len(arr1)):
        arr3[index]=arr1[i];
        index=index+1;

    for i in range(len(arr2)):
        arr3[index]=arr2[i];
        index=index+1;
    print(arr3)
    
    for i in range(i,len(arr3)):
        for j in range(i+1,len(arr3)):
            if(arr3[i]>arr3[j]):
                temp=arr3[i];
                arr3[i]=arr3[j];
                arr3[j]=temp;


    print("The sorted array is: ",arr3);

    median=size3//2;
    # print(median)
    median=arr3[median]
  
    print("The median is: ",median)



num1 = [1, 2, 3,6,7]
num2 = [4, 5]
median(num1, num2)
