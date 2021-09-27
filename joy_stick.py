#https://programmers.co.kr/learn/courses/30/lessons/42860
name="ABBAAAAAB"
UD_count=0
RL_count=0
RL_list=[0]*len(name)

for i,char in enumerate(name):
    if ord(char)!=65:
        RL_list[i]=1
    if ord(char)-65<=13:
        UD_count+=ord(char)-65
    else:
        UD_count+=91-ord(char)

RL_list[0]=0
current_point=0
move_count=0

while(True):
    if 1 not in RL_list:
        break
    move_count+=1
    if RL_list[current_point+move_count]==1:
        RL_count+=move_count
        RL_list[current_point+move_count]=0
        current_point+=move_count
        move_count=0      
        continue
    if RL_list[current_point-move_count]==1:
        RL_count+=move_count
        RL_list[current_point-move_count]=0
        current_point-=move_count
        move_count=0


answer=UD_count+RL_count
print(answer)
print(RL_count)