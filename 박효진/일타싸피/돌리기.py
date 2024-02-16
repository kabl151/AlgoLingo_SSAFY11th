# # atan2(높이,너비)
# import math
# def to_degree(radian):
#     return radian * 180 / math.pi
# my_ball = (0, 0)
# target_ball = (2, 1)    # 45
# target_ball = (1, 0)    # 90
# target_ball = (1, -2)   # 135
# target_ball = (0, -2)    # 180
# target_ball = (-2, -1)  # 225
# target_ball = (-1, 0)   # 270
# target_ball = (-1, 1)   # 315
# target_ball = (0, 1)    # 360

# distance = math.sqrt((target_ball[0] - my_ball[0]) ** 2 + (target_ball[1] - my_ball[1]) ** 2)

# # 각도계산
# width = target_ball[0] - my_ball[0]
# height = target_ball[1] - my_ball[1]
# theta = math.atan2(height, width)
# print('라디안', theta)    # radian 각도 => degree 각도로 변환
#                 # 라디안(Θ) : 각도(χ) = 2π : 360˚
#                 # χ * 2π = Θ * 360˚
#                 # χ = Θ * 360˚ / 2π = Θ * 180˚ / π
# degree = to_degree(theta)
# if degree == 90:            # 위 조정
#     degree += 90
# elif 0 < degree < 90:       # 1사분면 조정
#     degree = 90 - degree
# elif degree == 0:           # 오른쪽 조정
#     degree += 90
# elif -90 < degree < 0:      # 4사분면 조정
#     degree -= 90
#     degree = -degree
# elif degree == -90:         # 아래 조정
#     degree -= 90
#     degree = -degree
# elif -180 < degree < -90:   # 3사분면 조정
#     degree -= 90
#     degree = -degree
# elif degree == 180:         # 왼쪽 조정
#     degree += 90
# elif 90 < degree < 180:     # 2사분면 조정
#     degree = 90 - degree
#     degree = degree + 360

# print('각도', degree)

# # TODO : 4분면에 일타싸피에서 요구하는 각도로 값을 변경하기

# #return power, degree   함수전달


import math

def calculate_angle(my_ball, target_ball):
    
    # 각도 계산
    width = target_ball[0] - my_ball[0]
    height = target_ball[1] - my_ball[1]
    theta = math.atan2(height, width)
    degree = math.degrees(theta)
    
    # 원점을 기준으로 보정
    angle = 90 - degree    #<<<<<<<<<<<<<<< 사실상 보정 부분은 여기 뿐인듯???
    if angle < 0:          #<<<<<<<<<<<<<<<
        angle += 360       #<<<<<<<<<<<<<<<
    
    return angle

my_ball = (0, 0)
target_balls = [(1, 3), (2, 2), (3, 1), (4, 0), (3, -1), (2, -2), (1, -3), (0, -4), (-1, -3), (-2, -2), (-3, -1), (-4, 0), (-3, 1), (-2, 2), (-1, 3), (0, 4)]
target_ball = (10, 10) # 파워 예시
# c(두 공사이의 간격) = sqrt(a ** 2 + b ** 2)
distance = math.sqrt((target_ball[0] - my_ball[0] ** 2 + (target_ball[1] - my_ball[1]) ** 2))
power = max(10.0, distance * 2) # 0~100 (권장 파워는 10 이상, 100이상넘길수있지만 100으로고정)

for target_ball in target_balls:
    angle = calculate_angle(my_ball, target_ball)
    print(f"Target Ball: {target_ball}, Angle: {angle}")
    print(power)