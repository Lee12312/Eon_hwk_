import os

class BookList:
    def __init__(self):
        self.Booklist = []

    def Booklist_Get(self):
        try:
            THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
            my_file = os.path.join(THIS_FOLDER, 'input.txt')
            Bookdata = open(my_file, 'r')
            while True:
                    Book_read = Bookdata.readline()   
                    if not Book_read:
                        break
                    Book_list = Book_read.split()
                    self.Booklist.append(Book_list)
            Bookdata.close()
            return self.Booklist
        except:
            pass