# encoding: utf-8
import matplotlib.pyplot as plt

img = plt.imread('./data_source/rose.jpg')  # img.shape  # 高、宽度、颜色


def show_img(im, color="red"):
    if color == "blue":
        im = img[:, :, ::-1]
    elif color == "green":
        im = img[:, :, [1, 0, 2]]
    plt.imshow(im)


def main():
    show_img(im=img, color="blue")


if __name__ == '__main__':
    main()
