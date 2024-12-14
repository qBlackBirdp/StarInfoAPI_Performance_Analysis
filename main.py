import pandas as pd
import matplotlib.pyplot as plt

# CSV 파일 경로
maria_csv = "results_maria.csv"
postgres_csv = "results_postgres.csv"

# CSV 파일 읽기
maria_data = pd.read_csv(maria_csv)
postgres_data = pd.read_csv(postgres_csv)

# 요청 타입을 URL에서 추출하여 새로운 컬럼 'request_type' 추가
maria_data['request_type'] = maria_data['URL'].str.extract(r'/db_test/(\w+)/mariadb')
postgres_data['request_type'] = postgres_data['URL'].str.extract(r'/db_test/(\w+)/postgres')

# CRUD 별 평균 응답 시간 계산
maria_avg_by_type = maria_data.groupby('request_type')['elapsed'].mean()
postgres_avg_by_type = postgres_data.groupby('request_type')['elapsed'].mean()

print("MariaDB Average Response Time by Type:")
print(maria_avg_by_type)

print("\nPostgres Average Response Time by Type:")
print(postgres_avg_by_type)

# 그래프 생성
plt.figure(figsize=(12, 8))
bar_width = 0.35  # 막대 너비
index = range(len(maria_avg_by_type))  # 요청 타입 개수만큼 인덱스 생성

plt.bar(index, maria_avg_by_type, bar_width, label='MariaDB', color='blue')
plt.bar([i + bar_width for i in index], postgres_avg_by_type, bar_width, label='PostgreSQL', color='green')

# x축 설정
plt.xticks([i + bar_width / 2 for i in index], maria_avg_by_type.index, rotation=45)
plt.title("Average Response Time by Request Type")
plt.xlabel("Request Type")
plt.ylabel("Average Response Time (ms)")
plt.legend()

# 그래프 저장
plt.savefig("average_response_time_by_request_type.png")
plt.show()
