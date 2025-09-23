FROM nvcr.io/nvidia/pytorch:21.08-py3

ARG DEBIAN_FRONTEND=noninteractive

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

#Install the requirements for the yolov7
RUN pip install matplotlib>=3.2.2
RUN pip install numpy==1.23.1
RUN pip install opencv-python==4.5.5.64
RUN pip install Pillow>=7.1.2
RUN pip install PyYAML>=5.3.1
RUN pip install requests>=2.23.0
RUN pip install scipy>=1.4.1
RUN pip install tqdm>=4.41.0
RUN pip install protobuf==3.20.3

# Logging -------------------------------------
RUN pip install tensorboard>=2.4.1
# wandb

# Plotting ------------------------------------
RUN pip install pandas>=1.1.4
RUN pip install seaborn>=0.11.0

# Extras --------------------------------------
RUN pip install ipython  # interactive notebook
RUN pip install psutil  # system utilization
RUN pip install thop  # FLOPs computation

WORKDIR /root/



