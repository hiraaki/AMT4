import numpy as np
import pandas as pd
from PIL import Image, ImageFilter
from os import listdir
from os.path import isfile, join



fields = []
for i in range(16):
    if i != 15:
        fields.append('A'+i.__str__())
    else:
        fields.append('A' + i.__str__())
        fields.append('clas')

fields2 = []
for i in range(784):
    if i != 783:
        fields2.append(('A'+i.__str__()))
    else:
        fields2.append('A' + i.__str__())
        fields2.append('clas')

df1 = pd.DataFrame(columns=fields)
df2 = pd.DataFrame(columns=fields2)

for cla in range(10):
    print(cla)
    print("---------")
    mypath = "ct\\"+cla.__str__()+"\\"
    onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    F = 0
    for file in onlyfiles:
        F += 1
        if (F % 10) == 0:
            print(F)
        if file != 'Thumbs.db':
            path = mypath + file

            image_file = Image.open(path)  # open colour image
            image_file = image_file.convert('1')  # convert image to black and white
            image_file = image_file.filter(ImageFilter.MaxFilter(3))
            image_file = image_file.filter(ImageFilter.MinFilter(3))
            # image_file.save('result1.png')

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

            # # print(start_x, start_y)
            # # print(end_x, end_y)
            # # print("numero isolado")
            # jump_x = (end_x - start_x) / 4
            # jump_y = (end_y - start_y) / 4
            # # print(jump_x, jump_y)
            # # print(round(jump_x), round(jump_y))
            # black = 0
            # white = 0
            # wb = np.zeros(17)
            #
            # for i in range(4):
            #     for j in range(4):
            #         for k in range(start_x + round(i * jump_x), start_x + round((i + 1) * jump_x)):
            #             for l in range(start_y + round(j * jump_y), start_y + round((j + 1) * jump_y)):
            #                 if image_M[k][l]:
            #                     white = white + 1
            #                 else:
            #                     black = black + 1
            #         if black == 0:
            #             wb[(i*4)+j] = white
            #             # print(black, white, white)
            #         else:
            #             wb[(i*4)+j] = white / black
            #             # print(black, white, white / black)
            #         black = 0
            #         white = 0
            # # classssssssssssssssss
            # wb[16] = cla
            # df1e = pd.DataFrame([wb], columns=fields)
            # df1 = df1.append(df1e, ignore_index=True)
            # print(df1e)
            # print(df1)
            # print("--------------------------------------------------------")
            # i*4+j
            entry = np.zeros(785)
            # setor vidno pela direito ao número
            for i in range(start_x, end_x+1):
                for j in range(start_y-1):
                    entry[(i * 28) + j] = 1
            # setor de cima acima ao número
            for i in range(start_x-1):
                for j in range(start_y, end_y+1):
                    entry[(i * 28) + j] = 8
            # setor vidno pela esquerda ao número
            for i in range(start_x, end_x+1):
                for j in range(end_y+1, 28):
                    entry[(i * 28) + j] = 4
                # setor de baixo abaixo do número
                for i in range(end_x+1, 28):
                    for j in range(start_y, end_y+1):
                        entry[(i * 28) + j] = 2

                # print(entry)
                # print("------------------------------------------------------")
                for i in range(start_x, end_x+1):
                    for j in range(start_y, end_y+1):
                        # para direita
                        k = j + 1
                        braked = False
                        if k < 28:
                            while not image_M[i][k]:
                                k += 1
                                if k > end_y:
                                    braked = True
                                    break
                        else:
                            braked = True
                        if not braked:
                            entry[(i * 28) + j] += 1
                        # para baixo
                        k = i + 1
                        braked = False
                        if k < 28:
                            while not image_M[k][j]:
                                k += 1
                                if k > end_x:
                                    braked = True
                                    break
                        else:
                            braked = True
                        if not braked:
                            entry[(i * 28) + j] += 8
                        # para esquerda
                        k = j - 1
                        braked = False
                        if k >= 0:
                            while not image_M[i][k]:
                                k -= 1
                                if (k < start_y) or (k >= 0):
                                    braked = True
                                    break
                        else:
                            braked = True
                        if not braked:
                            entry[(i * 28) + j] += 4

                        # para cima
                        k = j - 1
                        braked = False
                        if k >= 0:
                            while not image_M[k][j]:
                                k -= 1
                                if (k < end_x) or (k >= 0):
                                    braked = True
                                    break
                        if not braked:
                            entry[(i * 28) + j] += 2

                        if image_M[i][j]:
                            entry[(i * 28) + j] += 16
                #classssssssssssssssss
                entry[784] = cla
                df2e = pd.DataFrame([entry.astype(int)], columns=fields2)
                df2 = df2.append(df2e, ignore_index=True)
                df2.to_csv('ct\\Base2.csv')


# df1.to_csv('Base1.csv')


