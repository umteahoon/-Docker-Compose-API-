#!/bin/bash  
# 이 스크립트가 bash 셸에서 실행된다는 것을 명시

# 무한 루프 시작
while true
do
  # Python 스크립트를 실행하여 항공편 데이터를 수집하고 저장
  python fetch_flights.py

  # 5분(300초) 대기 후 다음 실행
  sleep 300
done
