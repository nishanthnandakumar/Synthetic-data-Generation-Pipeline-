FROM tensorflow/tensorflow:2.12.0-gpu

ARG DEBIAN_FRONTEND=noninteractive

#Install dependencies
#RUN apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
RUN apt-get update && apt-get -y install clinfo cmake git wget tar qtbase5-dev libgoogle-glog-dev libtbb-dev libcholmod3 libatlas-base-dev libopenni0  mesa-utils 
#cuda-samples-11-6
RUN export LD_LIBRARY_PATH=$REPO_FOLDER/lib:$LD_LIBRARY_PATH
RUN pip3 install numpy opencv-python 
RUN pip3 install matplotlib tensorflow-datasets ipywidgets
RUN apt-get install -y python3-tk
RUN pip3 install wheel pandas
RUN pip3 install labelImg

WORKDIR /root
RUN wget https://github.com/tensorflow/models/archive/refs/heads/master.zip
RUN apt-get -y install unzip
RUN unzip master.zip
RUN rm -rf master.zip
RUN apt-get -y install protobuf-compiler

WORKDIR /root/models-master/research 
RUN protoc object_detection/protos/*.proto --python_out=. 
RUN cp object_detection/packages/tf2/setup.py . 
RUN python -m pip install .
RUN pip install protobuf==3.20.0

WORKDIR /root
RUN mkdir src

WORKDIR /root/src
RUN mkdir pre_trained_models

# WORKDIR /root/src/pre_trained_models
# RUN wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz
# RUN tar -zxvf ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz
# RUN rm -rf ssd_resnet101_v1_fpn_640x640_coco17_tpu-8.tar.gz

WORKDIR /root/src/pre_trained_models
RUN wget http://download.tensorflow.org/models/object_detection/tf2/20200711/ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz
RUN tar -zxvf ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz
RUN rm -rf ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8.tar.gz


WORKDIR /root/