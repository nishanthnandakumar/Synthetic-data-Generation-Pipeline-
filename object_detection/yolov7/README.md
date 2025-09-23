# object_detection

This repository is used for object detection of parts using the YOLOv7 model. The fastest OD model with best performance in 2024.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t yolo_v7 -f Dockerfile .
```

Make sure the locations are right in the docker-compose file for all the repositories is provided.

The dataset has to be added to the /data repository in the yolov7_custom repository in the following format,
```plaintext
/yolov7_custom
    /data
        /train
            /images
            /labels
        /test
            /images
            /labels
        /val
            /images
            /labels
```

The following changes are to be made in order to train the custom model,

1. cd into ./yolov7_custom/data/ and copy coco.yaml and save as custom_data.yaml

2. In custom_data.yaml remove lines 1-5, provide the path to train, test, and val as created earlier, and enter the number of classes(nc). Also, enter the names of the classes as per the classes.txt file obtained from labelImg.

3. cd into ./yolov7_custom/cfg/training and copy yolov7.yaml and save as yolov7_custom.yaml

4. Open yolov7_custom.yaml and edit line 2 and enter the number of classes(nc) in your dataset.

and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it yolo_v7 /bin/bash
```

This would access the running container. Once inside cd into src/yolov7_custom/ and run the following command to train the model.

```
python train.py --workers 1 --device 0 --batch-size 8 --epochs 100 --img 640 640 --data ./data/custom_data.yaml --hyp ./data/hyp.scratch.custom.yaml --cfg ./cfg/training/yolov7_custom.yaml --name yolov7_mech_parts --weights ./yolov7.pt
```
Once trained you can find the training logs, graphs inside the ./runs/train/yolov7_mech_parts repository

Here, cd into weights repository and copy the best.pt file and copy it to the yolov7_custom repo and rename as yolov7_mech_parts.pt

To test the trained yolov7 model run the following command,

```
python test.py --data ./data/custom_data.yaml --img 640 --batch 8 --conf 0.001 --iou 0.65 --device 0 --weights ./yolov7_mech_parts.pt --name yolov7_mech_parts_val

```

This will generate and save all the graphs and logs in the runs repository.

To get predictions run the following command,

```
python detect.py --weights yolov7_mech_parts.pt --conf 0.5 --img-size 640 --source ./path to image --view-img --no-trace

```

If there is a CUDA Memory shortage error try the following commands,

1. Open python in terminal inside the docker container

```
python
import torch
torch.cuda.empty_cache()

```
2. Run the following inside the docker container

```
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128

```


## External Dependencies

The following are required to run the project successfully,

1. docker
2. docker compose
3. nvidia docker
4. Tensorflow gpu
5. CuDA and CuDNN

## Build Dependencies

None

## Run Dependencies

None

## Authors

Nishanth Nandakumar @nandakun

## License

For open source projects, say how it is licensed.

## Project Status

Ongoing
