from PIL import Image
import ddbscan
import show_different_pixels_map
import circle
import different_functions
import time

file1 = input("Введите название первого файла: ")
file2 = input("Введите название второго файла: ")

image = Image.open(file1 + ".jpg")
image2 = Image.open(file2 + ".jpg")
(width, height) = image.size
pix = image2.load()

scan = ddbscan.DDBSCAN(20, 20)

for point in show_different_pixels_map.get_border_pixels(different_functions.different_pix(image, image2), width, height):
    scan.add_point(point=point, count=1, desc="")
scan.compute()


g = 0
pixels = [[]]
cluster_number = 0
for cluster in scan.clusters:
    cluster_number += 1
for i in range(len(scan.points)):
    if g != scan.points_data[i].cluster:
        pixels.append([])
        g += 1
    if scan.points_data[i].cluster == -1:
        print('\t <== Anomaly found!')
    pixels[g].append(scan.points[i])


for i in range(cluster_number):
    print(pixels[i])
    show_different_pixels_map.show_different_pixels_map(show_different_pixels_map.pixels_map(pixels[i], width, height))
    max_x, min_x, max_y, min_y = circle.square_definition(pixels[i])
    centre, radius = circle.described_circle(max_x, min_x, max_y, min_y)
    circle.draw_circle(centre, radius, width, height, pix)

image.show()
image2.show()

print(time.clock())