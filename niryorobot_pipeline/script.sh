#!/bin/bash
#This file runs all the required files to make the pipeline automatic
echo ===========================================================
echo Welcome to Automatic Generation of Synthetic Data Pipeline
echo ===========================================================

#checking if the geometric model exists

folder="./geometric_model"

if ls "$folder"/*.STL 1> /dev/null 2>&1; then

    echo =============================================================
    echo A .STL file exists in the folder. Copying the geometric model
    echo =============================================================

    xhost local:root

    #Deleting all the files from previous runs
    rm -rf ./blender/src/geometric_model/*
    rm -rf ./blender/src/output/model1/*
    rm -rf ./cgan_train/src/datasets/parts/trainA/*
    rm -rf ./cgan_train/src/datasets/parts/testA/*
    sudo rm -rf ./cgan_train/checkpoints/*
    sudo rm -rf ./cgan_test/results/*
    rm -rf ./labelling_images/dataset/*
    rm -rf ./object_detection_train/workspace/images/train/*
    rm -rf ./object_detection_train/workspace/images/test/*
    find ./object_detection_train/workspace/models/my_ssd_resnet/ -type f -name '*ckpt*' -exec rm -f {} \;
    rm -rf ./object_detection_train/workspace/models/my_ssd_resnet/checkpoint
    sudo rm -rf ./object_detection_train/workspace/models/my_ssd_resnet/train
    find ./object_detection_train/workspace/annotations -type f -name '*.record' -exec rm -f {} \;



    cp ./geometric_model/*.STL ./blender/src/geometric_model/model.STL

    echo ==================================================================================
    echo Finished copyinth the geometric model and Creating the docker image for blender
    echo ==================================================================================

    docker build -t blender_dataset -f ./blender/docker/Dockerfile .

    echo ====================================================================================
    echo Created the docker image titled blender_dataset and Generating the blender images
    echo ====================================================================================

    docker-compose -f ./blender/docker/docker-compose.yml down
    
    docker-compose -f ./blender/docker/docker-compose.yml up

    docker-compose -f ./blender/docker/docker-compose.yml down

    echo =================================================================
    echo Generated the blender images and copying them to cgan repository
    echo =================================================================

    ls -t ./blender/src/output/model1/ | tail -n +11 | xargs -I {} cp ./blender/src/output/model1/{} ./cgan_train/src/datasets/parts/trainA/

    ls -t ./blender/src/output/model1/ | head -n 10 | xargs -I {} cp ./blender/src/output/model1/{} ./cgan_train/src/datasets/parts/testA/

    echo =================================================================
    echo Files Copied to folder and building the docker image
    echo =================================================================

    docker build -t cyclegan_train -f ./cgan_train/docker/Dockerfile .

    echo ====================================================================================
    echo Created the docker image titled cyclegan_train and training the cycle gan model
    echo ====================================================================================

    docker-compose -f ./cgan_train/docker/docker-compose.yml up

    docker-compose -f ./cgan_train/docker/docker-compose.yml down

    echo ====================================================================================
    echo Completed training the cycle gan model and Generating the images using cgan
    echo ====================================================================================

    docker-compose -f ./cgan_test/docker/docker-compose.yml up

    docker-compose -f ./cgan_test/docker/docker-compose.yml down

    echo ============================================================================================
    echo Completed generating the images using cycle gan model and now copying the generated images
    echo ============================================================================================

    find ./cgan_test/results/parts_cyclegan/test_latest/images/ -type f -name '*fake_B*' -exec cp {} ./labelling_images/dataset \;

    echo ============================================================================================
    echo Completed copying the images and now building an image to label the images
    echo ============================================================================================

    docker build -t label_images -f ./labelling_images/docker/Dockerfile .

    echo ====================================================================================
    echo Created the docker image titled cyclegan_train and training the cycle gan model
    echo ====================================================================================

    docker-compose -f ./labelling_images/docker/docker-compose.yml up

    docker-compose -f ./labelling_images/docker/docker-compose.yml down

    echo ======================================================================================
    echo Completed labelling the images and now copy the datasets to perform object detection
    echo ======================================================================================

    ls -t ./labelling_images/dataset/*.png | tail -n +3 | xargs -I {} cp {} ./object_detection_train/workspace/images/train/

    ls -t ./labelling_images/dataset/*.png | head -n 2 | xargs -I {} cp {} .//object_detection_train/workspace/images/test/

    ############################################

    PNG_FOLDER="./object_detection_train/workspace/images/train"
    TXT_FOLDER="./labelling_images/dataset"
    DEST_FOLDER="./object_detection_train/workspace/images/train"

    for png_file in "$PNG_FOLDER"/*.png; do
        base_name=$(basename "$png_file" .png)
        txt_file="$TXT_FOLDER/$base_name.xml"
        
        if [ -f "$txt_file" ]; then
            cp "$txt_file" "$DEST_FOLDER/"
            echo "Copied: $txt_file to $DEST_FOLDER"
        else
            echo "No matching .xml file found for $png_file"
        fi
    done

    #############################################

    PNG_FOLDER="./object_detection_train/workspace/images/test"
    TXT_FOLDER="./labelling_images/dataset"
    DEST_FOLDER="./object_detection_train/workspace/images/test"

    for png_file in "$PNG_FOLDER"/*.png; do
        base_name=$(basename "$png_file" .png)
        txt_file="$TXT_FOLDER/$base_name.xml"
        
        if [ -f "$txt_file" ]; then
            cp "$txt_file" "$DEST_FOLDER/"
            echo "Copied: $txt_file to $DEST_FOLDER"
        else
            echo "No matching .xml file found for $png_file"
        fi
    done

    echo ======================================================================================
    echo Completed copying and building the image to train the object detection model
    echo ======================================================================================

    docker build -t object_detection_train -f ./object_detection_train/docker/Dockerfile .

    echo ===============================================================================================
    echo Created the docker image titled object_detection_train and training the object detection model
    echo ===============================================================================================

    docker-compose -f ./object_detection_train/docker/docker-compose.yml up

    docker-compose -f ./object_detection_train/docker/docker-compose.yml down

    echo ===================================================================================================
    echo Completed training the object detection model and now running object detection on real time camera
    echo ===================================================================================================

    docker-compose -f ./object_detection/docker/docker-compose.yml up

    docker-compose -f ./object_detection/docker/docker-compose.yml down

    echo ===================================================================================================
    echo Completed the pipeline!!!
    echo ===================================================================================================

else

    echo ===================================================================================================
    echo No .STL file found in the folder. Place the geometric model in ./geometric_model folder
    echo ===================================================================================================

fi