import os
import tensorflow as tf

def validate_tfrecord(filepath):
    try:
        dataset = tf.data.TFRecordDataset(filepath)
        for _ in dataset:
            pass  # Successfully read at least one record
        return True
    except:
        return False

# Replace with your dataset path
data_dir = "/raid/local/cvml_user/pjs/modified_libero_rlds/"
corrupted_files = []
for f in os.listdir(data_dir):
    if f.endswith(".tfrecord"):
        if not validate_tfrecord(os.path.join(data_dir, f)):
            corrupted_files.append(f)
print("Corrupted files:", corrupted_files)
