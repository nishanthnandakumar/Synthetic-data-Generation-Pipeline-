# cycle gan

The cycle GAN model is trained using the real and synthetic datasets to transfer the domail of real images onto the synthetic images generated using blender. In this work we try to implement cycle gans using [original code](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). The model is trained for 200 epochs, the images are to be of size 600x600. About 1200 images are used for training the cycle GAN model.

## Getting started

Clone this repository, and make sure the location of the dataset is correct in the docker-compose file.

Run the following commands in the terminal:

```
xhost local:root 
```
Then cd into the docker repository and Run

```
docker build -t cyclegan_train_festo -f Dockerfile .
```
and
```
docker-compose up
```

Now, in another terminal run the following command,

```
docker exec -it cyclegan_train_festo /bin/bash
```
This would access the running container. Once inside cd into src and run the following command to train the model.

```
python3 train.py --dataroot ./datasets/parts --name parts_cyclegan --model cycle_gan
```

To test the model trained and to generate images use the following command,

```
python3 test.py --dataroot ./datasets/parts --name parts_cyclegan --model cycle_gan
```

If we need to continue the training from where it stopped run the following command,

```
python3 train.py --dataroot ./datasets/parts --name parts_cyclegan --model cycle_gan --epoch_count 20 --continue_train
```
Note: epoch_count is the last epoch the training stopped.

The files have been downloaded from the [git repo](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix). The following changes are made to avoid the Runtime error:

1. File1: base.dataset.py: method=transforms.InterpolationMode.BICUBIC to method=Image.BICUBIC
2. File2: test_options.py: parser.add_argument('--num_test', type=int, default=500, help='how many test images to run')

FID score is 80.90006384077262. Try to improve the quality of the images generated.


## Using the RWU Server for training the model

Use the following command to access the server container with the GPU,

```
ssh -p 1922 root@141.69.58.212
```

To upload any files from the local system use the following command,

```
scp -P 1922 -r ./current repo on local system/ root@141.69.58.212:/root/repo on server/

```

To download any files from the local system use the following command,

```
scp -P 1922 -r  root@141.69.58.212:/root/path to the file/repo/on server ./current folder on local system
```

The current best results obtained are with the hyperparameters as saved in the best results repository.

While using the server,

Use screen to run the training.



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

