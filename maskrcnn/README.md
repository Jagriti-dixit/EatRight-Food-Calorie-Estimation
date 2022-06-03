## Instructions to train the model ##

Run command for running with coco weights. Give absolute weights path if you want to resume a run with another weights file
python3 food.py train --dataset=/home/ubuntu/data/data/common/kaggle-food-101/annotated_images --weights=coco --logs logs


The manual annotations that we created for the images are in the "annotated_images" directory has two folders:
1. train 
2. val 
The two folders contain their respective "via_region_data.json" file containing region-of-interest (ROI) information for all the images.
