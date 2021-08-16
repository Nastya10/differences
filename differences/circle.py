import math
import different_functions


# в переданной отличающейся области находит самый правый, левый, верхний и нижний пиксель -
# минимальные и максимальные значения высот и ширин
def square_definition(array):
    max_x = array[0][0]
    min_x = array[0][0]
    max_y = array[0][1]
    min_y = array[0][1]

    for i in array:
        if i[0] > max_x:
            max_x = i[0]
        if i[0] < min_x:
            min_x = i[0]
        if i[1] > max_y:
            max_y = i[1]
        if i[1] < min_y:
            min_y = i[1]

    return max_x, min_x, max_y, min_y


# по минимальнм и максимальнм значениям высоты и ширины находит
# центр и радиус описанной вокруг отличающейся области окружности
def described_circle(max_x, min_x, max_y, min_y):
    centre = [(max_x - min_x) // 2 + min_x, (max_y - min_y) // 2 + min_y]
    sum = ((max_x - min_x) // 2) ** 2 + ((max_y - min_y) // 2) ** 2
    radius = math.sqrt(sum) * 1.2
    return centre, radius


# по центру и радиусу описанной окружности строит на картинке красную окружность
def draw_circle(centre, radius, width, height, pix, picture_for_circle):

    for i in different_functions.frange(0, 360, 0.01):
        x = math.cos(i) * radius
        y = math.sin(i) * radius


        if 0 < centre[0] + x and centre[0] + x < width and 0 < centre[1] + y and centre[1] + y < height:
            pix[centre[0] + x, centre[1] + y] = (255, 0, 0)

        if 0 < centre[0] + x - 1 and centre[0] + x + 1 < width and 0 < centre[1] + y - 1 and centre[1] + y + 1 < height:
            for i in range(0, 2):
                for j in range(0, 2):
                    pix[centre[0] + x + i, centre[1] + y + j] = (255, 0, 0)
