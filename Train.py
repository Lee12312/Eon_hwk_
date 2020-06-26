import copy
import sys

class TrainServer:
    def __init__(self):
        self.TrainList = []
        self.Traintype_list = []

    def Train_Data_Get(self):
        try:
            traindata = open('C:/Users/82105/OneDrive/Desktop/eon hwk/TrainList.txt', 'r')
            while True:
                traindata_read = traindata.readline()   
                if not traindata_read:
                    break
                trainline_list = traindata_read.split()
                self.TrainList.append(trainline_list)

            self.TrainList.pop(0)
            return self.TrainList               #기차 리스트 반환
        except IOError as err:                       #예외처리
            print("알수없는 에러가 발생하였습니다.")
            print("{0}".format(err))

   
    def Trainlist_Set(self):
        Trainlist_copy = copy.deepcopy(self.TrainList)
        for i in range(len(Trainlist_copy)):
            Trainlist_copy[i].pop(5)
            self.Traintype_list.append(Trainlist_copy[i])
        
        return self.Traintype_list



class TrainSystem(TrainServer):
    def __init__(self, TrainList, Traintype_list):
        self.TrainList = TrainList
        self.Traintype_list = Traintype_list
        self.UserList = []
        self.UserSelection = 0
        self.UserReservation = []

    def Menu(self):
        print("메뉴를 선택하세요")
        print("1. 빠른시간 기차검색 및 예매")
        print("2. 전체 기차리스트 출력")
        print("3. 나의 예매현황 출력 및 예매취소")
        print("4. 프로그램 종료")
        self.UserSelection = int(input("번호입력 : "))

        if self.UserSelection == 1:
            self.Reservation()
        elif self.UserSelection == 2:
            self.Trainlist_Print()
        elif self.UserSelection == 3:
            self.User_Reservation()
        elif self.UserSelection == 4:
            self.ProgramExit()
        else:
            print("1부터4까지의 번호를 입력하세요")
            return self.Menu()

    def Compare(self):
        print("기차검색")
        print("(시간 출발지 -> 목적지 기차종류)")
        User_RInput = list(map(str,input("입력 (뒤로가려면 숫자1 입력) : ").split()))
        User_Time = []
        User_Time.append(User_RInput[0].split(':'))
        User_Time[0] = list(map(int, User_Time[0]))
        if User_RInput[0] == '1':
            return self.Menu()
        #가까운 시간 찾는 조건문
        if User_Time[0][0] == 6:
            if 0 <= User_Time[0][1] < 20:
                User_RInput.pop(0)
                User_RInput.insert(0,'06:05')
            elif 20 <= User_Time[0][1] < 55:
                User_RInput.pop(0)
                User_RInput.insert(0,'06:35')
            elif 55 <= User_Time[0][1] < 60:
                User_RInput.pop(0)
                User_RInput.insert(0,'07:15')
            else:
                print("시간 값을 0부터 60사이의 값을 입력해주세요.")
                return self.Compare()        
        elif User_Time[0][0] == 7:
            if 0 <= User_Time[0][1] <= 58:
                User_RInput.pop(0)
                User_RInput.insert(0,'07:15')
            elif 58 < User_Time[0][1] < 60:
                User_RInput.pop(0)
                User_RInput.insert(0,'08:42')
            else:
                print("시간 값을 0부터 60사이의 값을 입력해주세요.")
                return self.Compare()
        elif User_Time[0][0] == 8:
            User_RInput.pop(0)
            User_RInput.insert(0,'08:42')
        else:
            print("6~8 시 사이의 기차만 있습니다.")
            return self.Compare()
        return User_RInput

    def Reservation(self):
        User_RInput = self.Compare()        
        #출발지 목적지 기차종류를 찾는 조건문
        for i in range(len(self.Traintype_list)):
            if User_RInput == self.Traintype_list[i]:
                print("출발지와 목적지에 따른 가까운 시간 기차")
                print(User_RInput)
                choice = str(input("예매하시겠습니까? (y/n) : "))
                if choice == 'y':
                    self.UserReservation.append(User_RInput)
                    ChangeNum = str(int(self.TrainList[i][5]) - 1)
                    self.TrainList[i].pop(5)
                    self.TrainList[i].append(ChangeNum)
                    print("예매되었습니다.")
                    return self.Menu()
                elif choice == 'n':
                    print("메뉴로 돌아갑니다.")
                    return self.Menu()
                else:
                    print("y/n 중 하나의 값을 입력하세요.")
                    return self.Menu()
            else:
                if i >= len(self.Traintype_list) - 1:
                    print("기차목록에 해당 노선이 없습니다.")
                    return self.Menu()
                       
    def Trainlist_Print(self):
        print("전체 기차리스트 출력")
        for i in range(len(self.TrainList)):
            if self.TrainList[i][5] == '0':
                self.TrainList[i][5] = '매진'
            print(self.TrainList[i])
        return self.Menu()

    def User_Reservation(self):
        UserSelect = int(input("1.예매현황 출력 2.예매취소 3.메뉴로 돌아가기 : "))
        if UserSelect == 1:
            if not self.UserReservation:
                print("예약 현황이 없습니다.")
                return self.User_Reservation()
            else:
                print(self.UserReservation)
                return self.User_Reservation()
        elif UserSelect == 2:
            print("기차예매 취소")
            User_CInput = list(map(str,input("(시간 출발지 -> 목적지 기차종류) 입력 : ").split()))
            for i in range(len(self.UserReservation)):
                if User_CInput == self.UserReservation[i]:
                    del self.UserReservation[i]
                    print("예매가 취소되었습니다.")
                else:
                    print("예약된 정보가 없습니다.")

            for i in range(len(self.Traintype_list)):
                if self.Traintype_list[i] == User_CInput:
                    if self.TrainList[i][5] == '매진':
                        ChangeNum = '1'
                        self.TrainList[i].pop(5)
                        self.TrainList[i].append(ChangeNum)
                    else:
                        ChangeNum = str(int(self.TrainList[i][5]) + 1)
                        self.TrainList[i].pop(5)
                        self.TrainList[i].append(ChangeNum)

            return self.User_Reservation()
        elif UserSelect == 3:
            return self.Menu()

    def ProgramExit(self):
        print("프로그램을 종료합니다.")
        sys.exit()

Main_Train = TrainServer() #객체생성
Main_Train.Train_Data_Get() #객체 기차리스트 셋팅
Main_Train.Trainlist_Set()  #조건문에서 비교할 기차리스트 셋팅
Train1 = TrainSystem(Main_Train.TrainList, Main_Train.Traintype_list) #객체생성
Train1.Menu() 