# labelling_images

Used to label images

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t label_images -f Dockerfile .
```


Make sure the locations are right in the docker-compose file for the dataset.


and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it label_images /bin/bash
```

This would access the running container. 

```
labelImg
```

This will open labelImg to label the data.

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
