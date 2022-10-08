


from mmdet.apis import inference_detector
from mmdet.apis import init_detector
from cfg import cfg


import argparse
import mmcv
import glob as glob
import os
from tqdm import tqdm

# Contruct the argument parser.
parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input', default='/home/ubuntu/mm/input/data_root/dataset/JPEGImages',
    help='path to the input data'
)
parser.add_argument(
    '-w', '--weights', 
    default='outputs/yolox_l_8x8_300e_coco/epoch_285.pth',
    help='weight file name'
)
parser.add_argument(
    '-t', '--threshold', default=0.5, type=float,
    help='detection threshold for bounding box visualization'
)

args = vars(parser.parse_args())

# Build the model.

print(cfg.device)
model = init_detector(cfg, args['weights'], device='cpu')

image_paths = glob.glob(f"{args['input']}/*.jpg")

with open('input/data_root/dataset/ImageSets/Main/train.txt') as f:
    files = f.readlines()


image_paths = glob.glob("test2/*.jpg")


for i, image_path in enumerate(tqdm(image_paths)):
    # image_path = 'input/data_root/dataset/JPEGImages/{}.jpg'.format(file[:-1])
    file = image_path
    image = mmcv.imread(image_path)
    # Carry out the inference.
    result = inference_detector(model, image)
    print(result)
    # Show the results.
    frame = model.show_result(image, result, score_thr=args['threshold'])
    # mmcv.imshow(frame)
    # Initialize a file name to save the reuslt.
    save_name = f"{image_path.split(os.path.sep)[-1].split('.')[0]}"
    mmcv.imwrite(frame, f"pred/{image_path}.jpg")
    print(f"pred/{image_path}.jpg")


