import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import classification_report, confusion_matrix, ConfusionMatrixDisplay, accuracy_score
import pandas as pd

# ----- PARAMETERS -----
MODEL_PATH = "./saved_model/binary_classifier.keras"
TEST_DIR = "./test_dataset"
RESULT_DIR = "./result"
IMG_SIZE = (224, 224)
BATCH_SIZE = 32

os.makedirs(RESULT_DIR, exist_ok=True)

# ----- LOAD MODEL -----
model = tf.keras.models.load_model(MODEL_PATH)

# ----- LOAD TEST DATA -----
test_datagen = ImageDataGenerator(rescale=1. / 255)

test_data = test_datagen.flow_from_directory(
    TEST_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='binary',
    shuffle=False
)

# ----- PREDICTIONS -----
y_pred_probs = model.predict(test_data)
y_pred = (y_pred_probs > 0.5).astype(int).flatten()
y_true = test_data.classes

# ----- CLASS LABELS -----
# Auto-detect class names
index_to_class = {v: k for k, v in test_data.class_indices.items()}

# Make sure to include all classes that appear in either y_true or y_pred
unique_labels = np.unique(np.concatenate((y_true, y_pred)))
unique_labels = [label for label in unique_labels if label in index_to_class]
display_labels = [index_to_class[i] for i in unique_labels]

# ----- CONFUSION MATRIX -----
cm = confusion_matrix(y_true, y_pred, labels=unique_labels)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=display_labels)
disp.plot(cmap='Blues')
plt.title("Confusion Matrix (Test Data)")
plt.savefig(os.path.join(RESULT_DIR, "confusion_matrix.png"))
plt.close()

# Save as CSV
cm_df = pd.DataFrame(cm, index=display_labels, columns=display_labels)
cm_df.to_csv(os.path.join(RESULT_DIR, "confusion_matrix.csv"))

# ----- CLASSIFICATION REPORT -----
report_txt = classification_report(y_true, y_pred, target_names=display_labels)
with open(os.path.join(RESULT_DIR, "classification_report.txt"), "w") as f:
    f.write(report_txt)

# ----- ACCURACY -----
accuracy = accuracy_score(y_true, y_pred)
with open(os.path.join(RESULT_DIR, "accuracy.txt"), "w") as f:
    f.write(f"Accuracy: {accuracy:.4f}")

print("✅ Evaluation complete. Files saved in:", RESULT_DIR)