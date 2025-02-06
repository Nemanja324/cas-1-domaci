program_name = "Bookstore"
version = 1.0
is_new_program = True
Books = ['Harry Potter 1','LOTR Collection','Harry Potter 2']

print("Prvi clan liste prije promjene",Books[0])
print("-------------------------------------------")
Books[0] = "Rise of the Litch King"
Books.pop(2)
print("Prvi clan liste posle promjene",Books[0])