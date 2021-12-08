import json
import numpy as np
import cv2
import matplotlib.pyplot as plt
f = open("annotation-json\\annotation_test_2.json")
data = json.load(f)



for k in data.keys():

    filename = data[k]['filename']
    gt_lanes = data[k]['regions']
    img = plt.imread(filename)
    height, width, channel = img.shape

    #!Get all co-ordinates
    gt_lanes_vis = []
    for lane in gt_lanes:
        x_cor = lane['shape_attributes']['all_points_x']
        y_cor = lane['shape_attributes']['all_points_y']
        gt_lanes_vis.append([(x, y) for (x, y) in zip(x_cor, y_cor)])

    img_vis = img.copy()
    #!Marking the exact co-ordinates
    for lane in gt_lanes_vis:
        for pt in lane:
            cv2.circle(img_vis, pt, radius=5, color=(255, 255, 255))

    img_vis = img.copy()
    #!Drawing polylines on top of the image
    for lane in gt_lanes_vis:
        cv2.polylines(img_vis, np.int32(
            [lane]), isClosed=False, color=(0, 255, 0), thickness=5)
    plt.imshow(img_vis)
    cv2.imwrite('main.png', img_vis)
    # plt.show()

    #!Generating gt image
    gray_level = 0
    gray_image = gray_level * np.ones((height, width, 3), dtype=np.uint8)
    for lane in gt_lanes_vis:
        cv2.polylines(gray_image, np.int32(
            [lane]), isClosed=False, color=(255, 255, 255), thickness=5)
    plt.imshow(gray_image)
    cv2.imwrite('gt.png', gray_image)
    # plt.show()

    break
