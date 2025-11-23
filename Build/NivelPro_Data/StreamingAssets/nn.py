import csv
import os
input_file = "Assets/StreamingAssets/11.csv"
output_file = "Assets/StreamingAssets/leadercards.csv"


with open(input_file, "r", encoding="cp949", newline='') as f_in, \
     open(output_file, "w", encoding="cp949", newline='') as f_out:
    
    reader = csv.reader(f_in)
    writer = csv.writer(f_out)
    
    for row in reader:
        # 각 셀 안의 줄바꿈을 \n 문자열로 치환
        new_row = [cell.replace("\r\n", "\\n").replace("\n", "\\n").replace("\r", "\\n") for cell in row]
        writer.writerow(new_row)

print(f"CSV 내부 줄바꿈 치환 완료! 저장된 파일: {output_file}")
