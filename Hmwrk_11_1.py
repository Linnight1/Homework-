import PIL
import matplotlib.pyplot as plt
import requests
from PIL import Image, ImageFilter
response = requests.head("https://7fon.org")
print(response.headers)
print(response.json)
my_lst = [58840,79027,60731]
count = 0
for i in my_lst:

    response = requests.get(f'https://i.7fon.org/1000/x{i}.jpg')
    count += 1
    with open(f'img{count}.jpg', 'wb') as picture:
        picture.write(response.content)
images = ["img1.jpg","img2.jpg","img3.jpg"]
for image in images:
    with Image.open(image) as img:
        img.load()
        # img.show()
        print(img.format,img.size,img.mode)
image = "img1.jpg"
with Image.open(image) as img:
    cropped_img = img.crop((200, 200, 775, 530))
    cropped_img.load()
    # cropped_img.show()
    cropped_img.save("cropped_image.jpg")
print(cropped_img.mode)

response = requests.get("https://optim.tildacdn.com/tild6633-6535-4163-b666-383564623061/-/resize/320x/-/format/webp/Urban_University_log.png")
with open(f'img.png', 'wb') as picture:
    picture.write(response.content)
logo = "img.png"
with Image.open(logo) as img_logo:
    img_logo.load()

img_logo = Image.open(logo)
# img_logo.show()
img_logo = img_logo.convert("RGBA")
img_logo = img_logo.convert("L")
img_logo = img_logo.filter(ImageFilter.SMOOTH)
threshold = 50
img_logo = img_logo.point(lambda x: 255 if x > threshold else 0)
img_logo = img_logo.resize(
    (img_logo.width // 2, img_logo.height // 2)
)

img_logo = img_logo.filter(ImageFilter.CONTOUR)
# img_logo.show()

img_logo = img_logo.point(lambda x: 0 if x == 255 else 255)
# img_logo.show()
cropped_img.paste(img_logo, (1, 1), img_logo)
cropped_img.show()
cropped_img.save("image.jpg")
# Дальше код никак не связанный с предыдущими действиями. Хотелось бы, конечно, подсчитать и отразить в диаграмме что-то,
# связанное со скачанными картинками, но у меня пока не получается придумать что-то простое.
x = [1,2,3,4,5,6]
y = [20,24,45,11,23,68]
plt.plot(x,y,color = "red",marker = "o", markersize = 5)
plt.xlabel("Ось x")
plt.ylabel("Ось y")
plt.show()
x = ["Май", "Июнь", "Июль", "Август"]
y = [13,25,50,34]
plt.bar(x, y, label = "Затраты на ремонт")
plt.xlabel("Месяц")
plt.ylabel("Затраты в рублях")
plt.title("Столбчатая диаграмма с грустным содержанием")
plt.legend()
plt.show()


