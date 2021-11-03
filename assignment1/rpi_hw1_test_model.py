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
    # Encoder Layer
    # Encoder 1
    self.conv1  = torch.nn.Conv2d(in_channels=1, out_channels=4, kernel_size=3, stride=1, padding=1)      # 4x28x28
    self.relu1  = torch.nn.ReLU()
    self.conv2  = torch.nn.Conv2d(in_channels=4, out_channels=8, kernel_size=3, stride=1, padding=1)      # 8x28x28
    self.relu2  = torch.nn.ReLU()
    self.conv3  = torch.nn.Conv2d(in_channels=8, out_channels=12, kernel_size=3, stride=1, padding=1)     # 12x28x28
    self.relu3  = torch.nn.ReLU()
    self.conv4  = torch.nn.Conv2d(in_channels=12, out_channels=16, kernel_size=3, stride=1, padding=1)    # 16x28x28
    self.relu4  = torch.nn.ReLU()
    self.decode_conv5  = torch.nn.Conv2d(in_channels=16, out_channels=12, kernel_size=3, stride=1, padding=1)     # 12x28x28
    self.decode_relu5  = torch.nn.ReLU()
    self.decode_conv6  = torch.nn.Conv2d(in_channels=12, out_channels=8, kernel_size=3, stride=1, padding=1)    # 8x28x28
    self.decode_relu6  = torch.nn.ReLU()
    self.decode_conv7  = torch.nn.Conv2d(in_channels=8, out_channels=4, kernel_size=3, stride=1, padding=1)    # 4x28x28
    self.decode_relu7  = torch.nn.ReLU()
    self.decode_conv8  = torch.nn.Conv2d(in_channels=4, out_channels=1, kernel_size=3, stride=1, padding=1)    # 1x28x28
    self.decode_relu8  = torch.nn.ReLU()

    # Final Output Layers
    # Flatten 1x28x28 to 1x784
    # This is done in the forward(...) function

    # Create a fully connected layer followed by softmax to interpet the output of the neural network as confidences for the classes
    self.fully_connected = torch.nn.Linear(in_features=28*28, out_features=10)  # tensor of length 10
    self.softmax  = torch.nn.LogSoftmax(dim=1) # tensor of length 10, but entries are interpreted as probabilities

  def predict(self, input):
    # Do a forward pass to get a 1x10 tensor of class predcitions 
    x = self.forward( input )
    # The final layer is LogSoftmax(...), so just use argmax to get the prediction
    x = torch.argmax( x )
    return x

  def forward(self, input):
    x = self.conv1( input )
    x = self.relu1( x )
    x = self.conv2( x )
    x = self.relu2( x )
    x = self.conv3( x )
    x = self.relu3( x )
    x = self.conv4( x )
    x = self.relu4( x )
    x = self.decode_conv5( x )
    x = self.decode_relu5( x )
    x = self.decode_conv6( x )
    x = self.decode_relu6( x )
    x = self.decode_conv7( x )
    x = self.decode_relu7( x )
    x = self.decode_conv8( x )
    x = self.decode_relu8( x )
    x = x.view( 1, 28*28 )
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
