# anomaly_detection

This repository is used for anomaly detection of parts using the [anomalib](https://github.com/enrico310786/Image_Anomaly_Detection/tree/main). This is based on the [online](https://medium.com/@enrico.randellini/anomalib-a-library-for-image-anomaly-detection-and-localization-fb363639104f) proceeding as discussed. This would result in providing the anomaly detection of the required dataset.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t anomaly_detection -f Dockerfile .
```


Make sure the locations are right in the docker-compose file for all the repositories and the dataset.


and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it anomaly_detection /bin/bash
```

This would access the running container. Once inside cd into src and run the following command to train the model.

1. The main repo is mounted onto the container in the docker volumes.

2. The first step is to mount the custom dataset. This is acheived by adding the dataset to the src repository. It has the following structure,

    dataset
    |---festo
        |---orange
        |   |---fixed
        |   |---abnormal
        |---black
        |   |---fixed
        |   |---abnormal
        |---silver
        |   |---fixed
        |   |---abnormal


    Add the anomaly images in the abnormal repositories and good images in the fixed repositories.

3. Edit the ./src/Image_Anomaly_Detection-main/data/inspect_FolderDataModule.py to create the data tensors. Edit lines 12, 26-38, 108-118.

4. Now on inside of the container, cd to src/Image_Anomaly_Detection-main/data and run the following command,

```
python3 inspect_FolderDataModule.py
```

5. After this cd to Image_Anomaly_Detection-main repository and run the following command,

```
python3 ./train_anomalib/train_reversedistillation_anomalib.py --dataset_root /root/src/dataset/festo/orange --name_normal_dir fixed --name_wandb_experiment revdist_orange_v1 --name orange --max_epochs 100 --patience 10
```

6. The trained model can be tested using the following command,

```
python3 ./infer_anomalib/test_model.py --path_torch_model /root/src/Image_Anomaly_Detection-main/results/ReverseDistillation/orange/v0/weights/torch/model.pt --path_dataset /root/src/dataset/festo/orange --name orange --dir_result /root/src/Image_Anomaly_Detection-main/results/ReverseDistillation/orange/v0
```

and infer using the following command,

```
python3 ./infer_anomalib/infer_oneshot.py --path_torch_model /root/src/Image_Anomaly_Detection-main/results/ReverseDistillation/orange/v0/weights/torch/model.pt  --path_image /root/src/dataset/festo/orange/abnormal/0068.png --path_result /root/src/Image_Anomaly_Detection-main/results/ReverseDistillation/orange/v0/example_inference.png 
```

## External Dependencies

The following are required to run the project successfully,

1. docker
2. docker compose
3. nvidia docker
4. pytorch gpu
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
