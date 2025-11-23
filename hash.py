import os
import json
import hashlib

# 해시 계산 함수
def get_file_hash(path):
    md5 = hashlib.md5()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            md5.update(chunk)
    return md5.hexdigest().upper()

# Unity 빌드 폴더 경로 설정
BUILD_DIR = "./Build"     # 여기를 본인의 빌드 폴더 경로로 바꾸면 됩니다
OUTPUT_FILE = "./manifest.json"

file_list = []

for root, dirs, files in os.walk(BUILD_DIR):
    for fname in files:
        full_path = os.path.join(root, fname)
        rel_path = os.path.relpath(full_path, BUILD_DIR).replace("\\", "/")

        file_hash = get_file_hash(full_path)

        file_list.append({
            "path": rel_path,
            "hash": file_hash
        })

        print(f"해시 생성: {rel_path}")

manifest = { "files": file_list }

# JSON 파일 저장
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(manifest, f, indent=4)

print("\nmanifest.json 생성 완료!")
5