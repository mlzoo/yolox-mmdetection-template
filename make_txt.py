import os

folders = ['train', 'valid']

for folder in folders:
    print('---\n\nfolder:', folder)
    images = os.listdir('./license-plate-dataset/dataset/{}/images'.format(folder))
    
    print('len(images):', len(images))
    if folder == 'train':
        images += os.listdir('./CCPD2019/ccpd_base/')
        print('len(images):', len(images))
    

    file_name = 'input/data_root/dataset/ImageSets/Main/{}.txt'.format(folder)
    with open(file_name, 'w', encoding='utf-8') as file:
        for image in images:
            file.write('{}\n'.format(image.replace('.jpg', '')))

