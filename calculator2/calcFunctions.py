from math import factorial as fact

romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'),
        (1, 'I')
]

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
        if n >= 4000 or n<=0:       #음수일 때도 에러 처리
            return 'Error!'

        result = ''

        for value, letters in romans:
            while n >= value:
                result += letters
                n -= value
        return result
    except:
        return 'Error!'


def romanToDec(numStr):
     try:
         nu = numStr
         r=0
         romdic = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}

         while(len(nu)):        # nu의 길이가 0이 아닐 때 반복하여 검사
             if len(nu)==1:     # nu의 길이가 1이면 비교하지 않고 바로 r에 더하여 break
                 r+=romdic[nu[0]]
                 break
             elif romdic[nu[0]]>=romdic[nu[1]]:     # nu의 길이가 2이상일 때 nu[0]과 nu[1]을 비교하여
                 r+=romdic[nu[0]]                   # nu[0]>=nu[1]이면 첫번째 문자열은 무난하게 r에 더해줌
                 nu=nu[1:]                          # nu에서 nu[0]을 뺌으로서 문자열 슬라이싱

             else:                                  # nu의 길이가 2이상일 때, nu[0]<nu[1]일 때 더해야 할 수는 nu[1]-nu[0]이므로
                 r=r+romdic[nu[1]]-romdic[nu[0]]    # r에 nu[1]을 더하고 nu[0]을 뺌
                 if len(nu)>=3:                     # nu에서 nu[0]과 nu[1]을 모두 빼야하므로 슬라이싱 범위는 3이상일 때
                     nu=nu[2:]
                 else:                              # nu의 길이가 2일때는 슬라이싱 후 남는 문자열이 없으므로 break
                     break

     except:
         r = "Error!"
     return r