
import numpy as np
import cv2 as cv2
from scipy import interpolate
import matplotlib.pyplot as plt
from math import atan2
import os


# mouse callback function
x_input = []
y_input = []
points_list = []
count = 0
img = np.zeros((512, 512, 3), np.uint8)


def draw_circle(event, x, y, flags, param):
    global points_list, count, img
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # points_list[count]=[x,y]
        if (len(x_input) == 0 or max(x_input) < x):
            x_input.append(x)
            y_input.append(y)

            # points_list.append([x,y])
            cv2.circle(img, (x, y), 10, (255, 0, 0), -1)
        # count+=1

    # if event == cv2.EVENT_MBUTTONDOWN:
    #     del points_list[count-1]
    #     count -=1
    # cv.circle(img,(x,y),10,(0,0,0),-1)

    # cv2.circle(img,points_list[count-1],10,(255,0,0),-1)


def fit():
    x = np.array(x_input)

    y = np.array(y_input)

    tck = interpolate.splrep(x, y, s=0)
    xfit = np.arange(x[0], x[-1], np.pi / 50)
    yfit = interpolate.splev(xfit, tck, der=0)

    for i in range(len(xfit)):
        cv2.circle(img, (int(xfit[i]), int(yfit[i])), 3, (0, 0, 255), -1)

    cv2.imshow('img', img)
    cv2.waitKey(0)

    return xfit, yfit



def euclidean_dst(x1, x2, y1, y2):
    return np.sqrt(np.square(x1 - x2) + np.square(y1 - y2))


def get_arcLength(xfit, yfit):
    length = 0
    for i in range(len(xfit) - 1):
        length += euclidean_dst(xfit[i], xfit[i + 1], yfit[i], yfit[i + 1])
    return length


def get_motion_path(xfit, yfit, thetas, vel, fps, pix_2_m):
    assert vel != 0
    motion_path = {}
    length = get_arcLength(xfit, yfit)
    curr_length = 0
    keyframe_count = 0
    time_for_1_m = length // vel
    # l =100
    # v =5

    for i in range(len(xfit) - 1):
        curr_length += euclidean_dst(xfit[i], xfit[i + 1], yfit[i], yfit[i + 1]) * pix_2_m
        if curr_length >= vel:
            motion_path[keyframe_count * fps] = [xfit[i] * pix_2_m, yfit[i] * pix_2_m, thetas[i]]
            curr_length = 0
            keyframe_count += 1

    return motion_path


def get_orientation(xfit, yfit):
    thetas = []
    theta = atan2(yfit[0], xfit[0])
    thetas.append(theta)
    for i in range(1, len(xfit) - 3):
        img_copy = img.copy()

        theta = atan2((yfit[i + 3] - yfit[i]), (xfit[i + 3] - xfit[i]))
        thetas.append(theta)
        # cv2.arrowedLine(img_copy,(int(xfit[i]),int(yfit[i])),(int(xfit[i]+20*np.cos(theta)),int(yfit[i]+20*np.sin(theta))),(0,255,0),3)
        # cv2.imshow('img',img_copy)
        # cv2.waitKey(1)

    return thetas


def write_motion_path(motion_path):
    """
    assumption - z, r, p are constant [MIGHT CHANGE IN FUTURE]
    dict
    key - frame number
    value - [(x, y, z), (r, p, yaw)]

    file - frame_number, x, y, z, r, p, yaw
    """
    if os.path.exists("motion_path_2.txt"):
        os.remove("motion_path_2.txt")

    f = open("motion_path_2.txt", "w")
    r = 1.57
    p = 0
    z = 3.5
    for key in motion_path.keys():
        val = motion_path[key]
        f.write(str(key) + ","+str(val[0])+","+str(val[1])+","+str(z)+","+str(r)+","+str(p)+","+str(val[2]))
        f.write('\n')
    f.close()


def generate_motion_path(motion_path_file):
    """
    reads motion path file and returns dictionary for blender
    """
    f = open(motion_path_file, "r")
    motion_path_dict = {}
    for d in f.readlines():
        data = d.split(',')
        frame_number = int(data[0])
        x = float(data[1])
        y = float(data[2])
        z = float(data[3])
        roll = float(data[4])
        pitch = float(data[5])
        yaw = float(data[6])
        motion_path_dict[frame_number] = [(x, y, z), (roll, pitch, yaw)]

    return motion_path_dict


def main():
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw_circle)
    while 1:
        cv2.imshow('image', img)
        if cv2.waitKey(20) & 0xFF == 27:
            break
    cv2.destroyAllWindows()
    # print(points_list)

    xfit, yfit = fit()
    thetas = get_orientation(xfit, yfit)
    pix_2_m = 0.1
    vel = 5  # m/s
    motion_path = get_motion_path(xfit, yfit, thetas, vel=vel, fps=30, pix_2_m=pix_2_m)

    write_motion_path(motion_path)
    print(motion_path)


if __name__ == "__main__":
    main()