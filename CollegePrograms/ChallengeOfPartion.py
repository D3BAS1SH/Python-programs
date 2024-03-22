#Write a program to keep on partitioning and make new list and store it.
FINALL=[]

def Divider(V,L,R):
    global FINALL
    MAINLIST=[]
    if(L>=R):
        return
    X=(L+int(((R-L)/2)))
    print(f"Parition L : {V[L:X+1]} R : {V[X+1:R+1]}")
    MAINLIST=[Divider(V,L,X),Divider(V,X+1,R)]
    print(MAINLIST)
    FINALL.append(Divider(V,L,X))
    FINALL.append(Divider(V,X+1,R))
    # Divider(V,L,X)
    # Divider(V,X+1,R)
    return [V[L:X+1],V[X+1:R+1]]

Divider([1,2,3,4,5,6,7,8],0,7)
print(FINALL)
# print(MAINLIST)