import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ----- PARAMETERS -----
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
TEST_DIR = "./test_dataset"
MODEL_PATH = "./saved_model/binary_classifier.keras"

# ----- LOAD TEST DATA -----
test_datagen = ImageDataGenerator(rescale=1./255)
test_data = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)

# ----- LOAD MODEL -----
model = tf.keras.models.load_model(MODEL_PATH)
print(f"✅ Loaded model from {MODEL_PATH}")

# ----- PREDICT ON TEST DATA -----
test_data.reset()
y_probs = model.predict(test_data, verbose=1)
y_pred = (y_probs > 0.5).astype(int).reshape(-1)
y_true = test_data.classes
class_labels = list(test_data.class_indices.keys())

# ----- CONFUSION MATRIX ------
all_class_indices = list(test_data.class_indices.values())  # e.g. [0] if test only has one class

# But model can predict class 0 or 1, so let's define full binary classes:
full_class_indices = [0, 1]

# Mapping for all possible classes (you can define class names manually if needed)
index_to_class = {0: "class0", 1: "class1"}  # replace with your actual class names

# Or get class names from training, e.g.
# index_to_class = {v: k for k, v in train_data.class_indices.items()}

# Make sure to cover all classes that appear in predictions and true labels
unique_labels = np.unique(np.concatenate((y_true, y_pred)))

# Filter unique_labels to only those in your mapping keys
unique_labels = [label for label in unique_labels if label in index_to_class]

display_labels = [index_to_class[i] for i in unique_labels]

cm = confusion_matrix(y_true, y_pred, labels=unique_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)
disp.plot(cmap='Blues')

ax = plt.gca()
ax.set_xticks(np.arange(len(display_labels)))
ax.set_yticks(np.arange(len(display_labels)))

plt.title("Confusion Matrix (Test Data)")
plt.savefig("./result/confusion_matrix.png")
plt.close()

# Save confusion matrix CSV
cm_df = pd.DataFrame(cm, index=display_labels, columns=display_labels)
cm_df.to_csv("./result/confusion_matrix.csv")

# Save classification report
report = classification_report(y_true, y_pred, target_names=display_labels)
with open("./result/classification_report.txt", "w") as f:
    f.write(report)


# Save accuracy
acc = accuracy_score(y_true, y_pred)
with open("./result/accuracy.txt", "w") as f:
    f.write(f"Overall Accuracy: {acc:.4f}\n")