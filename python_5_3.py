# 5.3 while문

# 5.3.1 while(1)
# while문을 이용하면 주어진 조건식이 False가 될 때까지 처리를 반복(루프, loop) 할 수 있다
# while 조건식: ...
# 조건식이 True인 동안 while문의 처리가 반복된다
# 또한 while문의 처리는 if문과 같이 들여쓰기를 해서 루프할 곳을 지정한다

n = 2
while n > 0:
    print(n)
    n -= 1
# 2
# 1

x = 5
while x > 0:
    print("test")
    x -= 2
# test
# test
# test

# 5.3.2 while(2)
# 조건식의 변숫값을 갱신하지 않거나 조건식이 항상 성립되도록 하면 루프가 무한 반복된다
# 무한루프가 발생하지 않도록 주의!

# 문제
# while문을 사용하여 변수 x가 0이 아닌 동안 반복하도록 만들어라
# 반복문 안에서는 변수 x에서 1을 빼고, x값을 출력하라
# 다음처럼 실행 결과가 나오도록 만들어라
# 4
# 3
# 2
# 1
# 0

x = 5
while x != 0:  # x != 0 이 Fasle가 되면 while문은 멈춘다, 즉 x == 0일 경우 while문은 멈춘다
    x -= 1
    print(x)
# 4
# 3
# 2
# 1
# 0

# 5.3.3 while & if
# 문제
# 위의 문제에서 작성한 코드를 if문을 사용하여 다음과 같이 출력되도록 수정
# 4
# 3
# 2
# 1
# Bang

x = 5
while x != 0:
    x -= 1
    if x != 0:
        print(x)
    else:
        print("Bang")
