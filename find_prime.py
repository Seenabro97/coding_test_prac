#https://programmers.co.kr/learn/courses/30/lessons/42839

numbers="011"

def isPrime(num):
    for i in range(2,num**(1/2)):
        if num%i==0:
            return False
    return True

