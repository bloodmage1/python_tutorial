# 객체(object)

# = 속성  + 행위


# 사람
# - 이름 키 나이 생년월일
# - 행동, 행위


students = [
    {"name":"a", "korean":40 , "math": 50, "english": 60},
    {"name":"b", "korean":41 , "math": 57, "english": 69},
    {"name":"c", "korean":44 , "math": 58, "english": 68},
    {"name":"d", "korean":46 , "math": 53, "english": 65},
    {"name":"e", "korean":42 , "math": 51, "english": 63},
]


def 학생_생성(name, korean, math, english):
    return {"name" : name,
            "korean": korean,
            "math": math,
            "english": english}

students = [
    학생_생성("a", 40, 50, 60),
    학생_생성("b", 41, 57, 69),
    학생_생성("c", 44, 58, 68),
    학생_생성("d", 46, 53, 65),
    학생_생성("e", 42, 51, 63),
]


def 총점(student):
    return student["korean"] + student["math"] + student["english"]
def 평균(student):
    return 총점(student) / 4
def 출력(student):
    print(student["name"], 총점(student), 평균(student), sep = "\t")


print("이름", "총점", "평균", sep = "\t")

for student in students:
    score_sum = student["korean"] + student["math"] + student["english"]
    
    score_average = score_sum / 4
    
    print(student["name"], score_sum, score_average, sep = "\t")



# 여기서 score의 총합과 평균을 구하는 부분, print 하는 부분이 행위에 해당한다.
