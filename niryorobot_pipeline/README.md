# niryorobot_pipeline

This repository is used for running the Niryo Robot pipeline automatically.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t niryo_robot_pipeline -f Dockerfile .
```


Make sure the locations are right in the docker-compose file for all the repositories and the dataset.


and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it niryo_robot_pipeline /bin/bash
```



## External Dependencies

The following are required to run the project successfully,

1. docker
2. docker compose
3. nvidia docker
4. Pytorch
5. Tensorflow gpu
6. CuDA and CuDNN

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
