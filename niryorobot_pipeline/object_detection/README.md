# object_detection

This repository is used for object detection of parts using the [SSD ResNet101 V1 FPN 640x640](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf2_detection_zoo.md). This is based on the [online](https://www.youtube.com/watch?v=yqkISICHH-U) proceeding as discussed. This would result in providing the precision, recall, and the loss of the trained model evaluated on the dataset.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t retinanet101 -f Dockerfile .
```


Make sure the locations are right in the docker-compose file for all the repositories and the dataset.


and run 

```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it retinanet101 /bin/bash
```

This would access the running container. Once inside cd into src and run the following command to train the model.

1. The main repo is cloned during building the image, /root/models-master this contains the object detection API for tensorflow.

2. The pre-trained model is also downloaded and unziped during image buid in /root/src/ repository.

3. Add the images repository with train and test folders in workspace.

4. Now on inside of the container, make sure the following folders contain only these files,

5. /root/workspace/annotations should contain only label_map.pbtxt file.

6. /root/workspace/models/my_ssd_resnet/ should contain /export, /tfjsexport, /tfliteexport, and pipeline.config file and repos.

7. Make sure the dataset is present in the /root/workspace/images which should have a train and test repos with images and labels each.

8. Open /root/workspace/annotations/label_map.pbtxt make sure the number of labels, names of labels are right as per the labeling done using labelImg. If not follow the video to correct the same.

9. Now you can verify if the cloned object detection pipeline is working good using the following command,

```
python3 /root/models-master/research/object_detection/builders/model_builder_tf2_test.py
```

This will return OK at the end.

10. After this copy the pipeline.config of the downloaded model to /workspace/models/my_ssd_resnet/ if not available. 

```
cp /root/src/pre_trained_models/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8/pipeline.config /root/workspace/models/my_ssd_resnet/pipeline.config
```

And then open /root/workspace/models/my_ssd_mobnet/pipeline.config and change the num_classes to the number of classes in the project (8) and make sure all the paths to the label_map, fine tuned model, train.record and test.record. in this file are correct.

fine_tune_checkpoint: /root/src/pre_trained_models/ssd_resnet101_v1_fpn_640x640_coco17_tpu-8/checkpoint/ckpt-0

train_input_reader:

label_map_path : /root/workspace/annotations/label_map.pbtxt

tf_record_input_reader : /root/workspace/annotations/train.record

eval_input_reader:

label_map_path : /root/workspace/annotations/label_map.pbtxt

tf_record_input_reader : /root/workspace/annotations/test.record

fine_tune_checkpoint_type: "detection"

Now follow the commands to train and evaluate the model on the daatset.

Use generate_tf record in scripts to create train.record and test.record. Run the following commands from the /root repo.

```
python3 '/root/scripts/generate_tfrecord.py' -x '/root/workspace/images/train' -l '/root/workspace/annotations/label_map.pbtxt' -o '/root/workspace/annotations/train.record'
```

and 

```
python3 '/root/scripts/generate_tfrecord.py' -x '/root/workspace/images/test' -l '/root/workspace/annotations/label_map.pbtxt' -o '/root/workspace/annotations/test.record' 
```

Next step is to train the model using the following command.

```
python3 '/root/models-master/research/object_detection/model_main_tf2.py' --model_dir='/root/workspace/models/my_ssd_resnet' --pipeline_config_path='/root/workspace/models/my_ssd_resnet/pipeline.config' --num_train_steps=1000
```

Run the following command to evaluate the model on the test dataset,

```
python3 '/root/models-master/research/object_detection/model_main_tf2.py' --model_dir='/root/workspace/models/my_ssd_resnet' --pipeline_config_path='/root/workspace/models/my_ssd_resnet/pipeline.config' --checkpoint_dir='/root/workspace/models/my_ssd_resnet/'
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
