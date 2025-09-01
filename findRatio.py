import pandas as pd

# CSV 파일 불러오기 (파일명 수정하세요)
df = pd.read_csv("./samples.csv")

# 라벨별 개수와 비율 계산
label_counts = df['label'].value_counts()
label_ratios = df['label'].value_counts(normalize=True) * 100
total_count = len(df)

# 출력
for label, count in label_counts.items():
    ratio = label_ratios[label]
    print(f"label == {label}: {count}개 ({ratio:.2f}%)")

print(f"\n전체 샘플 수: {total_count}개")
