# Introduction

This repo is a tutorial for training YOLOX leveraging [MM Detection](https://github.com/open-mmlab/mmdetection).

The example is training [license template dataset](https://github.com/RobertLucian/license-plate-dataset) with YOLOX.

# Detailed steps

Step 1: Install libaries

```shell
pip install openmim shapely future tensorboard
```



Step 2: Download this repo

```shell
git clone https://github.com/mlzoo/yolox-mmdetection-template.git
cd yolox-mmdetection-template
python download_weights.py --weights yolox_l_8x8_300e_coco
```

Step 3: Download mmdet repo

```shell
git clone https://github.com/open-mmlab/mmdetection.git
```



Step 4: Install MM Det

```shell
cd mmdetection
pip install -v -e .
mim install mmdet mmengine mmcv-full
cd ..
```



Step 5: Get License Plate dataset

```shell
git clone https://github.com/RobertLucian/license-plate-dataset
```



Step 6: Make dataset(License Plate)

The architecture of input data:

- Annotations: VOC format annotations
- JPEGImages: raw images
- ImageSet/Main: training sample lists

```shell
mkdir input/data_root/dataset/Annotations input/data_root/dataset/JPEGImages -p
mkdir input/data_root/dataset/JPEGImages
mkdir input/data_root/dataset/ImageSets/Main -p

cp license-plate-dataset/dataset/train/annots/* input/data_root/dataset/Annotations/
cp license-plate-dataset/dataset/train/images/* input/data_root/dataset/JPEGImages/
cp license-plate-dataset/dataset/valid/annots/* input/data_root/dataset/Annotations/
cp license-plate-dataset/dataset/valid/images/* input/data_root/dataset/JPEGImages/
```



Step 7: Make dataset (CCPD2019)

```shell
# download CCPD2019.tar.xz
python download_dataset.py
# uncompress CCPD
tar xvf CCPD2019.tar.xz

# CCPD to VOC format
mkdir Annotations/ccpd_base/ -p
python CCPD_to_VOC.py

# move to input/data_root/dataset/
mv Annotations/ccpd_base/* input/data_root/dataset/Annotations/
```



Step 8: Make sample list

```shell
python make_txt.py
```



Step 9: Start training

```shell
# suggest using screen 'screen -S train'
python train.py 
```



Step 10: Inference 

```shell
python inference_image.py
```


## Basic Dockerfile
```Dockerfile
FROM pytorch/pytorch:1.12.1-cuda11.3-cudnn8-runtime

RUN apt update -y && apt install git gcc ffmpeg libsm6 libxext6 -y

RUN pip install openmim shapely future tensorboard pycocotools



RUN mkdir /packages && \
     cd /packages/ && \
     git clone https://github.com/open-mmlab/mmdetection.git && \
     cd mmdetection &&\
     pip install -v -e . && \
     mim install mmdet mmengine mmcv-full
```

Or you can simply run
```
docker pull mlzoo/mmdetection-predictor:pytorch-1.12.1-python-3.7.13
```
