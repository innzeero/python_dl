# 6.2.1 함수 작성
# 함수는 프로그램의 여러 처리를 하나로 정리한 것이다
# 정확하게는 인수를 받아 처리한 결과를 반환값으로 돌려준다
# 함수를 사용하면 전체적인 동작이 알기 쉬워지고, 동일한 처리를 여러 번 작성하지 않아도 되는 장점이 있다

# 함수의 작성법은 'def 함수명(인수):' 이다
# 인수는 함수에 전달하려는 값이다
# 인수가 비어 있는 경우도 있다
# 함수의 처리 범위는 들여쓰기로 나타낸다

# 함수를 호출할 때는 '함수명()'을 사용한다
# 함수는 정의한 후에만! 호출할 수 있다

# 다음은 인수가 없는 간단한 함수이다
# 함수 작성법과 호출 방힉을 확인해보자
def sing():
    print("노래하자!")

sing()

# 문제
def intro():
    print("아이엠그라운드 자기소개하기")

intro()

# 6.2.2 인수
# 함수에 전달하는 값을 '인수'라고 한다
# 함수는 그 인수를 받아서 그 값을 사용한다
# 'def 함수명(인수):' 처럼 인수를 지정한다
# '함수명(인수)'로 함수를 호출할 때 전달된 인수(값)가 인수로 지정한 변수에 대입되기 때문에
# 인수를 바꾸는 것만으로! 출력 내용을 변경할 수 있다!
# 인수와 함수에 정의된 변수는 그 함수 내에서만 사용할 수 있다는 것에 주의!

# 다음은 인수가 하나인 함수이다
# 함수 작성법과 호출 방식을 확인하자

def introduce(n):
    print(n + "입니다.")

introduce("라이언")

# 문제
# 인수 n을 세제곱한 값을 출력하는 함수 cube_cal 작성

def cube_cal(n):
    print(n**3)

cube_cal(4)

# 6.2.3 여러 개의 인수
# 여러 개의 인수를 전달하려면 () 안에 쉼표로 구분하여 지정한다
# 다음은 인수 2개를 지정한 함수이다
# 함수 작성법과 호출 방식을 확인하자

# 여러 인수의 예
def introduce_1(first, second):
    print("성은 " + first + "이고, " + "이름은 " + second + "입니다.")

introduce_1("은", "봉희")

# 문제
def introduce_2(n, age):
    print(n + "입니다. " + str(age) + "살입니다.")

introduce_2("홍길동", 18)


# 6.2.4 인수의 초깃값
# 인수에 초깃값을 설정할 수 있다
# 초깃값을 설정하면 '함수명(인수)'로 호출시 인수를 생략하면 초깃값이 사용된다
# 초깃값을 설정하려면 () 안에 '인수=초깃값이라고 적으면 된다

# 인수의 초깃값 예(1)
def introduce_3(first="김", second="길동"):
    print("성은 " + first + "이고, 이름은 " + second + "입니다.")

introduce_3("홍")