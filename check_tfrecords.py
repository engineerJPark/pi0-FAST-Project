import tensorflow as tf
import glob
import os

def check_tfrecords(directory):
    print(f"검사 중인 디렉토리: {directory}")
    files = glob.glob(f"{directory}/**/*.tfrecord", recursive=True)
    print(f"발견된 TFRecord 파일 수: {len(files)}")
    
    for file in files:
        print(f"파일 확인 중: {file}")
        try:
            dataset = tf.data.TFRecordDataset(file)
            count = 0
            for _ in dataset:
                count += 1
            print(f"  - 유효한 레코드 수: {count}")
        except tf.errors.DataLossError:
            print(f"  - 오류: 파일이 손상되었습니다")
        except Exception as e:
            print(f"  - 오류: {str(e)}")

# 여기에 검사할 디렉토리 경로 지정
check_tfrecords("DATA_DIR/modified_libero_rlds/")