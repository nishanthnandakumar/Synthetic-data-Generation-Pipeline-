# Blender Dataset

In this project, blender is used to generate synthetic images of a geometric model. Here docker is used to create the environment for using blender. The output from blender is saved on the local system to avoid memory usage error on Git.

## Getting started

Folder Structure:

- docker
    - docker-compose.yml
    - Dockerfile

- src
    - geometric_model
        - 1screw.obj


    - render_images.py

    - test.py

- ReadMe.md

Before we start make sure the docker and other dependencies if required are installed.

These are other requirements that have to be met before executing the commands,

1. Make sure the geometric model is available in the geometric_model repository.

2. Open the docker-compose file and make sure the paths in the volumes section are right,
    - Provide the path to the src repository on the local system.
    - Provide the path to the output repository. Make sure this repository is outside the git repository to avoid memory errors.

3. In the render_images.py edit the following,
    - Line 66 add the path to the geometric model.
    - Line 109 name of the geometric model.

Once all the above requirements are met,

Run the following command in the terminal,

```
xhost local:root
```

Now move into the docker repository and run the following command,

```
docker build -t blender_dataset -f Dockerfile .
```
This builds an image named blender_dataset. Then run the following command,


```
docker-compose up
```
This runs the docker image and creates a docker container named blender_dataset.

Now open another terminal while the docker container is running and run the following command,

```
docker exec -it blender_dataset /bin/bash
```
This command lets us to work inside the docker container.

Once inside move into the src repository and run the following command,

```
python3 render_images.py
```
This starts to render the geometric model and saves the images in the output repository.


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
