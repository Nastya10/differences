from PIL import Image


# по переданному массиву пикселей выводит картинку
def show_different_pixels_map(different_pixels_map):
    height = len(different_pixels_map[0])
    width = len(different_pixels_map)

    img = Image.new("RGB", (width, height), (255, 255, 255))
    pix = img.load()

    for y in range(height):
        for x in range(width):
            if different_pixels_map[x][y]:
                pix[x, y] = (0, 0, 0)
    img.show()



# по переданнм координатам пикселя в двумерном массиве проверяет,
# пренадлежит ли этот пиксель границе отличающейся области (True)
def is_bordering_pixel(x, y, different_pixels_map):
    width = len(different_pixels_map)
    height = len(different_pixels_map[0])

    if x == width - 1 or y == height - 1 or x == 0 or y == 0:
        return True
    neighbours = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if not(i == 0 and j == 0) and different_pixels_map[x + i][y + j]:
                neighbours += 1
    return neighbours <= 6


# передается отличающаяся область, возвращается ее граница
def bordering_pixels(pixels, different_pixels_map):
    array_of_bordering = []
    for pixel in pixels:
        if is_bordering_pixel(pixel[0], pixel[1], different_pixels_map):
            array_of_bordering.append(pixel)
    return array_of_bordering


# создает картинку с закрашенной отличающейся областью (закрашено - (True))
def pixels_map(pixels, width, height):
    picture = [[False for y in range(height)] for x in range(width)]
    for [x, y] in pixels:
        picture[x][y] = True
    return picture


# по переданному массиву координат отличающихся пикселей,
# высоте и ширине картинки возвращает границу отличающихся областей

def get_border_pixels(pixels, width, height):
    different_pixels_map = pixels_map(pixels, width, height)
    bordering_pixel = bordering_pixels(pixels, different_pixels_map)
    return bordering_pixel