from matplotlib.patches import Ellipse, Circle
import matplotlib.pyplot as plt
import pandas as pd
import os
import shutil
import math

if os.path.exists('./plot'):
    shutil.rmtree('./plot')
os.mkdir('./plot')

RAD2DEG = 57.29577951308232     # 弧度与角度换算关系1弧度=57.29..角度

# original big circle small circle-----------
# OBSTACLE_POS = [[24.5, 13.5], [22.8, 79.3], [41.4, 32.5], [26.4, 53.3], [70.5, 85.3], [89.2, 70.5], [78.2, 24.5], [69.4, 54.3]]
# OBSTACLE_RADIUS = [5, 8, 9.5, 2.5, 5, 4, 4.5, 6.5]
# original big circle small circle-----------

# random small circle-----------
# OBSTACLE_POS = [[12.4, 42.5], [24.5, 13.5], [20.8, 89.3], [71.2, 39.2], [29.8, 56.5], [40.4, 36.3], [70.5, 85.3], [56.4, 68.2], [89.2, 70.5], [83.2, 24.5]]
# OBSTACLE_RADIUS = [2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5, 2.5]
# random small circle-----------

# Big circle one empty-----------
BIG_RAD = 14
OBSTACLE_POS = []
for a in range(10):
    OBSTACLE_POS.append([50 + BIG_RAD * math.cos(math.pi / 6 * a), 50 + BIG_RAD * math.sin(math.pi / 6 * a)])
OBSTACLE_RADIUS = [2.5 for a in range(10)]
# Big circle one empty-----------

# narrow-----------
# OBSTACLE_POS = [[24.5, 13.5], [22.8, 79.3], [39.9, 32.5], [26.4, 53.3], [64.5, 85.3], [79.2, 67.5], [74.2, 24.5], [63.4, 45.3]]
# OBSTACLE_RADIUS = [5, 8, 9.5, 7.5, 5, 9.5, 5.5, 7.5]
# narrow-----------

for ff in os.listdir('./rlt'):
    cur_file = os.path.join('./rlt', ff)
    data = pd.read_csv(cur_file, sep=',',header=None)

    fig = plt.figure()
    
    ax = fig.add_subplot(111)

    for i in range(0, len(data), 2):
        cir1 = Circle(xy = [data.iloc[i, 0], data.iloc[i,1]], radius=2.5, facecolor= [160 / 255, 191 / 255, 124 / 255], alpha=0.25)
        ax.add_patch(cir1)
    
    for i in range(0, len(data), 8):
        end_x = data.iloc[i, 0] + 2.5 * math.cos(data.iloc[i, 4])
        end_y = data.iloc[i, 1] + 2.5 * math.sin(data.iloc[i, 4])
        # ax.annotate('', xy=[data.iloc[i, 0], data.iloc[i,1]], xytext=[end_x, end_y], arrowprops=dict(arrowstyle = "->", color=[160 / 255, 191 / 255, 124 / 255]))
        ax.annotate('', xy=[end_x, end_y], xytext=[data.iloc[i, 0], data.iloc[i,1]], arrowprops=dict(arrowstyle = "->", color=[160 / 255, 191 / 255, 124 / 255]))


    # ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
    for op, rd in zip(OBSTACLE_POS, OBSTACLE_RADIUS):
        # cir1 = Circle(xy = op, radius=2.5, facecolor= [160 / 255, 191 / 255, 124 / 255], alpha=0.3)
        cir1 = Circle(xy = op, radius=rd, facecolor= [224 / 255, 160 / 255, 158 / 255], alpha=0.9)
        ax.add_patch(cir1)

    plt.axis('scaled')
    plt.xlim((0,100))
    plt.ylim((0,100))
    # plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

    # plt.show()
    
    plt.savefig('./plot/{}.jpg'.format(ff))


    

# data = pd.read_csv('rlt/aa.save_info', sep=',',header=None)

# fig = plt.figure()
# ax = fig.add_subplot(111)

# for i in range(0, len(data), 2):
#     cir1 = Circle(xy = [data.iloc[i, 0], data.iloc[i,1]], radius=2.5, facecolor= [160 / 255, 191 / 255, 124 / 255], alpha=0.25)
#     ax.add_patch(cir1)

# for i in range(0, len(data), 8):
#     end_x = data.iloc[i, 0] + 2.5 * math.cos(data.iloc[i, 4])
#     end_y = data.iloc[i, 1] + 2.5 * math.sin(data.iloc[i, 4])
#     ax.annotate('', xy=[data.iloc[i, 0], data.iloc[i,1]], xytext=[end_x, end_y], arrowprops=dict(arrowstyle = "->", color=[160 / 255, 191 / 255, 124 / 255]))


# # ell1 = Ellipse(xy = (0.0, 0.0), width = 4, height = 8, angle = 30.0, facecolor= 'yellow', alpha=0.3)
# for op, rd in zip(OBSTACLE_POS, OBSTACLE_RADIUS):
#     # cir1 = Circle(xy = op, radius=2.5, facecolor= [160 / 255, 191 / 255, 124 / 255], alpha=0.3)
#     cir1 = Circle(xy = op, radius=rd, facecolor= [224 / 255, 160 / 255, 158 / 255], alpha=0.9)
#     ax.add_patch(cir1)

# plt.axis('scaled')

# plt.axis('equal')   #changes limits of x or y axis so that equal increments of x and y have the same length

# # plt.show()

# plt.savefig('./plot/aa.jpg')

    
 


