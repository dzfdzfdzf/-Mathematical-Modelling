import math
from math import radians, cos, sin, asin, sqrt
import os
import matplotlib.pyplot as plt


def distanceCalculate(x1, y1, x2, y2):
    x1, y1, x2, y2 = map(radians, [float(x1), float(y1), float(x2), float(y2)])
    dx = x2 - x1
    dy = y2 - y1
    a = sin(dy / 2) ** 2 + cos(y1) * cos(y2) * sin(dx / 2) ** 2
    c = 2 * asin(sqrt(a))
    r = 6371
    return c * r * 1000


def Geodist(point1, point2):
    return distanceCalculate(point1[1], point1[2], point2[1], point2[2])


def get_vertical_dist(pointA, pointB, pointX):
    a = math.fabs(Geodist(pointA, pointB))
    if a == 0:
        return math.fabs(Geodist(pointA, pointX))
    b = math.fabs(Geodist(pointA, pointX))
    c = math.fabs(Geodist(pointB, pointX))
    p = (a + b + c) / 2
    S = math.sqrt(math.fabs(p * (p - a) * (p - b) * (p - c)))
    vertical_dist = S * 2 / a
    return vertical_dist


def DP_compress(point_list, output_point_list, Dmax):
    start_index = 0
    end_index = len(point_list) - 1
    output_point_list.append(point_list[start_index])
    output_point_list.append(point_list[end_index])

    if start_index < end_index:
        index = start_index + 1
        max_vertical_dist = 0
        key_point_index = 0

        while (index < end_index):
            cur_vertical_dist = get_vertical_dist(point_list[start_index], point_list[end_index], point_list[index])
            if cur_vertical_dist > max_vertical_dist:
                max_vertical_dist = cur_vertical_dist
                key_point_index = index
            index += 1

        if max_vertical_dist >= Dmax:
            DP_compress(point_list[start_index:key_point_index], output_point_list, Dmax)
            DP_compress(point_list[key_point_index:end_index], output_point_list, Dmax)


def cal_Err(point_list, output_point_list):
    Err = 0

    start_index = 0
    end_index = len(output_point_list) - 1

    while (start_index < end_index):
        pointA_id = int(output_point_list[start_index][0])
        pointB_id = int(output_point_list[start_index + 1][0])

        id = pointA_id + 1
        while (id < pointB_id):
            Err += get_vertical_dist(output_point_list[start_index], output_point_list[start_index + 1], point_list[id])
            id += 1

        start_index += 1

    return Err


def work(infile, outfile, Dmax):
    point_list = []
    output_point_list = []

    fd = open(infile, 'r')
    id = 0
    for line in fd:
        line = line.strip()
        id += 1
        longitude = float(line.split(" ")[3])
        latitude = float(line.split(" ")[4])
        point_list.append((id, longitude, latitude))
    fd.close()

    DP_compress(point_list, output_point_list, Dmax)

    output_point_list = list(set(output_point_list))
    output_point_list = sorted(output_point_list, key=lambda x: x[0])
    fd = open(outfile, 'w')
    for point in output_point_list:
        fd.write("{},{},{}\n".format(point[0], point[1], point[2]))
    fd.close()

    # print("compression rate={}/{}={}".format(len(point_list), len(output_point_list),
    # len(output_point_list) / len(point_list)))
    return len(point_list), len(output_point_list), cal_Err(point_list, output_point_list)


if __name__ == '__main__':
    inputdir_path = 'C:\\Users\\asus\\Desktop\\loss'
    outputdir_path = 'C:\\Users\\asus\\Desktop\\dp'
    fileList = os.listdir(inputdir_path)
    rate = []
    error = []
    d = list(range(1, 21))
    compression_rate = 0
    mean_error = 0
    total_input = 0
    total_output = 0
    total_error = 0
    for name in fileList:
        inputfileTxt = os.path.join(inputdir_path, name)
        outfileTxt = os.path.join(outputdir_path, name)
        res = work(inputfileTxt, outfileTxt, 20)
        total_input += res[0]
        total_output += res[1]
        total_error += res[2]
    compression_rate = total_output / total_input
    mean_error = total_error / total_input
    print(total_input, total_output, compression_rate, mean_error)
    # print(total_output)
    # print(total_error)
    # print(compression_rate)
    # print(mean_error)
    # rate.append(compression_rate)
    # error.append(mean_error)
    # f = open('C:\\Users\\asus\\Desktop\\rate2.txt', 'w')
    # for i in rate:
    #     f.write(str(i))
    #     f.write(",")
    #     f.write('\n')
    # f.close()
    # f2 = open('C:\\Users\\asus\\Desktop\\error2.txt', 'w')
    # for i in error:
    #     f2.write(str(i))
    #     f2.write(",")
    #     f2.write('\n')
    # f2.close()
    # fig=plt.figure(1)
    # ax1=plt.subplot(1,2,1)
    # plt.plot(d,rate)
    # ax2=plt.subplot(1,2,2)
    # plt.plot(d,error)
