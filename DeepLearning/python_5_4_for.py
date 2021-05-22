# 5.4 for문

# 5.4.1 for문
# 리스트의 요소를 모두 출력하고 싶을 때 자주 사용하는 것이 for문이다
# 'for 변수 in 데이터셋:' 이라고 작성하면 데이터셋의 요소 수만큼 처리를 반복할 수 있다

# 데이터셋, dataset은 리스트형이나 딕셔너리형처럼 복수의 요소를 가진 것을 말한다

animals = ["tiger", "dog", "bear"]
for animal in animals:
    print(animal)
    
# tiger
# dog 
# bear

# 문제
storages = [1, 2, 3, 4]

for s in storages:
    print(s)


# 5.4.2 break
# break을 이용해서 반복 처리를 종료할 수도 있다

storages = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for s in storages:
    print(s)
    if s >= 5 :
        print("The End")
        break

# 문제
storages = [1, 2, 3, 4, 5, 6]

for s in storages:
    print(s)
    if s == 4 :
        break

# 5.4.3 continue
# continue는 break과 마찬가지로 if문 등과 조합해서 사용
# but break와는 달리 특정 조건일 때 loop를 한 번 건너뛴다

storages = [1, 2, 3]
for s in storages:
    if s == 2:
        continue
    print(s)

# 1
# 3

# 문제
nums = [1, 2, 3, 4, 5, 6]

for n in nums:
    if n % 2 == 0 :
        continue
    print(n)


# 5.5 추가
# 5.5.1 for문에서 index 표시
# for문을 사용한 루프에서 리스트의 index 확인이 필요할 때가 있다
# enumerate() 함수를 사용하면 인덱스가 포함된 요소를 얻을 수 있다
# 형식은 다음과 같다
# for x, y in enumerate("list 형"):
# for 안에서는 x, y를 사용하여 작성, x는 정수형의 인덱스, y는 리스트에 포함된 요소(값)이다
# x, y는 just 변수 이름 a, b or index, value or i, v 등등 자유롭게 이름을 붙일 수 있다

al = ["a", "b"]
for i, v in enumerate(al):
    print(i, v)

# 0 a
# 1 b

# 문제
animals = ["tiger", "dog", "elephant"]

for i, v in enumerate(animals):
    print("index:%d %s" % (i, v))

# 또다른 출력방법
for index, animal in enumerate(animals):
    print("index:" + str(index), animal)


# 5.5.2 리스트 안의 리스트 루프
# 리스트의 요소가 리스트형일 경우 그 내용을 for문을 사용해 꺼낼 수 있다
# g형식 : for a, b, c, ... in 변수(리스트형)
# a, b, c, ...의 개수는 리스트의 요소수와 가아야 한다

mylist = [[1, 2, 3], [4, 5, 6]]

for a, b, c in mylist:
    print(a, b, c)

# 1 2 3
# 4 5 6 

# 문제
# for문을 사용하여 다음을 출력하는 코드를 작성하라
# strawberry is red
# peach is pink
# banana is yellow

fruits = [["strawberry", "red"], ["peach", "pinik"], ["banana", "yellow"]]

for f, c in fruits:
    print("%s is %s" % (f, c))

# strawberry is red
# peach is pinik
# banana is yellow

# 또다른 출력방법
for fruit, color in fruits:
    print(fruit + " is " + color)


# 5.5.3 딕셔너리형 루프
# 딕셔너리형 루프에서는 키와 값을 모두 변수로 하여 반복할 수 있다
# items()를 사용하여 'for key의변수명, value의 변수명 in 변수(딕셔너리형).items():'로 작성

fruits = {"strawbeery" : "red", "peach" : "pink", "banana" : "yellow"}

for fruit, color in fruits.items():
    print(fruit + " is " + color)


# 문제
town = {"경기도" : "분당","서울" : "중구", "제주도" :"제주시"}

for p, c in town.items():
    print(p, c)


# 문제
items = {"지우개" : [100, 2], "펜" : [200, 3], "노트" : [400, 5]}

total_price = 0

for item in items :
    print(item +"은(는) 한 개에 " + str(items[item][0]) + "원이며, " + str(items[item][1]) + "개 구합니다.")
    total_price += items[item][0] * items[item][1]

print("지불해야 할 금액은 " + str(total_price) + "원입니다.")

money = int(input())

if money > total_price :
    print("거스름돈은 %d원입니다." % (money-total_price))
elif money == total_price:
    print("거스름돈은 없습니다.")
else :
    print("돈이 부족합니다datetime A combination of a date and a time. Attributes: ()")