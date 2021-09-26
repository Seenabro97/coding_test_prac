#42583
from collections import deque
priorities=[1, 1, 9, 1, 1, 1]
priorities=deque(priorities)
queue=deque([x for x in range(len(priorities))])
queue
result=[]
location=0
checked=0
# start=0
# end=len(priorities)-1

# while True:
#     if start==end:
#         break
#     for j in range(start+1,end):
#         if(priorities[j]>priorities[start]):
#             end=(end+1)%len(priorities)
#             break
#     start+=1

while queue:
    for i in priorities:
        if(priorities[0]<i):
            queue.append(queue[0])
            priorities.append(priorities[0])
            checked=1
            break
    if checked==0:
        result.append(queue[0])
    queue.popleft()
    priorities.popleft()
    checked=0

print(result.index(location))

# def solution(priorities, location):
#     queue =  [(i,p) for i,p in enumerate(priorities)]
#     answer = 0
#     while True:
#         cur = queue.pop(0)
#         if any(cur[1] < q[1] for q in queue):
#             queue.append(cur)
#         else:
#             answer += 1
#             if cur[0] == location:
#                 return answer
# any를 사용한 풀이