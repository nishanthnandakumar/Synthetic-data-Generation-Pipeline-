# object_classification

This repository is used for object classification of parts using the [SSD ResNet101 V1 FPN 640x640](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md). This is based on the [online](https://www.youtube.com/watch?v=yqkISICHH-U) proceeding as discussed. This would result in providing the precision, recall, and the loss of the trained model evaluated on the dataset.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t object_classification -f Dockerfile .
```


Make sure the locations are right in the docker-compose file for all the repositories and the dataset.


and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it object_classification /bin/bash
```

This would access the running container. Once inside cd into src and run the following command to train the model.

```
python3 train.py
```

Run the following command to evaluate the model on the test dataset,

```
python3 test.py
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
