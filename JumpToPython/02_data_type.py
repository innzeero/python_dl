# 02-1 숫자형
# 숫자형(Number)이란 숫자 형태로 이뤄진 자료형

# - 정수형 : 123, /178, 0
# - 실수형 : 2.1459, -1.5982, 4.26E10, 5.26e-10
# - 8진수(Octal) : 0o288 (0o or 0O 로 시작)
# - 16진수(Hexadecimal) : 0x8ff (0x로 시작)

# 연산자
# 사칙연산 (+, -, *, /)
# 제곱 : **
# 나머지 반환 : %
# 몫 반환 : //

# 02-2 문자열 자료형
# 문자열(string)이란 문자, 단어 등으로 구성된 문자들의 집합
# "Hello World" 
# 'Hello World"
# """Hello world"""
# '''Hello world'''

# food = "Python's favorite food is perl" (O)
# food = 'Python's favorite food is perl' (X, SyntaxError)
# say = '"Python is very easy." he says' (O)
# say = ""Python is very easy." he says" (X, SyntaxError)

# ' or " 를 문자열에 포함시키는 방법 : \사용하기
# ex) \', \" 이렇게 앞에 \를 삽입하면 ' or "는 문자열을 둘러싸는 기호의 의미가 아니라 문자 그 자체를 뜻하게 된다

# 여러 줄인 문자열을 변수에 대입
# 1) 줄을 바꾸기 위한 이스케이프 코드 \n 삽입
multiline1 = "Life is too short\nYou need python"
print(multiline1)\
# 위 방법은 읽기에 불편하고 줄이 길어지는 단점이 있다

# 2) ''' or """ 사용하기
multiline2 = '''
Life is too short
You need python
'''
print(multiline2)

# 이스케이프 코드란?
# 이스케이프 코드란 프로그래밍할 때 사용할 수 있도록 미리 정의해둔 "문자 조합"
# 주로 출력물을 보기 좋게 정렬하는 용도로 사용
# 자주 사용하는 것들
# \n, \t(문자열 사이에 탭 간겨게을 줄 때 사용)
# \\, \', \"

# 문자열 연산
# 문자열 더해서 연결하기(Concatenation)
head = "Python"
tail = " is fun!"
print(head+tail)

# 문자열 곱하기
title = "python"
print(title*2)

print('='*50)
print('My Program')
print('='*50)

# 문자열 길이 구하기
loc = "In the Cafe"
print(len(loc))

# 문자열 인덱싱과 슬라이싱
# indexing이란 무언가를 "가리킨다"는 의미
# slicing은 무언가를 "잘라낸다"는 의미

# 문자열 인덱싱이란?
n = "Nice to meet you"
print(n[3]) # e
# "파이썬은 0부터 숫자를 센다!!"
print(n[-1]) # u 끝에서 첫번째

print(n[0]) # N
print(n[-0]) # N

# 문자열 슬라이싱이란?
print(n[0:4]) # Nice [시작번호:끝번호]에서 끝번호에 해당하는 것은 포함하지 않음

print(n[:]) # Nice to meet you
print(n[-3:]) # you

# 슬라이싱으로 문자열 나누기
# 자주 사용하는 슬라이싱 기법 중 하나
today = "20020717Sunny"
date = today[:8]
weather = today[8:]
print(date) # 20020717
print(weather) # Sunny

# 'Pithon' 이라는 문자열을 'Python'으로 바꾸려면?
word = 'Pithon'
# word[1] = 'y'
# print(word) -> Error
# why? 문자열의 요솟값은 바꿀 수 없다
# 문자열 자료형은 그 요솟값을 변경할 수 없다, 그래서 immutable(불변의)한 자료형이라고도 부른다
# 하지만 슬라이싱 기법을 사용하면 Python으로 변경 가능하다
new_word = word[:1] + 'y' + word[2:]
print(new_word) # Python

# 문자열 Formatting
# 1. 숫자 바로 대입
print("I eat %d apples." % 3)

# 2. 문자열 바로 대입
print("I eat %s apples" % "five")

# 3. 숫자값을 나타내는 변수로 대입
number = 3
print("I eat %d apples." % number)

# 2개 이상의 값 대입
number = 10
day = "three"
print("I ate %d apples. So I was sick for %s days" % (number, day))

# 문자열 포맷 코드
# %s(문자열, string), %c(문자 1개, charcater)
# %d(정수형, integer), %f(부동소수, floating-point)
# %o(8진수), %x(16진수), %%(Literal %, 문자 % 그 자체)

# %s 코드의 특이한 점은 어떠한 형태의 값이든 변환해 넣을 수 있다
print("I have %s apples" % 3)
print("Rate is %s" % 99.9)
# 정수형이면 %d, 부동소수형이면 %f를 사용해야 하지만
# %s는 자동으로 뒤에 있는 값을 문자열로 바꾸기 때문에 그런 것을 생각하지 않아도 된다

# 다음은 어떻게 출력될까?
# print("Error is %d%." % 98) # ValueError: incomplete format
# Error 발생 이유는 문자열 포맷 코드인 %d와 %가 같은 문자열 안에 존재하는 경우
# %를 나타내려면 반드시 %%로 써야하는 법칙이 있기 때문이다
# 하지만 문자열 안에 %d와 같은 formatting 연산자가 없으면 홀로 쓰여도 상관 없다
# 위를 제대로 출력하려면 다음과 같이 하면 된다
print("Error is %d%%" % 98)

# 포맷 코드와 숫자 함께 사용하기
