# Run the following commands to install PyTorch and Torchvision on the Raspberry Pi 4B (Raspberry Pi OS)

## Download Cross Complied PyTorch and Torchvision from Google Drive (too large to upload to github)
https://drive.google.com/drive/folders/1GBhk3doR-VDc8IC7JXxIBSIWdk2kQfWh?usp=sharing

## After downloading and unzipping, run the following commands:

#Update RPi if required


$ sudo apt-get update

$ sudo apt-get upgrade


#the dependencies

$ sudo apt-get install ninja-build git cmake

$ sudo apt-get install libopenmpi-dev libomp-dev

$ sudo apt-get install libopenblas-dev libblas-dev libeigen3-dev

$ sudo -H pip3 install -U --user wheel mock pillow ccache

$ sudo -H pip3 install -U setuptools

#set some temporary environment variables

#remember, don't close the window as it will delete these variables

$ export BUILD_CAFFE2_OPS=OFF

$ export USE_FBGEMM=OFF

$ export USE_FAKELOWP=OFF

$ export BUILD_TEST=OFF

$ export USE_MKLDNN=OFF

$ export USE_NNPACK=ON

$ export USE_XNNPACK=ON

$ export USE_QNNPACK=ON

$ export MAX_JOBS=4

$ export USE_NCCL=OFF

$ export USE_SYSTEM_NCCL=OFF

$ sudo pip3 install torch-1.6.0a0+b31f58d-cp37-cp37m-linux_armv7l.whl


$ sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev

$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev

$ sudo pip3 install torchvision-0.6.0a0+b68adcf-cp37-cp37m-linux_armv7l.whl

(made by Abhinav Goel from Purdue University)