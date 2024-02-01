def power(x,e):

    ans=1;
    ans=int(ans);

    for i in range(e):
        ans=ans*x

    print("The answer is: ",ans);


print("Enter the number:")
x=input();
x=int(x);

print("Enter the exponent:")
e=input();
e=int(e);

power(x,e);
