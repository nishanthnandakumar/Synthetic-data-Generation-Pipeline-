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
