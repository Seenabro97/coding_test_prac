#https://programmers.co.kr/learn/courses/30/lessons/42747
citations=[8,8,8,8,8]

citations.sort(reverse=True)
print(citations)
H=0
for i,paper in enumerate(citations):
    if paper<i+1:
        H=i
        break

if all(len(citations)<=num for num in citations):
    H=len(citations)

print(H)

# def solution(citations):
#     citations.sort(reverse=True)
#     answer = max(map(min, enumerate(citations, start=1)))
#     return answer
#다른사람의 풀이