# Python 3.9 버전의 슬림 이미지(불필요한 패키지 제거된 경량 이미지)를 기반으로 사용
FROM python:3.9-slim

# 컨테이너 내 작업 디렉터리를 /app으로 설정
WORKDIR /app

# 현재 디렉터리의 fetch_flights.py 파일을 컨테이너의 /app으로 복사
COPY fetch_flights.py .

# entrypoint.sh 스크립트를 컨테이너의 /app으로 복사
COPY entrypoint.sh .

# entrypoint.sh 실행 권한 부여
RUN chmod +x entrypoint.sh

# Python 패키지 requests 설치 (API 요청을 위한 라이브러리)
RUN pip install requests

# 컨테이너 시작 시 entrypoint.sh 스크립트를 실행
CMD ["./entrypoint.sh"]
