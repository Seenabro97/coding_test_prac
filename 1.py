count=0
def main():
    test_case='abcdefghijklmn.p'
    print(solution(test_case))

def test2(ch):
    if ch.isalpha():
        return True
    if ch.isalnum():
        return True
    if ch == '-' or ch == '_' or ch == '.':
        return True
    else:
        return False
    

def solution(new_id):
    answer=''
    test1=new_id.lower()
    print(test1)
    test2_result=''
    test3_result=''
    
    for ch in test1:
        if test2(ch):
            test2_result+=ch

    print(test2_result)
    test3_result+=test2_result[0]
    for i in range(1,len(test2_result)):
        if test2_result[i]!='.' or test2_result[i-1]!=test2_result[i]:
            test3_result+=test2_result[i]
    print(test3_result)
    if test3_result and test3_result[0]=='.':
        test3_result=test3_result[1:]
        print(test3_result)
    if test3_result and test3_result[-1]=='.':
        test3_result=test3_result[:-1]
        print(test3_result)
    if not test3_result:
        test3_result='a'
    if len(test3_result)>=16:
        test3_result=test3_result[:15]
        print(test3_result)
    if test3_result and test3_result[-1]=='.':
        test3_result=test3_result[:-2]
    if len(test3_result)<=2:
        for i in range(len(test3_result)-1,2):
            test3_result+=test3_result[i]    
    answer=test3_result    
    return answer

main()
