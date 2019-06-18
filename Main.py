from PIL import Image
import numpy as np
image_file = Image.open("img_1.jpg") # open colour image
image_file = image_file.convert('1') # convert image to black and white
image_file.save('result.png')
image_M = np.asanyarray(image_file)
start_x = -1
end_x = -1
start_y = -1
end_y = -1
for i in range(len(image_M)):
    flag = False
    for j in range(len(image_M)):
        if image_M[i][j]:
            # print(i, j)
            start_x = i
            flag = True
            break
    if flag:
        break

for i in range(len(image_M)-1, -1, -1):
    flag = False
    for j in range(len(image_M)-1, -1, -1):
        if image_M[i][j]:
            # print(i, j)
            end_x = i
            flag = True
            break
    if flag:
        break

for i in range(len(image_M)):
    flag = False
    for j in range(len(image_M)):
        if image_M[j][i]:
            # print(i, j)
            start_y = i
            flag = True
            break
    if flag:
        break

for i in range(len(image_M)-1, -1, -1):
    flag = False
    for j in range(len(image_M)-1, -1, -1):
        if image_M[j][i]:
            # print(i, j)
            end_y = i
            flag = True
            break
    if flag:
        break
print(start_x, start_y)
print(end_x, end_y)
print("numero isolado")
jump_x = (end_x - start_x) / 4
jump_y = (end_y - start_y) / 4
print(jump_x, jump_y)
print(round(jump_x), round(jump_y))
for i in range(4):
    for j in range(4):
        
