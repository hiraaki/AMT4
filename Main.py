from PIL import Image
import numpy as np

image_file = Image.open("img_52.jpg")  # open colour image
image_file = image_file.convert('1')  # convert image to black and white
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

for i in range(len(image_M) - 1, -1, -1):
    flag = False
    for j in range(len(image_M) - 1, -1, -1):
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

for i in range(len(image_M) - 1, -1, -1):
    flag = False
    for j in range(len(image_M) - 1, -1, -1):
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
black = 0
white = 0
for i in range(4):
    for j in range(4):
        for k in range(start_x + round(i * jump_x), start_x + round((i + 1) * jump_x)):
            for l in range(start_y + round(j * jump_y), start_y + round((j + 1) * jump_y)):
                if image_M[k][l]:
                    white = white + 1
                else:
                    black = black + 1
        if black == 0:
            print(black, white, white)
        else:
            print(black, white, white / black)
        black = 0
        white = 0

# i*4+j
entry = np.zeros(784)

# setor vidno pela direito ao número
for i in range(start_x, end_x+1):
    for j in range(start_y):
        entry[(i * 28) + j] = 1
# setor de cima acima ao número
for i in range(start_x):
    for j in range(start_y, end_y):
        entry[(i * 28) + j] = 8
# setor vidno pela esquerda ao número
for i in range(start_x, end_x):
    for j in range(end_y, 28):
        entry[(i * 28) + j] = 4
# setor de baixo abaixo do número
for i in range(end_x, 28):
    for j in range(start_y, end_y):
        entry[(i * 28) + j] = 2

for i in range(start_x, end_x+1):
    for j in range(start_y, end_y+1):
        # para direita
        k = j + 1
        braked = False
        while not image_M[i][k]:
            k += 1
            if k > end_y:
                braked = True
                break
        if not braked:
            entry[(i * 28) + j] += 1
        # para baixo
        k = i + 1
        braked = False
        while not image_M[k][j]:
            k += 1
            if k > end_x:
                braked = True
                break
        if not braked:
            entry[(i * 28) + j] += 8
        # para esquerda
        k = j - 1
        braked = False
        while not image_M[i][k]:
            k -= 1
            if k < start_y:
                braked = True
                break
        if not braked:
            entry[(i * 28) + j] += 4

        # para cima
        k = j - 1
        braked = False
        while not image_M[k][j]:
            k -= 1
            if k < end_x:
                braked = True
                break
        if not braked:
            entry[(i * 28) + j] += 4





