# -*- coding: utf-8 -*-
#import hangulize

tenThousandPos = 4
hundredMillionPos = 9
txtDigit = ['', '십', '백', '천', '만', '억']
txtNumber = ['', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = ' 점 '
txtEnglish = ['에이','비','씨','디','이','에프','지','에이치','아이','제이','케이','엘','엠','엔','오','피','큐','알','에스','티','유','브이','더블유','엑스','와이','제트']


#def texttrans(input):
    #resultStr = ''

def is_digit(input):
    try:
        tmp = float(input)
        return True
    except ValueError:
        return False


def digit2txt(input):
    resultStr = ''
    digitCount = 0
    #자릿수 카운트
    
    ## input 이라는 것을 순환 하면서 숫자는 숫자로 영어는 영어로
    if input.isalpha() == True:
        concatstr = ""
        for ch in input:

            if ord('a') <= ord(ch) and  ord(ch) <= ord('z'):
                # index txtEnglish
                concatstr += txtEnglish[ord(ch) - ord('a')] if len(concatstr) == 0 else ' ' + txtEnglish[ord(ch) - ord('a')]
            
            elif ord('A') <= ord(ch) and  ord(ch) <= ord('Z'):
                # index txtEnglish
                concatstr += txtEnglish[ord(ch) - ord('A')] if len(concatstr) == 0 else ' ' + txtEnglish[ord(ch) - ord('A')]
       
        return '({0})/({1})'.format(input, concatstr)

        
        
    # elif input.isdigit() == True:
    #         return '문자 숫자 혼용으로 변환 불가'


    # (5대)/(오 대)
    #elif input[-1].isalpha() == True:


    #TODO : 여기 밑에서는 오직 숫자만 잇을 때 들어가도록 구현
   
   # elif input.isalpha() != True:
    elif is_digit(input) == True:
        resultStr = ''
        digitCount = 0

        #자릿수 카운트
        for ch in input:
            # ',' 무시
            # if (ord(ch)>=33 and ord(ch)<=47) or (ord(ch)>=58 and ord(ch)<=64) or(ord(ch)>=91 and ord(ch)<=96) or (ord(ch)>=123 and ord(ch)<=126):
            #     return input + '특수문자가 포함되어 변환 불가!'
            #     continue
            #
            # if ord('a') <= ord(ch) and  ord(ch) <= ord('z'):
            #     return input + '숫자 문자 혼합 불가!'
            # elif ord('A') <= ord(ch) and  ord(ch) <= ord('Z'):
            #     return input + '숫자 문자 혼합 불가!'

            digitCount = digitCount + 1
            
        # isfirstZero = False
        # if input[0] =='0' :
        #     isfirstZero = True
            
                
        digitCount = digitCount-1
        index = 0
        
        if len(input) >= hundredMillionPos:
            return '억단위 이상은 직접 입력하세요.'
    
        new_input = ''
        while True:
            notShowDigit = False
            ch = input[index]
            #print(str(index) + ' ' + ch + ' ' +str(digitCount))
            # ',' 무시
            if ch == ',':
                index = index + 1
                if index >= len(input):
                    break;
                continue

            if ch == '.':
                resultStr = resultStr + txtPoint
            else:
                #자릿수가 2자리이고 1이면 '일'은 표시 안함.
                # 단 '만' '억'에서는 표시 함
                if(digitCount >= 1) and (digitCount != tenThousandPos) and int(ch) == 1:
                    resultStr = resultStr + ' '
                elif int(ch) == 0:
                    resultStr = resultStr + ''
                    # 단 '만' '억'에서는 표시 함
                    if (digitCount != tenThousandPos) and (digitCount != hundredMillionPos):
                        notShowDigit = True
                else:
                    resultStr = resultStr + ' ' + txtNumber[int(ch)]


           # if isfirstZero == False :
                # 1억 이상
                if digitCount > hundredMillionPos:
                    if not notShowDigit:
                        resultStr = resultStr + txtDigit[digitCount-hundredMillionPos]
                # 1만 이상
                elif digitCount > tenThousandPos:
                    if not notShowDigit:
                        resultStr = resultStr + txtDigit[digitCount-tenThousandPos]
                else:
                    if not notShowDigit:
                        resultStr = resultStr + txtDigit[digitCount]

            if digitCount <= 0:
                digitCount = 0
            else:
                digitCount = digitCount - 1
            index = index + 1
            if index >= len(input):
                break;
        return '({0})/({1})'.format(input, resultStr.strip())

    #elif is_digit(input) == True

        