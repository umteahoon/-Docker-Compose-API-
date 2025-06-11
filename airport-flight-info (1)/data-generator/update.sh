#!/bin/bash

echo "🔄 항공편 정보 업데이트 시작..."

# Python 스크립트 실행
python3 fetch_flights.py

# 결과 확인
if [ $? -eq 0 ]; then
    echo "✅ 업데이트 성공!"
else
    echo "❌ 업데이트 실패!"
fi
#!/bin/bash

echo "🔄 항공편 정보 업데이트 시작..."

# Python 스크립트 실행
python3 fetch_flights.py

# 결과 확인
if [ $? -eq 0 ]; then
    echo "✅ 업데이트 성공!"
else
    echo "❌ 업데이트 실패!"
fi
