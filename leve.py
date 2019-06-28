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

    for F in range(onlyfiles.__len__()):
    # for F in range(10):
        file = onlyfiles[F]
        if (F % 10) == 0:
            print(F)
        if file != 'Thumbs.db':
            path = mypath + file
            #
            image_file = Image.open(path)  # open colour image
            image_file = image_file.convert('1')  # convert image to black and white
            image_file = image_file.filter(ImageFilter.MaxFilter(3))
            image_file = image_file.filter(ImageFilter.MinFilter(3))
            # # image_file.save('result1.png')
            #
            image_M = np.asanyarray(image_file)
            # start_x = -1
            # end_x = -1
            # start_y = -1
            # end_y = -1
            # for i in range(len(image_M)):
            #     flag = False
            #     for j in range(len(image_M)):
            #         if image_M[i][j]:
            #             # print(i, j)
            #             start_x = i
            #             flag = True
            #             break
            #     if flag:
            #         break
            #
            # for i in range(len(image_M) - 1, -1, -1):
            #     flag = False
            #     for j in range(len(image_M) - 1, -1, -1):
            #         if image_M[i][j]:
            #             # print(i, j)
            #             end_x = i
            #             flag = True
            #             break
            #     if flag:
            #         break
            #
            # for i in range(len(image_M)):
            #     flag = False
            #     for j in range(len(image_M)):
            #         if image_M[j][i]:
            #             # print(i, j)
            #             start_y = i
            #             flag = True
            #             break
            #     if flag:
            #         break
            #
            # for i in range(len(image_M) - 1, -1, -1):
            #     flag = False
            #     for j in range(len(image_M) - 1, -1, -1):
            #         if image_M[j][i]:
            #             # print(i, j)
            #             end_y = i
            #             flag = True
            #             break
            #     if flag:
            #         break

            # print(start_x, start_y)
            # print(end_x, end_y)
            # print("numero isolado")
            jump_x = 7
            jump_y = 7
            # print(jump_x, jump_y)
            # print(round(jump_x), round(jump_y))
            black = 0
            white = 0
            wb = []
            for i in range(16):
                wb.append(0.0)
            wb.append(cla)
            for i in range(4):
                for j in range(4):
                    for k in range(round(i * jump_x), round((i + 1) * jump_x)):
                        for l in range(round(j * jump_y), round((j + 1) * jump_y)):
                            if image_M[k][l]:
                                white = white + 1
                            else:
                                black = black + 1
                    if black == 0:
                        wb[(i*4)+j] = 1
                        # print(black, white, white)
                    else:
                        wb[(i*4)+j] = white / black
                        # print(black, white, white / black)
                    black = 0
                    white = 0
            # classssssssssssssssss
            df2e = pd.DataFrame([wb], columns=fields)
            df2 = df2.append(df2e, ignore_index=True)
            df2.to_csv('Base2.csv')


