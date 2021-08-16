from sklearn.cluster import DBSCAN
from PIL import Image
import show_different_pixels_map
import circle
import different_functions
import time

file1 = input("Введите название первого файла: ")
file2 = input("Введите название второго файла: ")


image = Image.open(file1 + ".jpg")
image2 = Image.open(file2 + ".jpg")
image_for_circle = Image.open(file2 + ".jpg")
(width, height) = image.size
pix = image2.load()
picture_for_circle = image_for_circle.load()

start_time = time.time()

x = show_different_pixels_map.get_border_pixels(different_functions.different_pix(image, image2), width, height)

if len(x) == 0:
    image.show()
    image2.show()
else:
    db = DBSCAN(eps=10, min_samples=10).fit(x)
    labels = db.labels_



    n_clusters = max(labels) + 1

    pixels = [[] for i in range(n_clusters)]

    for i in range(len(labels)):
        if labels[i] != -1:
            pixels[labels[i]].append(x[i])

    print("Время работы программы без отрисовки кругов: ",time.time() - start_time)

    for i in range(n_clusters):
        max_x, min_x, max_y, min_y = circle.square_definition(pixels[i])
        centre, radius = circle.described_circle(max_x, min_x, max_y, min_y)
        circle.draw_circle(centre, radius, width, height, pix, picture_for_circle)

    print("Время работы всей программы: ", time.time() - start_time)

    image.show()
    image2.show()

