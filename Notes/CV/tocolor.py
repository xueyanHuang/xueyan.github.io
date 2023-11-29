import os
from PIL import Image

filepath=r'D:\img\imgmask'
total = os.listdir(filepath)
savepath = r'D:\img\imgcolor'

num = len(total)
list = range(num)


for i in list:
    filename = total[i][:-4] + '.png'
    img = os.path.join(filepath, filename)
    mask = Image.open(img).convert('L')
    mask.putpalette([0, 0, 0,  # putpalette给对象加上调色板，相当于上色：背景为黑色，目标１为红色，目标2为黄色，目标3为橙色（如果你的图中有更多的目标，可以自行添加更多的调色值）
                     255, 255, 255,
                     255, 255, 0,
                     255, 153, 0])

    #filename2 = total[i][:-4] + '.png'
    mask.save(os.path.join(savepath, filename))
