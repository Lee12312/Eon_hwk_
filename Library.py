import sys
import os
import Book

class Library:
    def __init__(self, Booklist):
        self.Booklist = Booklist
        self.User_Add_Booklist = []
        self.Book = []
        self.User_Book_Search = []

    def AddBook(self):
        print("도서 추가")
        print("도서명 저자 출판연도 출판사명 장르")
        UserInput = list(map(str,input("입력 : ").split()))
        self.Booklist.append(UserInput)
        self.User_Add_Booklist.append(UserInput)
        print("도서가 추가되었습니다")
        return self.Menu()

    def FindBook(self):
        Num_Cnt = 0
        print("도서검색(1.도서명 2.저자 3.출판년도 4.출판사명 5.장르) 메뉴로가려면 6번입력")
        UserChoice = int(input("숫자입력 : "))
        if UserChoice == 1:
            UserInput1 = str(input("도서명 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput1 == self.Booklist[i][0]:                    
                    print(self.Booklist[i])        
                    Num_Cnt += 1
                    if i == len(self.Booklist) - 1:
                        print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
                elif i ==len(self.Booklist) - 1:
                    print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
            return self.FindBook()
        elif UserChoice == 2:
            UserInput2 = str(input("저자 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput2 == self.Booklist[i][1]:
                    print(self.Booklist[i])
                    Num_Cnt += 1
                    if i == len(self.Booklist) - 1:
                        print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
                elif i == len(self.Booklist) - 1:
                    print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
            return self.FindBook()
        elif UserChoice == 3:
            UserInput3 = str(input("출판년도 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][2]:
                    print(self.Booklist[i])
                    Num_Cnt += 1
                    if i == len(self.Booklist) - 1:
                        print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
                elif i == len(self.Booklist) - 1:
                    print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
            return self.FindBook()
        elif UserChoice == 4:
            UserInput3 = str(input("출판사 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][3]:
                    print(self.Booklist[i])
                    Num_Cnt += 1
                    if i == len(self.Booklist) - 1:
                        print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
                elif i == len(self.Booklist) - 1:
                    print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
            return self.FindBook()
        elif UserChoice == 5:
            UserInput3 = str(input("장르 입력 : "))
            for i in range(len(self.Booklist)):
                if UserInput3 == self.Booklist[i][4]:
                    print(self.Booklist[i])
                    Num_Cnt += 1
                    if i == len(self.Booklist) - 1:
                        print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
                elif i == len(self.Booklist) - 1:
                    print("검색결과: {0}개의 도서가 검색 되었습니다.".format(Num_Cnt))
            return self.FindBook()    
        elif UserChoice == 6:
            return self.Menu()
        else:
            print("1~6까지의 숫자만 입력하세요")
            return self.FindBook()

    def ModifyBook(self):
        print("도서 정보 수정")
        UserInput = str(input("수정할 도서명을 입력해주세요 : "))
        for i in range(len(self.Booklist)):    
            if UserInput == self.Booklist[i][0]:
                print("수정할 정보입력")
                UserInput_MDY = list(map(str, input("도서명 저자 출판일 출판사명 장르 (입력) :").split()))
                del self.Booklist[i]
                self.Booklist.insert(i, UserInput_MDY)
                print("수정 완료")
                return self.Menu()
            else:
                if i == len(self.Booklist):
                    print("수정할 도서가 없습니다.")
        return self.ModifyBook()

    def DeleteBook(self):
        print("도서 삭제")
        UserInput = str(input("도서명 입력 : "))
        for i in range(len(self.Booklist)):
            if UserInput == self.Booklist[i][0]:
                del self.Booklist[i]
                print("도서 삭제 완료")
                return self.Menu()
            else:
                if i == len(self.Booklist):
                    print("목록에 없는 도서입니다.")
        return self.DeleteBook()

    def ShowBook(self):
        for i in range(len(self.Booklist)):
            print(self.Booklist[i])

        return self.Menu()

    def ProgramExit(self):
        print("프로그램을 종료합니다.")
        sys.exit()

    def SaveBook(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        Bookdata = open(my_file, 'w')
        UserInput = str(input("이때까지 내용들을 저장하시겠습니까? (y/n) : "))
        if UserInput == 'y':
            for i in range(len(self.Booklist)):
                Bookdata.writelines(" ".join(self.Booklist[i]))
                Bookdata.write("\n")
            print("저장완료")
            return self.Menu()
        elif UserInput == 'n':
            print("메뉴로 돌아갑니다.")
            return self.Menu()
        else:
            print("잘못 입력하셨습니다.")
            return self.SaveBook()
        Bookdata.close()

    def Menu(self):
        try:
            print("1. 도서 추가")
            print("2. 도서 검색")
            print("3. 도서 정보 수정")
            print("4. 도서 삭제")
            print("5. 현재 총 도서 목록 출력")
            print("6. 작업한 내용 저장")
            print("7. 프로그램 종료")
            User_Choice = int(input("입력 : "))

            if User_Choice == 1:
                self.AddBook()
            elif User_Choice == 2:
                self.FindBook()
            elif User_Choice == 3:
                self.ModifyBook()
            elif User_Choice == 4:
                self.DeleteBook()
            elif User_Choice == 5:
                self.ShowBook()
            elif User_Choice == 6:
                self.SaveBook()
            elif User_Choice == 7:
                self.ProgramExit()
            else:
                print("1부터 7까지의 숫자만 입력하세요.")
                return self.Menu()
        except ValueError:
            print("잘못입력하셨습니다.")
            return self.Menu()    
        
BookSet = Book.BookList()
BookSet.Booklist_Get()
BookSystem = Library(BookSet.Booklist)
BookSystem.Menu()