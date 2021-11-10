import torch
import time

### Student Code Begin
### Copy-paste your IoU function here
def IoU(predictedBoundingBox:list, labelBoundingBox:list) -> float:
	return 0
### Student Code End

### Load bounding box dataset
### The shape of both lists is [20000,2,2]
### predicted_bbox_dataset[0] is the 1st bounding box in the dataset
### predicted_bbox_dataset[0][1] is the upper-left vertex of the 1st bounding box in the dataset
### predicted_bbox_dataset[0][1][0] is the x-coordinate of the upper-left vertex of the 1st bounding box in the dataset
predicted_bbox_dataset 	= torch.load('bounding_box_predicted_dataset_20k.pt').tolist()
labeled_bbox_dataset 	= torch.load('bounding_box_labeled_dataset_20k.pt').tolist()

### Iterate over the upper-left and lower-right vertices of each bounding box
start_time = time.perf_counter_ns()
meanIoU = 0.0
for k in range(20000):
	### Student Code Begin
	### Call your IoU(...) function and pass in the k'th predicted and labeled bounding box pair
	### Student Code End
meanIoU /= 20000.0
elapsed_time = ( time.perf_counter_ns() - start_time ) / 1000000000

### Print meanIoU, inference time
print("Mean IoU: {}".format(meanIoU))
print("Time to compute: {} seconds".format(elapsed_time))
