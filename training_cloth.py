n=12
lost=[1,2,4,5,6,11]
reserve=[1,3,5,7,11]
lost.sort()
reserve.sort()
temp=[]
enter=[0]*len(lost)
for r in reserve:
    if r not in lost:
        temp.append(r)
    else:
        lost.remove(r)
for r in temp:
    for i in range(len(lost)):
        if enter[i]==1:
            continue
        if lost[i]==r-1 or lost[i]==r+1:
            enter[i]=1
            break
answer = n-(len(lost)-enter.count(1))
print(answer)

# def solution(n, lost, reserve):
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     for r in _reserve:
#         f = r - 1
#         b = r + 1
#         if f in _lost:
#             _lost.remove(f)
#         elif b in _lost:
#             _lost.remove(b)
#     return n - len(_lost)
#다른 사람 풀이