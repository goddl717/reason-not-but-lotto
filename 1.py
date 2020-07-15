#한 번호대에 4개이상은 피하라
#4연번은 피해라
#같은 끝수 3개는 피해라
#2개의 쌍연번은 피해라
#낮은 수만 있는거 높은 수만 있는 것은 피해라 23기준
#도형이나 라인은 피해라
#말도 안되는 수는 피해라
#2홀4짝 4홀2짝 3홀3짝
#이전의 회사에서 3개이상 중복은 피해라
#일정한 규칙을 가진 숫자는 피해
def prime_number(number):   # number를 입력 받아 소수인지 아닌지 구분하는 함수
     # number가 1이 아니면, (1은 소수가 아님)
    if number != 1:                 
        # 2, 3, 4, ..., (number - 1)까지의 인수에 대해서
        for f in range(2, number):  
            # number가 위의 인수 중의 하나로 나누어지면, (나머지가 0이면)
            if number % f == 0:     
                return False    # 소수가 아님
    else:                       # number가 1이라면, 
        return False            # 소수가 아님
    
    # number가 1이 아니면서, 2부터 (number - 1)까지의 수로 나눠지지 않으므로
    # 소수로 판별됨 (소수는 1과 자신만을 인수로 갖는 수)
    return True 

#함수화 하기.
array = [] 

def make_lotto():
    import random
    global array
    prior = [19,32,37,40,41,43]

    #print(prior)

    list = []

    while len(list) < 6 :
        insert = random.randrange(1,46)
        if insert not in list :
            list.append(insert)

    list.sort()

    digit=[0,0,0,0,0,0]
    #print(list)

    #digit 4개 이상이면 실패를 출력.
    for item in list :
        #print(int(item/10))
        digit[int(item/10)] += 1
        
    #print(digit)
    for item in digit :
        if item >= 4 :
            #print("한번호 대에 4개이상은 실패!")
            return False 
            break

    # 4연속은 실패

    #list= [1,2,3,7,8,9]
    first = 0
    #print(len(list))
    i = 0
    while(i < len(list) -1  ):
        if (list[i] == list[i+1]-1):
            first +=1
        
            if(first >= 3):
               # print("4연속은 실패!")
                return False 
                break
        else :
            first = 0
        
        i+=1


    #같은 끝수 3개는 피해라


    i = 0
    digit=[0,0,0,0,0,0,0,0,0,0]
    for i in range(len(list)) :
        digit[int(list[i]%10)] +=1
    #print(digit)
    digit.sort()
    #print(digit)
    if digit[9] >=3 :
        #print("일의자리 중복이 3개 이상이라서 실패!")
        return False 

    # 몰려있는 거를 피해라.
    sum1 = 0

    for item in list :
        if item >= 23 :
            sum1 +=1
    if sum1 ==0 or sum1 ==6 or sum1 == 1 or sum1 == 5:
       # print("23이상 혹은 미만으로 몰려 있어서 실패!")
        return False 


    # 2개의 쌍연번을 피해

    #list = [1,2,3,4,5,6]
    first = 0
    i = 0
    while(i < len(list) -1):
        #print(list[i],list[i+1]-1)
        if (list[i] == list[i+1]-1):
            first +=1
        i+=1
    if first >=2 :
        #print("쌍연번을 피해라")
        return False 

    odd = 0


    # 홀수만 몰려있는거를 피한다.
    for i in range(len(list)) :
        if list[i] %2 ==1:
            odd +=1
    #print("홀수는 ",odd,"개")
    if(odd ==5 or odd == 6 or odd ==1 or odd ==0):
        #print("홀짝 균형이 안맞아서 실패!")
        return False 

    #list = [19,32,37,38,39,40]
    sum = 0
    #print(prior)
    #print(list)

    for item in prior:
        for jtem in list:
            #print(item,jtem)
            if item == jtem :
                sum +=1
                #print("더")
    #print(sum)
    if sum >=3 :
        #print("중복되는 것이 3개 이상이라서 실패!")
        return False 
    sum = 0
    for jtem in list:
        sum += jtem

    if 100 >= sum or sum >= 200 :
        #print(sum,"총합의 표준이 벗어납니다.실패!")
        return False 

    sum = 0
    for jtem in list:
       if prime_number(jtem) == True :
           sum+=1

    if(sum > 4):
       # print("소수의 수가 너무 많습니다 실패!")
        return False

    for item in list:
        array.append(item)
    return True



i = 0
dangchem = [16,19,24,33,42,44]

a = 0
b = 0
c = 0
d = 0

while (i<10000) :
    if make_lotto() == True :
        print(array)
        sum = 0
        for item in array:
            for jtem in dangchem :
                if item == jtem :
                    sum +=1

        if sum == 6 :
            #print("1등")
            a+=1  
        elif sum == 5 :
            #print("2등")
            b+=1
        elif sum == 4 :
            #print("3등")
            c+=1
        elif sum == 3:
            d+=1
            #print("4등")
                
        i+=1
        array.clear()

print ("1등 ",a)
print ("2등 ",b)
print ("3등 ",c)
print ("4등 ",d)


