# 5.1 리스트
# 5.1.1 리스트형(1)

# 변수에 여러 값을 대입할 수 있는 리스트(list형) 변수
# 리스트형은 수치, 문자열 등의 데이터를 한꺼번에 저장할 수 있는 자료형
# [요소1, 요소2, ...] 와 같이 기술한다
# 또한 리스트에 저장되어 있는 값 하나하나를 요소 또는 객체(object)라고 한다
# 다른 프로그래밍 언어 비유하자면 '배열'과 유사하다

# 문제
c = ["red", "blue", "yellow"]
print(c)  # ['red', 'blue', 'yellow']
print(type(c))  # <class 'list'>

# 5.1.2 리스트형(2)
# 리스트형에는 다른 자료형이 섞여 있어도 괜찮고, 변수를 리스트  안에 저장할 수도 있다
n = 3
print(["사과", n, "고릴라"])  # ['사과', 3, '고릴라']

# 문제
apple = 4
grape = 3
banana = 6

fruits = [apple, grape, banana]
print(fruits)  # [4, 3, 6]

# 5.1.3 리스트 안의 리스트
# 리스트 요소로 리스트형을 저장할 수 있다
# 즉, 중첩된 구조를 만들 수 있다
print([[1, 2], [3, 4], [5, 6]])  # [[1, 2], [3, 4], [5, 6]]

# 문제
fruits_name_1 = "apple"
fruits_num_1 = 2
fruits_name_2 = "orange"
fruits_num_2 = 10

fruits = [[fruits_name_1, fruits_num_1], [fruits_name_2, fruits_num_2]]
print(fruits)  # [['apple', 2], ['orange', 10]]

# 5.1.4 리스트에서 값 추출
# 리스트의 요소는 차례대로 0, 1, 2, 3, ... 이라는 번호가 할당되어 있으며, 이를 인덱스 번호라고 한다
# 인덱스는 0부터 시작하는 것에 주의!
# 리스트 요소는 뒤에서부터 순서대로 번호를 지정할 수도 있다
# 가장 마지막 요소는 -1번째, 끝에서 2번째는 -2번째
# 리스트의 각 요소는 '리스트[인덱스번호]'로 검색할 수 있다

a = [1, 2, 3, 4]
print(a[1])  # 2
print(a[-2])  # 3

# 문제
fruits = ["apple", 2, "orange", 4, "grape", 3, "banana", 1]
print(fruits[1])  # 2
print(fruits[-1])  # 1

# 5.1.5 리스트에서 리스트 추출(슬라이스)
# 리스트에서 새로운 리스트를 추출할 수도 있는데, 이르르 "슬라이스, slice" 라고 한다
# 작성법 : 리스트[start:end]
# 인덱스 번호 start부터 end-1까지의 리스트를 추출한다

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
print(alphabet[1:5])  # ['b', 'c', 'd', 'e']
print(alphabet[1:-5])  # ['b', 'c', 'd', 'e']
print(alphabet[:5])  # ['a', 'b', 'c', 'd', 'e']
print(alphabet[6:])  # ['g', 'h', 'i', 'j']
print(alphabet[:])  # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

# 문제
chaos = ["cat", "apple", 2, "orange", 4,
         "grape", 3, "banana", 1, "elephant", "dog"]
fruits = chaos[1:-2]
print(fruits)  # ['apple', 2, 'orange', 4, 'grape', 3, 'banana', 1]


# 5.1.6 리스트 요소 갱신 및 추가
# 리스트 요소(객체)를 갱신하거나 추가할 수 있다
# '리스트[인덱스 번호] = 값'을 사용하면 지정한 인덱스 번호의 요소를 갱신할 수 있다
# 슬라이스 값을 통해 값을 갱신할 수도 있다
#
#  리스트에 요소를 추가하고 싶은 경우 리스트와 리스트를 '+'을 사용하여 연결한다
# 여러 요소를 동시에 추가하는 것도 가능하다
# '리스트명.append(추가할 요소)'로 추가할 수도 있다
# append() 메서드를 사용할 경우 여러 요소를 동시에 추가할 수 있따

alphabet = ["a", "b", "c", "d", "e"]
alphabet[0] = "A"
alphabet[1:3] = ["B", "C"]
print(alphabet)  # ['A', 'B', 'C', 'd', 'e']

alphabet = alphabet + ["f"]
alphabet += ["g", "h"]
alphabet.append("i")
print(alphabet)  # ['A', 'B', 'C', 'd', 'e', 'f', 'g', 'h', 'i']

# 문제
c = ["dog", "blue", "yellow"]
c[0] = "red"
c.append("green")
print(c)  # ['red', 'blue', 'yellow', 'green']

# 5.1.7 리스트 요소 삭제
# 리스트 요소 방법 : 'del 리스트[인덱스 번호]'
# 인덱스 번호를 슬라이스로 지정할 수도 있다

alphabet = ["a", "b", "c", "d", "e"]
del alphabet[3:]
del alphabet[0]
print(alphabet)  # ['b', 'c']

# 문제
c = ["dog", "blue", "yellow"]
del c[0]
print(c)  # ['blue', 'yellow']

# 5.1.9 리스트형 주의점

alphabet = ["a", "b", "c"]
alphabet_copy = alphabet
alphabet_copy[0] = "A"
print(alphabet)  # ['A', 'b', 'c']

# 위처럼 리스트 변수를 다른 변수에 대입한 뒤 대입한 변수에서 값을 바꾸면 원래 변수의 값도 바뀐다
# 이를 막기 위해서는 y = x 대신 y = x[:] 또는 y = list(x) 이런 식으로 사용하면 된다
alphabet = ["a", "b", "c"]
alphabet_copy = alphabet[:]
# alphabet_copy = list(alphabet)
alphabet_copy[0] = "A"
print(alphabet)  # ['a', 'b', 'c']

# 문제
c = ["red", "blue", "yellow"]
c_copy = list(c)
c_copy[1] = "green"
print(c)  # ['red', 'blue', 'yellow']
