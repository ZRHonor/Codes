# author = ZRHonor
# 超像素分割 局部生长算法
# 输入依次为：灰度图像，生长起始点，检测阈值
import numpy as np

def regionGrowing(grayImg,seed,threshold):
    """ 超像素分割 局部生长算法
        输入依次为：灰度图像，生长起始点，检测阈值
        输出为{0,255}的二值图像"""
    [maxX, maxY] = grayImg.shape[0:2]

    # 用于保存生长点的队列
    pointQueue = []
    pointQueue.append((seed[0], seed[1]))
    outImg = np.zeros_like(grayImg)
    outImg[seed[0], seed[1]] = 255

    pointsNum = 1
    pointsMean = float(grayImg[seed[0], seed[1]])

    # 用于计算生长点周围八个点的位置
    NextEight = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

    while(len(pointQueue)>0):
        # 取出队首并删除
        growSeed = pointQueue[0]
        del pointQueue[0]

        for differ in NextEight:
            growPointx = growSeed[0] + differ[0]
            growPointy = growSeed[1] + differ[1]

            # 是否是边缘点
            if((growPointx < 0) or (growPointx > maxX - 1) or 
			   (growPointy < 0) or (growPointy > maxY - 1)):
                continue

            # 是否已经被生长
            if(outImg[growPointx,growPointy] == 255):
                continue

            data = grayImg[growPointx,growPointy]
            # 判断条件
			# 符合条件则生长，并且加入到生长点队列中
            if(abs(data - pointsMean)<threshold):
                pointsNum += 1
                pointsMean = (pointsMean * (pointsNum - 1) + data) / pointsNum
                outImg[growPointx, growPointy] = 255
                pointQueue.append([growPointx, growPointy])

    return outImg
