Book=dict()
Book["Title"]=input("Title of the book : ")
Book["Author"]=input("Author of the book : ")
Book["Year"]=input("Year of Release : ")

for x in Book.keys():
    print(f"{x} : {Book[x]}")