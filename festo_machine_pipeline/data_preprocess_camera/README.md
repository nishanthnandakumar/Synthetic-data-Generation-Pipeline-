# data_preprocessing

This repository is used for any kind of data prepocessing required before training the model. Currently we have resize and renaming files.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t data_preprocessing_festo -f Dockerfile .
```
and
```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it data_preprocessing_festo /bin/bash
```
This would access the running container. Once inside cd into src and run the following command to resize and rename the images

```
python3 resizenrename.py
```

For using dataaugmentation run after all the locations are right,

```
python3 data_augmentation.py
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

Nishanth Nandakumar @nandakun

## License

For open source projects, say how it is licensed.

## Project Status

Ongoing

