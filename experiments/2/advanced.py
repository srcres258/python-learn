import turtle as tt
from bs4 import BeautifulSoup
import argparse
import numpy as np
import cv2
import os
from typing import Generator, Any, Tuple
import tkinter as tk


# 贝塞尔函数（英文：Bézier function，后文略）的取样次数。
WRITE_STEP = 15

# 界面宽度。
WIDTH = 600

# 界面高度。
HEIGHT = 600

# 记录前一个贝塞尔函数的句柄。
XH = 0
YH = 0

# 用于转换 SVG 数据时记录放缩因子。
SCALE = (1, 1)

# 是否首次调用 SVG 数据处理过程。
FIRST = True

# 记录绘制过程中要处理多少种颜色。
K = 32

# 是否禁用绘制动画。
DISABLE_ANIMATION = False


def bezier(p1: float, p2: float, t: float) -> float:
    """
    一阶贝塞尔函数。
    :param p1:
    :param p2:
    :param t:
    :return:
    """

    return p1 * (1 - t) + p2 * t


def bezier_2(
        x1: float, y1: float,
        x2: float, y2: float,
        x3: float, y3: float
) -> None:
    """
    二阶贝塞尔函数。
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x3:
    :param y3:
    :return:
    """

    tt.goto(x1, y1)
    tt.pd()
    for t in range(0, WRITE_STEP + 1):
        x = bezier(bezier(x1, x2, t / WRITE_STEP),
                   bezier(x2, x3, t / WRITE_STEP),
                   t / WRITE_STEP)
        y = bezier(bezier(y1, y2, t / WRITE_STEP),
                   bezier(y2, y3, t / WRITE_STEP),
                   t / WRITE_STEP)
        tt.goto(x, y)
    tt.pu()


def bezier_3(
        x1: float, y1: float,
        x2: float, y2: float,
        x3: float, y3: float,
        x4: float, y4: float
) -> None:
    """
    三阶贝塞尔函数。
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x3:
    :param y3:
    :param x4:
    :param y4:
    :return:
    """

    # 坐标变换
    x1 = -WIDTH / 2 + x1
    y1 = HEIGHT / 2 - y1
    x2 = -WIDTH / 2 + x2
    y2 = HEIGHT / 2 - y2
    x3 = -WIDTH / 2 + x3
    y3 = HEIGHT / 2 - y3
    x4 = -WIDTH / 2 + x4
    y4 = HEIGHT / 2 - y4

    tt.goto(x1, y1)
    tt.pd()
    for t in range(0, WRITE_STEP + 1):
        x = bezier(bezier(bezier(x1, x2, t / WRITE_STEP),
                          bezier(x2, x3, t / WRITE_STEP),
                          t / WRITE_STEP),
                   bezier(bezier(x2, x3, t / WRITE_STEP),
                          bezier(x3, x4, t / WRITE_STEP),
                          t / WRITE_STEP),
                   t / WRITE_STEP)
        y = bezier(bezier(bezier(y1, y2, t / WRITE_STEP),
                          bezier(y2, y3, t / WRITE_STEP),
                          t / WRITE_STEP),
                   bezier(bezier(y2, y3, t / WRITE_STEP),
                          bezier(y3, y4, t / WRITE_STEP),
                          t / WRITE_STEP),
                   t / WRITE_STEP)
        tt.goto(x, y)
    tt.pu()


def move_to(x: float, y: float) -> None:
    """
    移动到 SVG 坐标下（x，y）。
    :param x:
    :param y:
    :return:
    """

    tt.pu()
    tt.goto(-WIDTH / 2 + x, HEIGHT / 2 - y)
    tt.pd()


def move_to_r(dx: float, dy: float) -> None:
    """
    移动到 SVG 当前相对坐标下（dx，dy）。
    :param dx:
    :param dy:
    :return:
    """

    tt.pu()
    tt.goto(tt.xcor() + dx, tt.ycor() - dy)
    tt.pd()


def line(x1: float, y1: float, x2: float, y2: float) -> None:
    """
    连接 SVG 坐标下两点。
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :return:
    """

    tt.pu()
    tt.goto(-WIDTH / 2 + x1, HEIGHT / 2 - y1)
    tt.pd()
    tt.goto(-WIDTH / 2 + x2, HEIGHT / 2 - y2)
    tt.pu()


def line_to_r(dx: float, dy: float) -> None:
    """
    连接当前点和相对坐标（dx，dy）的点。
    :param dx:
    :param dy:
    :return:
    """

    tt.pd()
    tt.goto(tt.xcor() + dx, tt.ycor() - dy)
    tt.pu()


def line_to(x: float, y: float) -> None:
    """
    连接当前点和 SVG 坐标下（x，y）的点。
    :param x:
    :param y:
    :return:
    """

    tt.pd()
    tt.goto(-WIDTH / 2 + x, HEIGHT / 2 - y)
    tt.pu()


def curve_to(
        x1: float, y1: float,
        x2: float, y2: float,
        x: float, y: float
) -> None:
    """
    三阶贝塞尔曲线到（x，y）。
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x:
    :param y:
    :return:
    """

    global XH, YH

    tt.pu()
    x_now = tt.xcor() + WIDTH / 2
    y_now = HEIGHT / 2 - tt.ycor()
    bezier_3(x_now, y_now, x1, y1, x2, y2, x, y)
    XH = x - x2
    YH = y - y2


def curve_to_r(
        x1: float, y1: float,
        x2: float, y2: float,
        x: float, y: float
) -> None:
    """
    # 三阶贝塞尔曲线到相对坐标（x，y）。
    :param x1:
    :param y1:
    :param x2:
    :param y2:
    :param x:
    :param y:
    :return:
    """

    global XH, YH

    tt.pu()
    x_now = tt.xcor() + WIDTH / 2
    y_now = HEIGHT / 2 - tt.ycor()
    bezier_3(x_now, y_now, x_now + x1, y_now + y1, x_now + x2, y_now + y2, x_now + x, y_now + y)
    XH = x - x2
    YH = y - y2


def transform(w_attr: str) -> None:
    global SCALE

    funcs = w_attr.split(' ')
    for func in funcs:
        func_name = func[0:func.find('(')]
        if func_name == 'scale':
            SCALE = (float(func[func.find('(') + 1:-1].split(',')[0]),
                     -float(func[func.find('(') + 1:-1].split(',')[1]))


def read_path_attr_d(w_attr: str) -> Generator[float, Any, None]:
    ulist = w_attr.split(' ')
    for i in ulist:
        if len(i) == 0:
            continue
        elif i.isdigit() or i.isalpha():
            yield float(i)
        elif i[0].isalpha():
            yield i[0]
            yield float(i[1:])
        elif i[-1].isalpha():
            yield float(i[0:-1])
        elif i[0] == '-':
            yield float(i)


def draw_svg(filename: str, w_color: str) -> None:
    global FIRST

    with open(filename, 'r') as svg_file:
        svg = BeautifulSoup(svg_file.read(), 'lxml')
        height = float(svg.svg.attrs['height'][0:-2])
        width = float(svg.svg.attrs['width'][0:-2])
        transform(svg.g.attrs['transform'])
        if FIRST:
            tt.setup(height=height, width=width)
            tt.setworldcoordinates(-width / 2, 300, width / 2, -height + 300)
            tt.mode("world")
            FIRST = False
        if DISABLE_ANIMATION:
            tt.tracer(False)
            tt.speed(0)
            tt.delay(0)
        else:
            tt.speed("fast")
            tt.tracer(n=100, delay=10)
        tt.pensize(1)
        tt.pu()
        tt.color(w_color)
        tt.shape("turtle")

        for i in svg.find_all('path'):
            attr = i.attrs['d'].replace('\n', ' ')
            f = read_path_attr_d(attr)
            last_j = ''
            for j in f:
                match j:
                    case 'M':
                        tt.end_fill()
                        move_to(next(f) * SCALE[0], next(f) * SCALE[1])
                        tt.begin_fill()
                    case 'm':
                        tt.end_fill()
                        move_to_r(next(f) * SCALE[0], next(f) * SCALE[1])
                        tt.begin_fill()
                    case 'C':
                        curve_to(next(f) * SCALE[0], next(f) * SCALE[1],
                                 next(f) * SCALE[0], next(f) * SCALE[1],
                                 next(f) * SCALE[0], next(f) * SCALE[1])
                        last_j = j
                    case 'c':
                        curve_to_r(next(f) * SCALE[0], next(f) * SCALE[1],
                                   next(f) * SCALE[0], next(f) * SCALE[1],
                                   next(f) * SCALE[0], next(f) * SCALE[1])
                        last_j = j
                    case 'L':
                        line_to(next(f) * SCALE[0], next(f) * SCALE[1])
                    case 'l':
                        line_to_r(next(f) * SCALE[0], next(f) * SCALE[1])
                        last_j = j
                    case _:
                        match last_j:
                            case 'C':
                                curve_to(j * SCALE[0], next(f) * SCALE[1],
                                         next(f) * SCALE[0], next(f) * SCALE[1],
                                         next(f) * SCALE[0], next(f) * SCALE[1])
                            case 'c':
                                curve_to_r(j * SCALE[0], next(f) * SCALE[1],
                                           next(f) * SCALE[0], next(f) * SCALE[1],
                                           next(f) * SCALE[0], next(f) * SCALE[1])
                            case 'L':
                                line_to(j * SCALE[0], next(f) * SCALE[1])
                            case 'l':
                                line_to_r(j * SCALE[0], next(f) * SCALE[1])
            tt.pu()
            tt.update()


def draw_bitmap(w_image: cv2.typing.MatLike) -> None:
    print('Reducing the colors...')
    z = w_image.reshape((-1, 3))

    # convert to np.float32
    z = np.float32(z)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
    print('begin kmeans')
    ret, label, center = cv2.kmeans(z, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    print('end kmeans')

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    res = center[label.flatten()]
    res = res.reshape(w_image.shape)
    no = 0
    if os.path.exists('./.tmp.bmp'):
        os.remove('./.tmp.bmp')
    if os.path.exists('./.tmp.svg'):
        os.remove('./.tmp.svg')
    for i in center:
        print('Drawing: %.2f%% ' % (
                no / K * 100) + f'({no}/{K}) [' + '#' * no + ' ' * (K - no) + ']')
        no += 1
        res2 = cv2.inRange(res, i, i)
        res2 = cv2.bitwise_not(res2)
        cv2.imwrite('.tmp.bmp', res2)
        os.system('potrace .tmp.bmp -s --flat -o .tmp.svg')
        try:
            draw_svg('.tmp.svg', '#%02x%02x%02x' % (i[2], i[1], i[0]))
        finally:
            os.remove('.tmp.bmp')
            os.remove('.tmp.svg')
    tt.hideturtle()
    print('\nFinished, close the window to exit.')
    tt.done()


def get_screen_size() -> Tuple[int, int]:
    """
    获取屏幕的宽度和高度。
    :return:
    """

    root = tk.Tk()
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    root.destroy()
    return width, height


def main() -> None:
    global K, DISABLE_ANIMATION

    parser = argparse.ArgumentParser(description='Convert an bitmap to SVG and use turtle libray to draw it.')
    parser.add_argument('filename', type=str,
                        help='The file(*.jpg, *.png, *.bmp) name of the file you want to convert.')
    parser.add_argument('-c', '--color',
                        help='How many colors you want to draw.(If the number is too large that the program may be very slow.)',
                        type=int, default=32)
    parser.add_argument('--no-anim',
                        help='Set to 1 to disable drawing animation.',
                        type=int, default=0)
    args = parser.parse_args()
    K = args.color
    if hasattr(args, 'no_anim') and args.no_anim == 1:
        DISABLE_ANIMATION = True
    if os.path.splitext(args.filename)[1].lower() not in ['.jpg', '.png', '.bmp']:
        print(__file__ + ': error: The file is not a bitmap file.')
        quit()
    try:
        f = open(args.filename, 'rb')
        f.close()
    except FileNotFoundError:
        print(__file__ + ': error: The file is not existing.')
        quit()
    bitmap = cv2.imread(args.filename)
    bitmap = cv2.pyrDown(bitmap)
    screen_size = get_screen_size()
    max_height = screen_size[1] - 150
    if bitmap.shape[0] > max_height:
        bitmap = cv2.resize(bitmap, (
            int(bitmap.shape[1] * (max_height / bitmap.shape[0])),
            max_height))
    draw_bitmap(bitmap)


if __name__ == '__main__':
    main()