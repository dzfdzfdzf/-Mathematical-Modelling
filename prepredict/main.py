import os
import numpy as np
from datetime import *

def gethour(s):
    time = datetime.strptime(s,"%H:%M:%S")
    return time.hour


def GetCross(x1,y1,x2,y2,x,y):
    a=(x2-x1,y2-y1)
    b=(x-x1,y-y1)
    return a[0]*b[1]-a[1]*b[0]
def isInSide(x1,y1,x2,y2,x3,y3,x4,y4,x,y):
    return GetCross(x1,y1,x2,y2,x,y)*GetCross(x3,y3,x4,y4,x,y)>=0 and GetCross(x2,y2,x3,y3,x,y)*GetCross(x4,y4,x1,y1,x,y)>=0

def cal(inflie):
    f=open(inflie,'r')
    lis=[0,0,0,0,0,0,0,0]
    for line in f:
        line=line.strip()
        time=line.split(" ")[1]
        longitude = float(line.split(" ")[3])
        latitude = float(line.split(" ")[4])
        #if isInSide(114.289882,30.55773,114.290062,30.558227,114.299296,30.552629,114.299655,30.552909,longitude,latitude):
        #if isInSide(114.27811,30.55444,114.27832,30.55488,114.28747,30.54934,114.28772,30.54982,longitude,latitude):
        if isInSide(114.28354, 30.55238, 114.28341, 30.55218, 114.29277, 30.54731, 114.29265, 30.54711,longitude, latitude):
            hour=gethour(time)
            id=hour//3
            if lis[id]==0:
                lis[id]+=1
    return lis

if __name__== "__main__":
    inputdir_path="C:\\Users\\asus\\Desktop\\t3"
    filelist=os.listdir(inputdir_path)
    ans=[]
    for name in filelist:
        inputdir_path2=os.path.join(inputdir_path,name)
        filelist2=os.listdir(inputdir_path2)
        res=[0, 0, 0, 0, 0, 0, 0, 0]
        for name2 in filelist2:
            file_name=os.path.join(inputdir_path2,name2)
            temp=cal(file_name)
            res = np.sum([res, temp], axis=0).tolist()
        ans.append(res)
    print(ans)


