# festo_machine_pipeline

This repository is used for running the Festo Machine pipeline automatically.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
./script.sh
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

Nishanth Nandakumar
Jörg Eberhardt

## License

For open source projects, say how it is licensed.

## Project Status

Completed
