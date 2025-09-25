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
sudo rm -rf ./blender/src/geometric_model/*
sudo rm -rf ./blender/src/output/model1/*
sudo rm -rf ./crop_images/src/output/*
sudo rm -rf ./crop_images/src/images/*
sudo rm -rf ./data_preprocessing/src/images/blender/*
sudo rm -rf ./data_preprocessing/src/output/blender/*
sudo rm -rf ./data_preprocessing/src/output/real/*
sudo rm -rf ./cgan_train/src/datasets/parts/trainA/*
sudo rm -rf ./cgan_train/src/datasets/parts/testA/*
sudo rm -rf ./cgan_train/checkpoints/*
sudo rm -rf ./cgan_test/results/*
sudo rm -rf ./anomaly_detection_train/src/Image_Anomaly_Detection-main/results/*
sudo rm -rf ./anomaly_detection_train/src/Image_Anomaly_Detection-main/data/__pycache__
sudo rm -rf ./anomaly_detection_train/src/Image_Anomaly_Detection-main/data/datamodule_test.csv
sudo rm -rf ./anomaly_detection_train/src/Image_Anomaly_Detection-main/data/datamodule_train.csv
sudo rm -rf ./anomaly_detection_train/src/Image_Anomaly_Detection-main/data/datamodule_val.csv
sudo rm -rf ./anomaly_detection_train/src/dataset/festo1/fixed/*
###sudo rm -rf ./anomaly_detection_train/results/*
sudo rm -rf ./camera_output/*
sudo rm -rf ./crop_image_camera/src/images/*
sudo rm -rf ./crop_image_camera/src/output/*
sudo rm -rf ./data_preprocess_camera/src/images/*
sudo rm -rf ./data_preprocess_camera/src/output/*
sudo rm -rf ./anomaly_detection_test/image/*
sudo rm -rf ./anomaly_detection_test/output/*

# cp ./geometric_model/cylinder_new.STL ./blender/src/geometric_model/cylinder_new.STL
# cp ./geometric_model/temp_sensor.STL ./blender/src/geometric_model/temp_sensor.STL

# echo ==================================================================================
# echo Finished copyinth the geometric model and Creating the docker image for blender
# echo ==================================================================================

# docker build -t blender_dataset_festo -f ./blender/docker/Dockerfile .

# echo ====================================================================================
# echo Created the docker image titled blender_dataset and Generating the blender images
# echo ====================================================================================

# docker-compose -f ./blender/docker/docker-compose.yml down

# docker-compose -f ./blender/docker/docker-compose.yml up

# docker-compose -f ./blender/docker/docker-compose.yml down

# echo =============================================================
# echo Generated the blender images and copying them to crop images
# echo =============================================================

# cp ./blender/src/output/model1/* ./crop_images/src/images

# echo ====================================================================================================
# echo Generated the blender images and mounted to crop images repository and building the docker image
# echo ====================================================================================================

# docker build -t image_crop -f ./crop_images/docker/Dockerfile .

# echo ==================================================================
# echo Created the docker image titled image_crop and croping the images
# echo ==================================================================

# docker-compose -f ./crop_images/docker/docker-compose.yml up

# docker-compose -f ./crop_images/docker/docker-compose.yml down

# echo =======================================================
# echo Completed croping the images and now data preprocessing
# echo =======================================================

# cp ./crop_images/src/output/* ./data_preprocessing/src/images/blender/

# docker build -t data_preprocessing_festo -f ./data_preprocessing/docker/Dockerfile .

# echo ==================================================================
# echo Created the docker image titled image_crop and croping the images
# echo ==================================================================

# docker-compose -f ./data_preprocessing/docker/docker-compose.yml up

# docker-compose -f ./data_preprocessing/docker/docker-compose.yml down


# echo =================================================================
# echo The preprocessed images are copied to cgan repository
# echo =================================================================

# ls -t ./data_preprocessing/src/output/real/ | tail -n +11 | xargs -I {} cp ./data_preprocessing/src/output/real/{} ./cgan_train/src/datasets/parts/trainB/

# ls -t ./data_preprocessing/src/output/real/ | head -n 10 | xargs -I {} cp ./data_preprocessing/src/output/real/{} ./cgan_train/src/datasets/parts/testB/

# ls -t ./data_preprocessing/src/output/blender/ | tail -n +11 | xargs -I {} cp ./data_preprocessing/src/output/blender/{} ./cgan_train/src/datasets/parts/trainA/

# ls -t ./data_preprocessing/src/output/blender/ | head -n 10 | xargs -I {} cp ./data_preprocessing/src/output/blender/{} ./cgan_train/src/datasets/parts/testA/    

# echo =================================================================
# echo Files Copied to folder and building the docker image
# echo =================================================================

# docker build -t cyclegan_train -f ./cgan_train/docker/Dockerfile .

# echo ====================================================================================
# echo Created the docker image titled cyclegan_train and training the cycle gan model
# echo ====================================================================================

# docker-compose -f ./cgan_train/docker/docker-compose.yml up

# docker-compose -f ./cgan_train/docker/docker-compose.yml down

# echo ====================================================================================
# echo Completed training the cycle gan model and Generating the images using cgan
# echo ====================================================================================

# docker-compose -f ./cgan_test/docker/docker-compose.yml up

# docker-compose -f ./cgan_test/docker/docker-compose.yml down

# echo ============================================================================================
# echo Completed generating the images using cycle gan model and now copying the generated images
# echo ============================================================================================

# find ./cgan_test/results/parts_cyclegan/test_latest/images/ -type f -name '*fake_B*' -exec cp {} ./anomaly_detection_train/src/dataset/festo1/fixed/ \;

# echo ==========================================================
# echo Completed copying the images and now anomaly detection
# echo ==========================================================

# docker build -t anomaly_detection_festo -f ./anomaly_detection_train/docker/Dockerfile .

# echo ====================================================================================
# echo Created the docker image titled anomaly_detection_festo and training the cycle gan model
# echo ====================================================================================

# docker-compose -f ./anomaly_detection_train/docker/docker-compose.yml up

# docker-compose -f ./anomaly_detection_train/docker/docker-compose.yml down

# echo ==================================================================================
# echo Completed training the anamoly detection model and now capturing the camera image
# echo ==================================================================================

    docker-compose -f ./crop_image_camera/docker/docker-compose.yml down

    ids_peak_cockpit

    echo ==================================================
    echo Captured the camera image now cropping the image
    echo ==================================================

    cp ./camera_output/* ./crop_image_camera/src/images/

    docker-compose -f ./crop_image_camera/docker/docker-compose.yml up

    docker-compose -f ./crop_image_camera/docker/docker-compose.yml down

    echo ==========================================
    echo Cropped the image now data preprocessing
    echo ==========================================

    cp ./crop_image_camera/src/output/* ./data_preprocess_camera/src/images/

    docker-compose -f ./data_preprocess_camera/docker/docker-compose.yml up

    docker-compose -f ./data_preprocess_camera/docker/docker-compose.yml down

    echo ==========================================
    echo Running anomaly detection on the image
    echo ==========================================

    cp ./data_preprocess_camera/src/output/* ./anomaly_detection_test/image/

    docker-compose -f ./anomaly_detection_test/docker/docker-compose.yml up

    docker-compose -f ./anomaly_detection_test/docker/docker-compose.yml down

    echo ===================================================================================================
    echo Completed the pipeline!!!
    echo ===================================================================================================

else

    echo ===================================================================================================
    echo No .STL file found in the folder. Place the geometric model in ./geometric_model folder
    echo ===================================================================================================

fi