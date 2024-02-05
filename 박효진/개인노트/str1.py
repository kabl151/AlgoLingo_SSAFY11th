def itoa(i):
    '''
    parpam i : 변환할 정수값
    return str: 해당되는 문자열
    '''
    # 빈 문자열의 변수
    result = []
    
    # 몫이 0이 될 때까지 반복!
    while i != 0:
        digit = i % 10  # 첫째자리 수, 4
        i = i // 10 # 첫째자리 수를 뺀 나머지 자릿수, 123
        
        '''
        - digit를 해당되는 문자로 변환
        - 아스키코드를 변환하는 두 가지 함수 => chr(), ord()
            1. chr() : 아스키코드 값 -> 문자
            2. ord() : 문자 -> 아스키코드 값
    
        '0'에 해당되는 아스키코드값? => ord('0') => 48
        정수형 문자 0~9 -> 아스키코드 값 '0'~'9'
        ord('0') + digit
        '''
        
        s_digit = chr(ord('0') + digit)
        result.append(s_digit)
        
        
        # result ?? ['4', '3', '2', '1']
        # 문자열을 역순으로 반환
    return ''.join(result[::-1])
    
i = 1234
string = itoa(i)
print(string)
#--------------------------------------------------위에 윤하코드 아래 강사님 코드
def itoa(i):
    """
    :param i: 변환할 정수값
    :return: str 해당되는 문자열
    """
    # 빈문자열의 변수
    # result = ''
    # 비어있는 리스트
    result = []
    # 몫이 0이 될때까지 반복!
    while i != 0:
        digit = i % 10  # 첫째자리 수, 4
        i = i // 10  # 첫째자리 수를 뺀 나머지 자릿수, 123
        s_digit = chr(ord('0') + digit)
        result.append(s_digit)

    # result ?? ['4','3','2','1']
    # 문자열을 역순으로 반환...!
    return ''.join(result[::-1])


number = 1234
string = itoa(number)
print(string)
print(type(string))
    
    
