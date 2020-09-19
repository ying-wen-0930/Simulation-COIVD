'''
人的状态：
    0 未感染
    1 潜伏期
    2 确诊
    3 隔离（住院，会占用床位）
    4 免疫期
    5 死亡
'''

# 概率分布标准差
SCALE = 1

'''
parameters
'''

ACTION_RATE = 100 # worst case
SAFETY_AWARENESS = 0.01 # worst case


# ACTION_RATE = 0.01 # happy case
# SAFETY_AWARENESS = 100# happy case


BED_NUM = 2
INFECTION_NUM = 288
LATENT_TIME = 14
THEATMENT_TIME = 25
IMMUNE_TIME = 100
HOSPITAL_TIME = 14
SPREAD_RATE = 0.9
DEATH_RATE = 0.056
SECURITY_DIST = 6
CITY_PEOPLE_NUM = 8399
SCALE = 10000




'''
People 
'''
#     0 未感染
#     1 潜伏期
#     2 确诊
#     3 隔离（住院，会占用床位）
#     4 免疫期
#     5 死亡
UNINFECTED_STATUS = 0
LATENT_STATUS = 1
CONFIRMED_STATUS = 2
ISOLATION_STATUS = 3
IMMUNE_STATUS = 4
DEATH_STATUS = 5

'''
床位状态
'''
#     0 闲置
#     1 占用
IDLE_STATU = 0
OCCUPY_STATUS = 1


'''
医院相关
'''



'''
画布相关
'''
# 画布的起点
CANVAS_INIT = (0, 0)

# 人在不同状态对应的颜色
PEOPLE_COLORS = [
    'black', # 未感染
    'orange', # 潜伏期
    'red',  # 确诊
    'blue', # 隔离
    'green', # 免疫期
    'grey', # 死亡
    'blue', # 绘制隔离曲线
    'black', # 绘制死亡曲线
    'orange', # 绘制死亡曲线
]

# 医院床位不同状态的颜色
BED_COLORS = [
    'green', # 空床
    'red', # 有人
]