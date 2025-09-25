FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive

#https://developer.blender.org/docs/handbook/building_blender/linux/
#Install python Git Git-lfs
RUN apt update && \
    apt install -y python3 git git-lfs && \
    mkdir ~/blender-git && \
    cd ~/blender-git && \
    git clone https://projects.blender.org/blender/blender.git

RUN apt update && \
    apt install -y build-essential git git-lfs subversion cmake libx11-dev libxxf86vm-dev libxcursor-dev libxi-dev libxrandr-dev libxinerama-dev libegl-dev && \
    apt install -y libwayland-dev wayland-protocols libxkbcommon-dev libdbus-1-dev linux-libc-dev

WORKDIR /root/blender-git/blender

RUN ./build_files/utils/make_update.py --use-linux-libraries

WORKDIR /root/blender-git/blender

RUN make update && \
    make bpy

WORKDIR /root/blender-git/
RUN cmake -C ./blender/build_files/cmake/config/bpy_module.cmake ./blender

RUN apt-get update && \
    apt-get install -y python3-setuptools && \
    apt-get -y install python3-pip && \
    pip3 install wheel && \
    pip3 install bpy && \
    apt update && \
    apt install -y libsm6 libxext6 && \
    apt-get install -y libxrender-dev
#     python3 ./blender/build_files/utils/make_bpy_wheel.py ./build_linux_bpy/bin/
    
# WORKDIR /root/blender-git/build_linux_bpy/bin/
# RUN pip3 install bpy-4.4.0a0-cp311-cp311-ubuntu_22.04.5_x86_64.whl

# WORKDIR /root/blender-git/blender/



WORKDIR /root

# Installing OpenEXR
# RUN apt-get update && \
#     apt-get install -y openexr libopenexr-dev && \
#     pip install OpenEXR && \
#     pip install open3d-python