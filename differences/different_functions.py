import time


# возвращает все значения от начала до конца с пререданным шагом
def frange(start, stop, step):
    while start < stop:
        yield start
        start += step


# по пререданным двум картинкам возвращает массив c координатами отличающихся пиксилей
def different_pix(image, image2):
    start_time = time.time()
    pixels = []

    width = image.size[0]
    height = image.size[1]

    pix = image.convert('L').load()
    pix2 = image2.convert('L').load()


    for i in range(width):
        for j in range(height):
            r = pix[i, j]
            r1 = pix2[i, j]

            if abs(r - r1) > 20:
                pixels.append([i, j])
    return pixels

