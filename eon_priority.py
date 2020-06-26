wrk_cnt = int(input("작업 수  : "))
wrk_num = int(input("작업 번호  : "))
wrk_priority = list(map(int,input("작업 우선순위 : ").split()))

output_num = list(range(len(wrk_priority))) 
output_num[wrk_num] = "print" 
output_time = 0

while True:
    #첫번째 작업의 우선순위가 제일높을 때
    if wrk_priority[0] == max(wrk_priority): 
        output_time += 1
        if output_num[0] == "print":
            print("{}분".format(output_time))
            break
        else:
            wrk_priority.pop(0)
            output_num.pop(0)
    #첫번째 작업의 우선순위가 제일 높지 않을 때
    else:
        wrk_priority.append(wrk_priority.pop(0))
        output_num.append(output_num.pop(0))

