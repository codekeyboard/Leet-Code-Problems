def armstrong(n):
    length = len(str(n))
    num = n 
    ams_num = 0
    while num > 0:
        last = num % 10
        ams = last ** length
        print(ams_num)
        num = num // 10
        ams_num = ams_num + ams

    if ams_num == n: 
        print("Amstrong", ams_num)
    else:
        print("Not Amstring", ams_num)
                

armstrong(153)