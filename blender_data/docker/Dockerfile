FROM zocker160/blender-bpy

ARG DEBIAN_FRONTEND=noninteractive

#Install dependencies

WORKDIR /root

# Installing OpenEXR
RUN apt-get update && \
    apt-get install -y openexr libopenexr-dev && \
    pip3 install OpenEXR && \
    pip3 install open3d-python
