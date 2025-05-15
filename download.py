import os
import json
import subprocess

# 심볼릭 링크 생성
link_path = "DATA_DIR"
target_path = "/raid/local/cvml_user/pjs"

if not os.path.exists(link_path):
    subprocess.run(["ln", "-s", target_path, link_path])
    print(f"Created symbolic link {link_path} -> {target_path}")
else:
    print(f"Symbolic link {link_path} already exists")

# 데이터셋 로드 및 저장
# pip install datasets
from datasets import load_dataset

dataset = load_dataset("openvla/modified_libero_rlds")

save_dir = "./modified_libero_rlds"
os.makedirs(save_dir, exist_ok=True)

for split_name, split_data in dataset.items():
    save_path = os.path.join(save_dir, f"{split_name}.jsonl")
    with open(save_path, "w", encoding="utf-8") as f:
        for example in split_data:
            json_line = json.dumps(example, ensure_ascii=False)
            f.write(json_line + "\n")
    print(f"Saved {split_name} split to {save_path}")