#https://programmers.co.kr/learn/courses/30/lessons/42748

array=[1, 5, 2, 6, 3, 7, 4]
commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer=[]

for command in commands:
    temp=sorted(array[command[0]-1:command[1]])
    answer.append(temp[command[2]-1])

print(answer)

# def solution(array, commands):
#     return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
#다른 사람 풀이 람다함수와 map함수 이용