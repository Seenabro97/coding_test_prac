#https://programmers.co.kr/learn/courses/30/lessons/42883

# number="124177785427"
# k=6
# answer=""

# index=number.index(max(number[:k+1]))
# k-=index
# number=number[index:]

# for i in range(len(number)):
#     if k==0:
#         answer+=number[i:]
#         break
#     try:
#         if number[i]>=number[i+1]:
#             answer+=number[i]
#         else:
#             k-=1
#     except IndexError:
#         if k==1:
#             break
#         elif k>=2:
#             answer=answer[:-k+1]
#         else:
#             answer+=number[i]


# print(answer)

#try-catch문 하지만 실패한 문제

number="124177785427"
k=4

index=number.index(max(number[:k+1]))
k-=index
number=number[index:]

i=0
while(True):
    if k==0:
        break
    try:
        if number[i]<number[i+1]:
            number=number[:i]+number[i+1:]
            k-=1
            i-=1
            continue
    except IndexError:
        number=number[:-k]

    i+=1

print(number)