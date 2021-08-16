from PIL import Image

different_pixels_map = [
    [False, False, False, False, False],
    [False, False, True, True, False],
    [False, False, False, True, False],
    [False, True, True, True, False],
    [False, False, False, False, False],
    [False, False, False, False, False]
]


def show_different_pixels_map(different_pixels_map):
    width = len(different_pixels_map[0])
    height = len(different_pixels_map)

    img = Image.new("RGB", (width, height), (255, 255, 255))
    pix = img.load()

    for y in range(len(different_pixels_map)):
        for x in range(y):
            if different_pixels_map[y][x] == True:
                pix[x, y] = (0, 0, 0)

    img.show()
#print(count_neighbours(1, 1, different_pixels_map))


def count_neighbours(x, y, different_pixels_map):
    if (y == len(different_pixels_map) or x == len(different_pixels_map[0])):
        print("a")
        return True
    neighbours = 0
    for i in range(-1, 1):
        for j in range(-1, 1):
            if (different_pixels_map[y + i][x + j] == False):
                neighbours += 1
    if ((neighbours - 1) <= 6):
        return True
    return False

def bordering_pixels(pixels):
    array_of_adjoining = []
    for x in pixels:
        if (count_neighbours(x[0], x[1], different_pixels_map) == True):
            array_of_adjoining.append(x)
    return array_of_adjoining