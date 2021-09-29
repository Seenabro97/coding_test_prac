#https://programmers.co.kr/learn/courses/30/lessons/17683

m="ABC"
musicinfos=["11:00,11:05,WORLD,ABDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","13:00,13:05,WORLD,ABCDEF","23:59,00:00,HELLO,C#DEFGAB" ]
musicinfos.sort()
print(musicinfos)
played=[]
result=[]
played_time=[]
music_name=[]

def replace_char(melody):
    melody=melody.replace('A#','H')
    melody=melody.replace('C#','I')
    melody=melody.replace('D#','J')
    melody=melody.replace('F#','K')
    melody=melody.replace('G#','L')
    return melody

def calTime(start,end):
    s=start.split(':')
    e=end.split(':')

    hour=int(e[0])-int(s[0])
    minute=int(e[1])-int(s[1])
    if hour<0:
        hour=24+hour
    return hour*60+minute

m=replace_char(m)

for music in musicinfos:
    data=music.split(',')
    time=calTime(data[0],data[1])
    data[3]=replace_char(data[3])
    played_time.append(time)
    music_name.append(data[2])
    d,mod=divmod(time,len(data[3]))
    played.append(data[3]*d+data[3][:mod])
    

for i,play in enumerate(played):
    if m in play:
        result.append(i)

if not result:
    print("(None)")

print(played_time)
select=[item for i,item in enumerate(played_time) if i in result]
select2=[i for i,item in enumerate(played_time) if i in result and item==max(select)]
if len(select2)>1:
    print("dd")
print(select2)
print(music_name[select2[0]])

# def shap_to_lower(s):
#     s = s.replace('C#','c').replace('D#','d').replace('F#','f').replace('G#','g').replace('A#','a')
#     return s

# def solution(m,musicinfos):
#     answer=[0,'(None)']   # time_len, title
#     m = shap_to_lower(m)
#     for info in musicinfos:
#         split_info = info.split(',')
#         time_length = (int(split_info[1][:2])-int(split_info[0][:2]))*60+int(split_info[1][-2:])-int(split_info[0][-2:])
#         title = split_info[2]
#         part_notes = shap_to_lower(split_info[-1])
#         full_notes = part_notes*(time_length//len(part_notes))+part_notes[:time_length%len(part_notes)]
#         if m in full_notes and time_length>answer[0]:
#             answer=[time_length,title]
#     return answer[-1]
#다른사람 풀이