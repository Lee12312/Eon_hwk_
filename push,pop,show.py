def menu():
    print("=======메뉴=======")
    print("PUSH : 1")
    print("pop : 2")
    print("SHOW : 3")
    print("(종료 하려면 1,2,3 이외의 수 입력)\n")

try:
    def check_list():
        menu_select = int(input("메뉴를 선택하세요 : "))
        if menu_select == 1:
            apd = int(input("수 입력 : "))
            num_list.append(apd)
            return check_list()       
        elif menu_select == 2:
            num_list.pop()
            return check_list()               
        elif menu_select == 3:
            print(num_list)
            return check_list()                
        else:
            print("======== 스택 프로그램을 종료합니다 ========")

    num_list= list()
    menu()
    check_list()

except:
    print("리스트가 비었습니다")