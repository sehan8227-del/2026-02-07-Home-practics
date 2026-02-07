#2일차 반복훈련 A-06 복습
person = {"name": "공욱재", "age": 26}
result = "name" in person
print(result)

person = {"name": "이세한", "age": 32}
result = "name" in person
print(result)

#전에 연습했던 person 이라는 변수에 맞는 딕셔너리를 만들고 딕셔리 안의 내용인 person 변수 안의 딕셔너리의 내용 중 "name"이 존재 하면 true을 출력하는 방식이였지? 실험했을 시 "age"를 넣어보고 "hobby"를 넣어봤는데 age는 내용이 있으니 true , "hobby"는 내용안에 없으니 Flase가 출력 되었지.

#2일차 반복 훈련 A-07시작

person = {"name": "공욱재", "age": 26, "nickname": "공미남"}
del person["nickname"]
print(person)

person = {"name": "이세한", "age": 32, "nickname": "이세팟"}
del person["nickname"]
print(person)

#person의 변수 중 딕셔너리 안 nickname을 del을 이용하여 삭제 시키는 거군 그러면 혹시 변수 안에 저장되어 있다가 del로 내부 로직을 강제적으로 잘라낼수도 있으려나 ?궁금하네

person = {"name": "이세한", "age": 32, "nickname": "이세팟"}
del person["nickname"]#["age"]
print(person) #맞다 딕셔너리 하나당 내용 하나만 불러올 수 있었지

person = {"name": "이세한", "age": 32, "nickname": "이세팟"}
del person["age"]
print(person)

person = {"name": "이세한", "age": 32, "nickname": "이세팟"}
del person["name"]
print(person)

person = {"name": "이세한", "age": 32, "nickname": "이세팟"}
del person["nickname"]
print(person)

person = {"name": "이세한", "age": 32,"nickname": "이세팟", "hobby": "노래부르기"}
del person["hobby"]
print(person)

person = {"name": "이세한", "age": 32, "nickname": "이세팟", "hobby": "노래부르기"}
del person["nickname"]
print(person)

