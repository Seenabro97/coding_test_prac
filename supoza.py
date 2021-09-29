#https://programmers.co.kr/learn/courses/30/lessons/42840

from typing import Counter


answer=[1,3,2,4,2]

first_pat=[1,2,3,4,5]
second_pat=[2,1,2,3,2,4,2,5]
third_pat=[3,3,1,1,2,2,4,4,5,5]

def create(pat):
    n,m=divmod(len(answer),len(pat))
    return pat*n+pat[:m]

result=[]
for pat in [first_pat,second_pat,third_pat]:
    temp=create(pat)
    count=0
    for num,anw in enumerate(answer):
        if temp[num]==anw:
            count+=1
    result.append(count)

test=[i+1  for i,item in enumerate(result) if item==max(result)]
print(test)

# from itertools import cycle

# def solution(answers):
#     giveups = [
#         cycle([1,2,3,4,5]),
#         cycle([2,1,2,3,2,4,2,5]),
#         cycle([3,3,1,1,2,2,4,4,5,5]),
#     ]
#     scores = [0, 0, 0]
#     for num in answers:
#         for i in range(3):
#             if next(giveups[i]) == num:
#                 scores[i] += 1
#     highest = max(scores)

#     return [i + 1 for i, v in enumerate(scores) if v == highest]
#다른사람의 답 itertool의 cycle을 이용