x = input("수열을 넣어주세요: ").split()
y = list(map(int, x)) # map은 원본 리스트를 변경하지 않고 새 리스트를 생성
print("입력한 수열 = {}".format(y))
z = len(x)

for i in range(0,z-1):
    for j in range(0,z-1):
        if y[j] > y[j + 1]:
            a = y[j]
            y[j] = y[j + 1]
            y[j + 1] = a

print("오름차순으로 정렬된 수열 = {}".format(y))