# 5.2 딕셔너리

# 5.2.1 딕셔너리형
# 딕셔너리형은 리스트형처럼 여러 데이터를 다룰 때 사용한다
# 리스트형과 다른 점은 인덱스 번호로 요소를 꺼내는 방식이 아니라 키(key)와 값(value) 쌍으로 연결되어 있어
# 키를 통해 연결되어 있는 값을 얻는다
# 작성방법 : {키1: 값1, 키2: 값2, ...}
# 문자열의 경우 ""로 감싸준다

dic = {"Korea": "Seoul", "France": "Paris"}
print(dic)  # {'Korea': 'Seoul', 'France': 'Paris'}

# 문제
town = {"Gyeongido": "Anyang", "Seoul": "Mapogu"}
print(town)
print(type(town))
# {'Gyeongido': 'Anyang', 'Seoul': 'Mapogu'}
# <class 'dict'>

# 5.2.2 딕셔너리 요소 추출
# 딕셔너리 요소를 추출할 때는 '딕셔너리명["키"]'라고 작성한다
dic = {"Korea": "Seoul", "France": "Paris"}
print(dic["Korea"])  # Seoul

# 문제
town = {"경기도": "수원", "서울": "중구"}
print("경기도의 중심 도시는 " + town["경기도"] + "입니다.")
print("서울의 중심 도시는 " + town["서울"] + "입니다.")
# 경기도의 중심 도시는 수원입니다.
# 서울의 중심 도시는 중구입니다.

# 5.2.3 딕셔너리 갱신 및 추가
# 딕셔너리 값을 갱신할 때는 '딕셔너리명["값을 갱신할 키"] = 값' 이라고 쓰고
# 딕셔너리에 요소를 추가할 때는 '딕셔너리명["추가할 키" = 값]' 이라고 쓴다

dic = {"Korea": "Seoul", "France": "Paris"}
dic["Korea"] = "Gyeongju"
dic["Italy"] = "Rome"

print(dic)  # {'Korea': 'Gyeongju', 'France': 'Paris', 'Italy': 'Rome'}

# 문제
town = {"경기도": "수원", "서울": "중구"}
town["제주도"] = "제주시"
town["경기도"] = "분당"

print(town)  # {'경기도': '분당', '서울': '중구', '제주도': '제주시'}

# 5.2.4 딕셔너리 요소 삭제
# 딕셔너리 값을 삭제 방법 : 'del 딕셔너리명["삭제할 키"]'
dic = {'Korea': 'Gyeongju', 'France': 'Paris', 'Italy': 'Rome'}
del dic["Italy"]
print(dic)  # {'Korea': 'Gyeongju', 'France': 'Paris'}

# 문제
town = {'경기도': '분당', '서울': '중구', '제주도': '제주시'}
del town["경기도"]
print(town)  # {'서울': '중구', '제주도': '제주시'}
