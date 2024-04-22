import csv
import os


imgs=[] #['95.999999_022.png.npy', '96.999999_021.png.npy', '97.999999_013.png.npy', '98.999999_016.png.npy', '99.999999_012.png.npy']
imgs_with_filepath=[]  #['./predict_result/95.999999_022.png.npy', './predict_result/96.999999_021.png.npy', './predict_result/97.999999_013.png.npy', './predict_result/98.999999_016.png.npy', './predict_result/99.999999_012.png.npy']


#022.png not coding (under dev)
image_with_route=[]
images = []
image_file_path="D:\\python_work\\AD_Work\\anomalydetection-main\\combine_all\\datasets\\dataset\\"

filepath="./predict_result/"
files = os.listdir(filepath)
for file in files:
    if file.endswith('.png.npy'):
        print(file) #95.999999_022.png.npy

        rates=file.split('_')[0] 
        print(rates) #96.999999

        start_index = file.find('_')+1
        end_index = file.find('.npy')
        desired_output = file[start_index:end_index]
        print(desired_output) # 022.png

        with open('D:\\python_work\\AD_Work\\anomalydetection-main\\combine_all\\datasets\\datasets_label.csv', encoding='utf-8') as csvfile:
            rows = csv.reader(csvfile)
            for row in rows:
                if row[0]==desired_output and row[1]=='FALSE':
                    print('i need it\n')
                    imgs.append(file)
                    images.append(desired_output)


#['95.999999_022.png.npy', '96.999999_021.png.npy', '97.999999_013.png.npy', '98.999999_016.png.npy', '99.999999_012.png.npy']
print(imgs)
print(len(imgs))




# 遍历 imgs 列表
for filename in imgs:
    # 将文件名与文件路径拼接
    full_path = os.path.join(filepath, filename)
    # 将拼接后的路径添加到 imgs_with_filepath 列表中
    imgs_with_filepath.append(full_path)

# 输出结果
#['./predict_result/95.999999_022.png.npy', './predict_result/96.999999_021.png.npy', './predict_result/97.999999_013.png.npy', './predict_result/98.999999_016.png.npy', './predict_result/99.999999_012.png.npy']
print(imgs_with_filepath)



#輸出結果['022.png', '021.png', '013.png', '016.png', '012.png']
print(images)
print(len(images))




for image in images:
    image_full_path=os.path.join(image_file_path,image)
    image_with_route.append(image_full_path)

print(image_with_route) #['D:\\python_work\\AD_Work\\anomalydetection-main\\combine_all\\datasets\\dataset\\022.png'

        


