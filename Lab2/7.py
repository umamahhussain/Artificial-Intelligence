tuple=1,2,3,4,5
a,b,c,d,e=tuple

print("a: ",a)
print("b: ",b)
print("c: ",c)
print("d: ",d)
print("e: ",e)

print("Original Tuple: ",tuple)
newitem=6
tuple=tuple+(newitem,)
print("Updated Tuple: ",tuple)

# Reverse the tuple 
revTuple = tuple[::-1]
print("Original Tuple: ",tuple)
print("Reversed Tuple:", revTuple)


tuple2=(("fruits",1),("vegetables",2),("juice",3),("chips",4))
dictionary=dict(tuple2)
print("\nDictionary created from the tuple:\n",dictionary)

tuple3=8,1,3,5,2
tuple3=list(tuple3)

for i in range(0,len(tuple3)):
    for j in range(i+1,len(tuple3)):
        if(tuple3[i]>tuple3[j]):
            temp = tuple3[i]
            tuple3[i] = tuple3[j]
            tuple3[j] = temp


print("Sorted Tuple is: ",tuple3)