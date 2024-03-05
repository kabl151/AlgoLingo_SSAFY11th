# import math
# def to_degree(radian):
#     return radian * 180 / math.pi
# my_ball = (0, 0)    #   내 공 위치
# target_ball = (-1,-1)   # 넣을 공 위치
# distance = math.sqrt((target_ball[0] - my_ball[0]) ** 2 + (target_ball[1] - my_ball[1]) ** 2)
# power = max(10.0, distance * 2)

# width = target_ball[0] - my_ball[0]
# height = target_ball[1] - my_ball[1]
# theta = math.atan2(height, width)

# angle = to_degree(theta)
# degree = 90 - angle
# if degree < 0:
#     degree += 360

# print(power)

# print(degree)


# TODO : 4분면에 일타싸피에서 요구하는 각도로 값을 변경하기

#return power, degree   함수전달

import math

def to_degree(theta):
    angle = theta * 180 / math.pi
    degree = 90 - angle
    if degree < 0:
        degree += 360
    return degree

def to_power(distance):
    power = max(60, distance * 2)
    return power

my_ball = (0, 0)                # 주어지는 값
target_ball = (10, -3)          # 주어지는 값
width = target_ball[0] - my_ball[0]
height = target_ball[1] - my_ball[1]

distance = math.sqrt((width)**2 + (height)**2)
print(to_power(distance))
theta = math.atan2(height, width)
print(to_degree(theta))

