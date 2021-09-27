#https://programmers.co.kr/learn/courses/30/lessons/42746

numbers=[23, 232, 21, 212, 1000, 565,77,111,214,23,0,0]
str_nums=list(map(str,numbers))

answer=''
result=[[i] for i in range(10)]

for num in str_nums:
    result[int(num[0])].append(num)

for num_list in reversed(result[1:]):
    temp=[]
    for num in num_list[1:]:
        temp.append(int(num)/int(num[0]*len(num)))
    temp=sorted(list(zip(temp,num_list[1:])),key=lambda x:x[0],reverse=True)
    for num in temp:
        answer+=num[1]
if(answer):
    for zero in result[0][1:]:
        answer+=zero
else:
    answer='0'

print(answer)

# def solution(numbers):
#     numbers = list(map(str, numbers))
#     numbers.sort(key=lambda x: x*3, reverse=True)#문자열 자체를 정렬
#     return str(int(''.join(numbers)))#조인연산
#다른 사람의 풀이