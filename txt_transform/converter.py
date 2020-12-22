# -*- coding:utf-8 -*-

import re
import textblob

# 만 단위 자릿수
tenThousandPos = 4
# 억 단위 자릿수
hundredMillionPos = 9
txtDigit = ['', '십', '백', '천', '만', '억']
txtNumber = ['영', '일', '이', '삼', '사', '오', '육', '칠', '팔', '구']
txtPoint = ' 점'
txtja = ['ㄱ', 'ㄴ', 'ㄷ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅅ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
txtja_pn = ['기역', '니은', '디귿', '리을', '미음', '비읍', '시옷', '이응', '지읒', '치읓', '키읔', '티읕', '피읖', '히읗']
txtEng = ['에이', '비', '씨', '디', '이', '에프', '지', '에이치', '아이', '제이', '케이', '엘', '엠', '엔', '오', '피', '큐', '알', '에스', '티',
          '유', '브이', '더블유', '엑스', '와이', '제트']
numEng = ['제로', '원', '투', '쓰리', '포', '파이브', '식스', '세븐', '에잇', '나인','텐']
numEngB20 = ['', '일레븐', '트웰브', '써틴', '포틴', '피프틴', '식스틴', '세븐틴', '에잇틴','나인틴']
numEngTen = ['','','투웬티','써티','포티','피프티','식스티','세븐티','에잇티','나인티']
numHan = ['영', '한', '두', '세', '네', '다섯', '여섯', '일곱', '여덟','아홉','열']
numHanTen = ['','','스물','서른','마흔','쉰','예순','일흔','여든','아흔']
dialect = ['요', '요게', '요렇게', '요거', '요건', '요런', '요거는', '요기', '고', '그', '고건', '고걸', '고렇게', '그죠', '그쵸','조렇게']
standard = ['이', '이게', '이렇게', '이거', '이건', '이런', '이거는', '여기', '그', '그', '그건', '그걸', '그렇게', '그렇죠', '그렇죠','저렇게']
gram = ['그램','그람','킬로그램','키로그램','키로그람','킬로그람']

def stcTrans(input):
    if ';' in input:
        stc = re.sub('[-=#:^$@\"※~&%ㆍ』\\‘|\(\)\[\]\<\>`…》]', '', input)
        txt_list = stc.split("'")
        for i in range(len(txt_list)):
            if txt_list[i].endswith(';'):
                txt_list[i] = combtxt(txt_list[i].replace(';',''))
        return ''.join(txt_list)
    else:
        return combtxt(input)

def combtxt(txt):
    input = txt.replace(' ','')
    conStr = ''
    engNumStr = ''
    hanNumStr = ''
    tmp = []

    for i in range(len(input)):
        if input in dialect:  # 구어체 처리
            conStr = standard[dialect.index(input)]

        elif input not in dialect:
            if input[i].isalpha() == True:
                if isHangul(input[i]) == False:    # 알파벳일 경우 띄어쓰기 포함
                    conStr += (txt2prun(str(input[i])).split('/')[1].strip('()') + ' ')
                    engNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()') + ' ')
                    hanNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()') + ' ')

                elif isHangul(input[i]) == True and input.isalpha() == False:  # 한글일 경우 띄어쓰기 없이 그대로
                    if (i != len(input) - 1):
                        if isHangul(input[i+1]) == False:
                            conStr += (txt2prun(str(input[i])).split('/')[1].strip('()')) + ' '
                            engNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()')) + ' '
                            hanNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()')) + ' '
                        else:
                            conStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))
                            engNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))
                            hanNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))
                    else:
                        conStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))
                        engNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))
                        hanNumStr += (txt2prun(str(input[i])).split('/')[1].strip('()'))

                elif (isHangul(input[i]) == True) and input.isalpha() == True:
                    return f"({kor2eng(input)})/({txt})"

            elif input[i].isalpha() == False:  # 숫자 하나씩만 인식되므로 뒤에 더 있을 경우까지 고려해야 함.
                tmp.append(input[i])
                if input[i] == ' ':
                    pass
                if (i == len(input) - 1) or input[i + 1].isalpha() == True: # 맨 끝에 도달 또는 뒤에 문자 오는 경우까지
                    conStr += (digit2txt(''.join(tmp)).split('/')[1].strip('()') + ' ')
                    if '.' not in input:  # 100 미만 정수일 경우만 영어, 한글 서수 발음 이중전사
                        if int(''.join(tmp)) >= 0 and int(''.join(tmp)) < 11:
                            engNumStr += numEng[int(''.join(tmp))] + ' '
                            hanNumStr += numHan[int(''.join(tmp))] + ' '
                        elif int(''.join(tmp)) >= 11 and int(''.join(tmp)) < 20:
                            engNumStr += numEngB20[int(''.join(tmp)) - 10] + ' '
                            hanNumStr += numHan[10] + ' ' + numHan[int(tmp[1])] + ' '
                        elif int(''.join(tmp)) >= 20 and int(''.join(tmp)) < 100:
                            if tmp[1] != '0':
                                engNumStr += numEngTen[int(tmp[0])] + ' ' + numEng[int(tmp[1])] + ' '
                                hanNumStr += numHanTen[int(tmp[0])] + ' ' + numHan[int(tmp[1])] + ' '
                            elif tmp[1] == '0':
                                engNumStr += numEngTen[int(tmp[0])] + ' '
                                hanNumStr += numHanTen[int(tmp[0])] + ' '

                        else:
                            engNumStr = '범위초과 '
                            hanNumStr = '범위초과 '
                    else:
                        engNumStr = '범위초과 '
                        hanNumStr = '범위초과 '
                    tmp = []
                else:
                    continue

    if '범위초과' not in engNumStr and input.isalpha() != True:
        return '({0})/({1}) \n({2})/({3}) \n({4})/({5})'.format(txt, conStr.strip(), txt, engNumStr.strip(), txt, hanNumStr.strip())

    else:
        if len(input) <= 5 and '.' in input and input.isalpha() == False \
                and (input[:input.index('.')].isdigit() == True
                     and int(input[:input.index('.')])<=12 and int(input[:input.index('.')])>=1) \
            and (input[input.index('.')+1:].isdigit() == True
                     and int(input[input.index('.')+1:]) <= 31 and int(input[input.index('.')+1:]) >= 1) :  # 한국사 기념일 경우 점 발음 없이 발음할 경우 고려
            return '({0})/({1}) \n({2})/({3})'.format(txt, conStr.replace(' 점 ',' ').strip(), txt, conStr.strip())

        elif input in dialect:
            return '({1})/({0})'.format(txt, conStr.strip())

        else:
            return '({0})/({1})'.format(txt, conStr.strip())


def isHangul(ch):  # 주어진 문자가 한글인지 아닌지 리턴해주는 함수
    jamo_start_letter = 44032
    jamo_end_letter = 55203
    return ord(ch) >= jamo_start_letter and ord(ch) <= jamo_end_letter

def kor2eng(kr): # 한국어 발음 입력 시 영어로 이중전사
    try:
        blob = textblob.TextBlob(kr)
        return str(blob.translate(to='en')).lower()
        #return kr
    except:
        if isHangul(kr) == True and kr in gram[:2]:
            return str('gram')
        elif isHangul(kr) == True and kr in gram[2:]:
            return str('kilogram')

def txt2prun(strNum):
    if strNum.isalpha() == True:
        if isHangul(strNum) == False:
            if strNum not in txtja:
                concatstr = ""
                for ch in strNum:
                    if ord('a') <= ord(ch) and ord(ch) <= ord('z'):
                        # index txtEnglish
                        concatstr += txtEng[ord(ch) - ord('a')] if len(concatstr) == 0 else ' ' + txtEng[
                            ord(ch) - ord('a')]

                    elif ord('A') <= ord(ch) and ord(ch) <= ord('Z'):
                        # index txtEnglish
                        concatstr += txtEng[ord(ch) - ord('A')] if len(concatstr) == 0 else ' ' + txtEng[
                            ord(ch) - ord('A')]

                return '({0})/({1})'.format(strNum, concatstr)

            # 강의 ㄱ, ㄴ, ㄷ 같은 보기 전사용
            elif strNum in txtja:
                prun = txtja_pn[txtja.index(strNum)]
                return '({0})/({1})'.format(strNum, prun)

        elif isHangul(strNum) == True:
            #if strNum not in dialect:
                return '({0})/({1})'.format(strNum, strNum)


def digit2txt(strNum):
    if strNum.isalpha() != True:
        resultStr = ''
        digitCount = 0
        # 자릿수 카운트
        for ch in strNum:
            # ',' 무시
            if ch == ',':
                continue
            # 소숫점 까지
            elif ch == '.':
                break
            digitCount = digitCount + 1

        digitCount = digitCount - 1
        index = 0

        while True:
            notShowDigit = False
            ch = strNum[index]
            # ',' 무시
            if ch == ',':
                index = index + 1
                if index >= len(strNum):
                    break;
                continue

            if ch == '.':
                resultStr = resultStr + txtPoint
            else:
                # 자릿수가 2자리이고 1이면 '일'은 표시 안함.
                # 단 '만' '억'에서는 표시 함
                if int(ch) == 1 and (digitCount >= 1) and (digitCount != tenThousandPos) and (
                        digitCount != hundredMillionPos):
                    resultStr = resultStr + ' '
                elif int(ch) == 0 and (len(strNum) > 1) and ('.' not in strNum):
                    resultStr = resultStr + ''
                    # 단 '만' '억'에서는 표시 함
                    if (digitCount != tenThousandPos) and (digitCount != hundredMillionPos):
                        notShowDigit = True
                elif int(ch) == 0 and ('.' in strNum) and (len(strNum[:strNum.index('.')]) > 1):
                    resultStr = resultStr + ''

                    # 단 '만' '억'에서는 표시 함
                    if (digitCount != tenThousandPos) and (digitCount != hundredMillionPos):
                        notShowDigit = True

                else:
                    resultStr = resultStr + ' ' + txtNumber[int(ch)]


            # 1억 이상
            if digitCount > hundredMillionPos:
                if not notShowDigit:
                    resultStr = resultStr + txtDigit[digitCount - hundredMillionPos]
            # 1만 이상
            elif digitCount > tenThousandPos:
                if not notShowDigit:
                    resultStr = resultStr + txtDigit[digitCount - tenThousandPos]
            else:
                if not notShowDigit:
                    resultStr = resultStr + txtDigit[digitCount]

            if digitCount <= 0:
                digitCount = 0
            else:
                digitCount = digitCount - 1
            index = index + 1
            if index >= len(strNum):
                break;

        return '({0})/({1})'.format(strNum, resultStr.strip())







