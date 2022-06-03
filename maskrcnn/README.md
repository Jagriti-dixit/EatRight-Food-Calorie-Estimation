README

Run command for running with coco weights. Give absolute weights path if you want to resume a run with another weights file
python3 food.py train --dataset=/home/ubuntu/data/data/common/kaggle-food-101/annotated_images --weights=coco --logs logs


annotated_images directory has two folders train and val with images and their via_region_data.json file containing segment information for all the images.
