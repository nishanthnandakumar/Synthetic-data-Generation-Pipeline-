from anomalib.data.image.folder import Folder
from anomalib import TaskType
from anomalib.data.utils import ValSplitMode

# set the dataset root for a particular category
dataset_root = "/root/src/dataset/festo/orange"

# Create the datamodule
datamodule = Folder(
    name="orange",
    root=dataset_root,
    normal_dir="fixed",
    abnormal_dir="abnormal",
    task=TaskType.CLASSIFICATION,
    seed=42,
    normal_split_ratio=0.2, # default value
    val_split_mode=ValSplitMode.FROM_TEST, # default value
    val_split_ratio=0.5, # default value
    train_batch_size=32, # default value
    eval_batch_size=32, # default value
    image_size=(256,256)
)

# Setup the datamodule
datamodule.setup()