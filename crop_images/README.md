# data_preprocessing

This repository is used for cropping the images

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t image_crop -f Dockerfile .
```
and
```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it image_crop /bin/bash
```
This would access the running container. Once inside cd into src and run the following command to crop the images

```
python3 crop_image.py
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

