# n*n 행렬에서 n의 값을 받는 함수
def Vector():
    try:
        n = int(input("수 입력 : "))
        return n
    except ValueError:
        print("숫자를 잘못입력하셨습니다.")

Matrix_Num = Vector()   # n*n 의 행렬을 만들 n의 값을 입력받는다.

ZeroArr = [[0]*Matrix_Num for i in range(Matrix_Num)] #n*n의 영행렬

num = 0 # 달팽이 배열의 숫자들
w = 0  #달팽이 배열의 행 (width)
h = -1  # 달팽이 배열의 열 (height)
k = 1 # 크기조절

def Snail_function(Matrix_Num, num, k, w, h):
    for i in range(Matrix_Num):
        num += 1
        h = h + k
        ZeroArr[w][h] = num
    
    Matrix_Num -= 1     # 행, 열의 끝점에 도달하면 다음 수행할 반복이 하나씩 줄음

    for j in range(Matrix_Num):
        num += 1
        w = w + k
        ZeroArr[w][h] = num

    k = k * (-1)    # 행과 열을 한번씩 로테이션 돈 후에 다시 거꾸로 로테이션 돌기위함

    if num == Matrix_Num ** 2:
        for i in range(len(ZeroArr)):
            print(ZeroArr[i])
    else:
        return Snail_function(Matrix_Num, num, k, w, h) #재귀함수

Snail_function(Matrix_Num, num, k, w, h)

