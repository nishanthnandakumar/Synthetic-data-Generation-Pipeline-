# data_preprocessing

This repository is used for labelling of data prepocessing required before training the model. Currently we have labelImg as labeling tool and visualflow to convert from pascal voc to yolo.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t data_label -f Dockerfile .
```
and
```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it data_label /bin/bash
```
This would access the running container. 
The label format can be changed by two methods,

1. Use LabelImg to open the images and change the format from PascalVOC to YOLO and save.
2. Use the python script provided in the repo. Change the file locations as required.

Once inside cd into src and run the following command to change from PascalVOC to YOLO format,

```
python3 test.py
```

For using labelImg use the following command,

```
labelImg
```

## External Dependencies

The following are required to run the project successfully,

1. docker
2. docker compose
3. nvidia docker

## Build Dependencies

None

## Run Dependencies

None

## Authors

Nishanth Nandakumar
Jörg Eberhardt

## License

For open source projects, say how it is licensed.

## Project Status

Completed

