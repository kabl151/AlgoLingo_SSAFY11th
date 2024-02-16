# atan2(높이,너비)
import math
def to_degree(radian):
    return radian * 180 / math.pi
my_ball = (0, 0)
# target_ball = (2, 1)    # 45
# target_ball = (1, 0)    # 90
# target_ball = (1, -2)   # 135
target_ball = (0, 2)    # 180
# target_ball = (-2, -1)  # 225
# target_ball = (-1, 0)   # 270
# target_ball = (-1, 1)   # 315
# target_ball = (0, 1)    # 360

distance = math.sqrt((target_ball[0] - my_ball[0]) ** 2 + (target_ball[1] - my_ball[1]) ** 2)

# 각도계산
width = target_ball[0] - my_ball[0]
height = target_ball[1] - my_ball[1]
theta = math.atan2(height, width)
print('라디안', theta)    # radian 각도 => degree 각도로 변환
                # 라디안(Θ) : 각도(χ) = 2π : 360˚
                # χ * 2π = Θ * 360˚
                # χ = Θ * 360˚ / 2π = Θ * 180˚ / π
degree = to_degree(theta)
if degree == 90:            # 0도일 때 조정
    degree += 90
elif 0 < degree < 90:       # 1사분면 조정
    degree = 90 - degree
elif degree == 0:           # 90도일때 조정
    degree += 90
elif -90 < degree < 0:      # 4사분면 조정
    degree -= 90
    degree = -degree
elif -180 < degree < -90:   # 3사분면 조정
    degree -= 90
    degree = -degree
# elif degree == -90:         # 180도일때 조정

print('각도', degree)

# TODO : 4분면에 일타싸피에서 요구하는 각도로 값을 변경하기

#return power, degree   함수전달