import tensorflow as tf

def is_tfrecord_corrupted(tfrecord_file):
    try:
        dataset = tf.data.TFRecordDataset(tfrecord_file)
        for _ in dataset:
            pass
        print(f"TFRecord file {tfrecord_file} is valid")
        return False
    except tf.errors.DataLossError:
        print(f"TFRecord file {tfrecord_file} is corrupted")
        return True
        
# Check all TFRecord files in your directory
import glob
files = glob.glob("DATA_DIR/modified_libero_rlds/**/*.tfrecord", recursive=True)
for file in files:
    is_tfrecord_corrupted(file)
