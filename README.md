# Introduction

This repo is a tutorial for training YOLOX leveraging [MM Detection](https://github.com/open-mmlab/mmdetection)

# Detailed steps

```shell
https://github.com/mlzoo/yolox-mmdetection-template.git
```

```shell
git clone https://github.com/open-mmlab/mmdetection.git
```
 

 python download_weights.py --weights yolox_l_8x8_300e_coco

 python train.py 

 git clone https://github.com/RobertLucian/license-plate-dataset


  make dataset

 mkdir input/data_root/dataset/Annotations input/data_root/dataset/JPEGImages -p
 mkdir input/data_root/dataset/JPEGImages
 mkdir input/data_root/dataset/ImageSets/Main -p

 cp license-plate-dataset/dataset/train/annots/* input/data_root/dataset/Annotations/
 cp license-plate-dataset/dataset/train/images/* input/data_root/dataset/JPEGImages/
 cp license-plate-dataset/dataset/valid/annots/* input/data_root/dataset/Annotations/
 cp license-plate-dataset/dataset/valid/images/* input/data_root/dataset/JPEGImages/

  CCPD_base
 pip install shapely
 mkdir Annotations/ccpd_base/ -p
 python CCPD_to_VOC.py
 mv Annotations/ccpd_base/* input/data_root/dataset/Annotations/

  make train.txt & val.txt
 python make_txt.py

   echo license-plate > classes_list.txt

 pip install future tensorboard

python inference_image.py --weights checkpoints/yolox_l_8x8_300e_coco_20211126_140236-d3bd2b23.pth




 vi Annotations/ccpd_base/00651340996169-92_91-286\&523_436\&575-436\&576_285\&572_284\&519_435\&523-0_0_3_11_27_26_26-174-14.xml 


find Annotations/ccpd_base/ -name "*.xml" | xargs -i cp {} input/data_root/dataset/Annotations/
find CCPD2019/ccpd_base/ -name "*.jpg" | xargs -i cp {} input/data_root/dataset/JPEGImages/






 install cpu-ver for test
pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

pip install -U openmim
 git clone https://github.com/open-mmlab/mmdetection.git
cd mmdetection
pip install -v -e .
pip install mmdet
mim install mmengine

mim download mmdet --config yolov3_mobilenetv2_320_300e_coco --dest .

python download_dataset.py













