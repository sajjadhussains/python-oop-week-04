
class User:
    
    def __init__(self,name,roll,password) -> None:
        self.name=name
        self.roll=roll
        self.password=password
        self.borrow_books=[]
        self.returned_books=[]

class Library:
    def __init__(self,book_list) -> None:
        self.book_list=book_list
    def borrow_book(self,bookName,user):
        for book in self.book_list:
            if book==bookName:
                if bookName in user.borrow_books:
                    print("Age boi ferot dau")
                    return
                if self.book_list[book]==0:
                    print("Boi shesh hoye gese")
                    return
                self.book_list[book]-=1
                user.borrow_books.append(bookName)
                # print(user.borrow_books[bookName])
                print("You have borrowed this book")
                return
        print("Book not available")
    
    def return_book(self,bookName,user):
        for book in self.book_list:
            if book==bookName:
                self.book_list[book]+=1
                user.borrow_books.remove(bookName)
                user.returned_books.append(bookName)
                print("book returned successfully")
                return
        print("Kar boi ferot dite ashco?")
    def availability(self):
        for book in self.book_list:
                if self.book_list[book]>0:
                    print(book)

    def donate(self,bookName,amount):
        for book in self.book_list:
            if book==bookName:
                self.book_list[book]+=amount
                print("thanks for donating")
                return
        self.book_list[bookName] = amount

library=Library({"English":2,"Bangla":5,"Math":3})
allUsers=[]
currentUser=None

while True:
    if currentUser==None:
        print("Not Logged In\n Please Login or create account(L/C)")
        option=input()
        if option=="L":
            roll=int(input("Roll: "))
            password=input("Password:")
            match=False
            for user in allUsers:
                if user.roll==roll and user.password==password:
                    currentUser=user
                    match=True
            if match==False:
                print("User not found")
        else:
            name=input("Name: ")
            roll=int(input("roll: "))
            password=input("Password: ")
            user=User(name,roll,password)
            currentUser=user
    else:
        print("OPTIONS")
        print("_________")
        print("1.Borrow a book")
        print("2.Return a book")
        print("3.Borrowed book list")
        print("4.Returned book list")
        print("5.Availability check: ")
        print("6.Donate")
        print("7.Logout")

        x=int(input("Give option: "))
        if x==1:
            bookName=input("Book name: ")
            library.borrow_book(bookName,currentUser)
        elif x==2:
            bookName=input("Book name: ")
            library.return_book(bookName,currentUser)
        elif x==3:
            print(currentUser.borrow_books)
        elif x==4:
            print(currentUser.returned_books)
        elif x==5:
            library.availability()
        elif x==6:
            bookName=input("Bookname: ")
            amount =int(input("Amount: "))
            library.donate(bookName,amount)
        elif x==7:
            currentUser=None
