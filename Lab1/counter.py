def Counter(arr):
    uppercount=0;
    lowercount=0;
    spaces=0;

    for i in arr:
        if(i>='A' and i<='Z'):
            uppercount=uppercount+1;
        if(i>='a' and i<='z'):
            lowercount=lowercount+1;
        if(i==" "):
            spaces=spaces+1;

    print("The Upper Case Characters are: ",uppercount)
    print("The Lower Case Characters are: ",lowercount)
    print("The Space Characters are: ",spaces)



arr ="""My Name is Umamah""";
Counter(arr);