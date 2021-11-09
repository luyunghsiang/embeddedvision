import random
import torch
import torch.nn
import torch.optim
import sys
import time

### Neural Network Model
### MNIST images are 1 channel 28x28 images
class MNIST_CNN( torch.nn.Module ):
  # Constructor
  def __init__(self):
	# Invoke constructor of nn.Model
	super(MNIST_CNN, self).__init__()
	# Initialize layers of network
	self.conv1	  = torch.nn.Conv2d(in_channels=1, out_channels=16, kernel_size=3, stride=1, padding=1)
	self.bn1	  = torch.nn.BatchNorm2d(16)
	self.maxpool1 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

	self.conv2	  = torch.nn.Conv2d(in_channels=16, out_channels=24, kernel_size=3, stride=1, padding=1)
	self.bn2	  = torch.nn.BatchNorm2d(24)
	self.maxpool2 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

	self.conv3	  = torch.nn.Conv2d(in_channels=24, out_channels=32, kernel_size=3, stride=1, padding=1)
	self.bn3	  = torch.nn.BatchNorm2d(32)
	self.conv4	  = torch.nn.Conv2d(in_channels=32, out_channels=32, kernel_size=3, stride=1, padding=1)
	self.bn4	  = torch.nn.BatchNorm2d(32)

	self.conv5	  = torch.nn.Conv2d(in_channels=32, out_channels=48, kernel_size=3, stride=1, padding=1)
	self.bn5	  = torch.nn.BatchNorm2d(48)
	self.maxpool3 = torch.nn.MaxPool2d(kernel_size=2, stride=2)

	# Final Output Layers
	# Flatten 1x28x28 to 1x784
	# This is done in the forward(...) function
	# Create a fully connected layer followed by softmax to interpet the output of the neural network as confidences for the classes
	self.fully_connected  = torch.nn.Linear(in_features=432, out_features=10)  # tensor of length 10
	self.softmax		  = torch.nn.LogSoftmax(dim=1) # tensor of length 10, but entries are interpreted as probabilities

  def predict(self, input):
	# Do a forward pass to get a 1x10 tensor of class predcitions 
	x = self.forward( input.cuda() )
	# The final layer is LogSoftmax(...), so just use argmax to get the prediction
	x = torch.argmax( x, dim=1 )
	return x

  def forward(self, input):
	x = self.conv1( input.cuda() )
	x = self.bn1( x )
	x = torch.nn.functional.relu6( x )
	x = self.maxpool1( x )

	x = self.conv2( x )
	x = self.bn2( x )
	x = torch.nn.functional.relu6( x )
	x = self.maxpool2( x )

	x = self.conv3( x )
	x = self.bn3( x )
	x = torch.nn.functional.relu6( x )

	x = self.conv4( x )
	x = self.bn4( x )
	x = torch.nn.functional.relu6( x )

	x = self.conv5( x )
	x = self.bn5( x )
	x = torch.nn.functional.relu6( x )
	x = self.maxpool3( x )

	x = x.view( 1, 432 )
	x = self.fully_connected( x )
	x = self.softmax( x )
	return x

### Create a 'fake' testing dataset of 500 images and compute the inference time
mnist_images 	= torch.floor( torch.rand(500,1,1,28,28) * 255.0 )
### Load model from .pt file
model = MNIST_CNN()
model.load_state_dict( torch.load('partially_trained_model.pt',map_location=torch.device('cpu')) )
model.eval()
### Compute inference time. Compare to Google Colab
start_time = time.perf_counter_ns()

for k in range(500):
	model.forward( mnist_images[k] )
	
elapsed_time = ( time.perf_counter_ns() - start_time ) / 1000000000
print("Elapsed time (seconds): {}".format(elapsed_time))
