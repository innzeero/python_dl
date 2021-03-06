# 4.3 자료형
# 4.3.1 자료형의 종류
# 파이썬의 값은 형(자료형, data type)이라는 개념이 있다.
# 자료형은 문자열형(str형), 정수형(int형), 부동소수점형(float형), 리스트형(list형) 등이 있다.

# 다른 형끼리의 계산이나 연결을 시도하면 에러가 발생하는 경우가 있다.
# height = 177
# print("신장은 " + height + "cm입니다.")
# TypeError: can only concatenate str (not "int") to str
# height 변수는 int형인데 연결하려는 것은 str형이라 에러 발생!

# 변수의 자료형 조사 방법
# type()을 사용한다.
height = 177
print(type(height))  # <class 'int'>

# 문제
h = 1.7
w = 60

print(type(h))  # <class 'float'>
print(type(w))  # <class 'int'>

bmi = w / h**2
print(bmi)  # 20.761245674740486
print(type(bmi))  # <class 'float'>

# 자료형의 변환
# 서로 다른 자료형을 계산하거나 결합하려면 형을 변환하여 같은 형으로 만들어야 한다.
# 정수형으로 변환하려면 int()
# 소수점을 포함한 수치형으로 변환하려면 float()
# 문자열로 변환하려면 str()
# 소수점을 포함한 수치형을 부동소수점형(float형)이라 한다.

# NOTE #
# 부동소수점의 '부동'은 부호, 지수, 가수로 소수점을 나타내는 컴퓨터 특유의 표시 방법이다.
# 프로그래밍 실무에서 소수점을 포함하는 숫자는 대부분 float 형이다.

h = 177
print("신장은 " + str(h) + "cm입니다.")  # 신장은 177cm입니다.

# 부동소수점형과 정수형은 엄밀하게는 다른 형이지만 둘 다 수치를 취급하는 형이다.
# 그러므로 위처럼 형 변환을 하지 않아도 부동소수점과 정수형을 혼합한 계산이 가능하다.
a = 35.4
b = 10
print(a+b)  # 45.4

# 문제
print("당신의 bmi는 " + str(bmi) + "입니다.")
# 당신의 bmi는 20.761245674740486입니다.


# 4.3.3 자료형의 이해와 확인
# 프로그래밍에서 자료형은 매우 중요하다.
# 정리하자면 결국 다른 자료형끼리는 결합할 수 없고, 문자열로 저장된 수치는 계산할 수 없다는 것이다.
greeting = "hi!"
print(greeting * 2)  # hi!hi!
