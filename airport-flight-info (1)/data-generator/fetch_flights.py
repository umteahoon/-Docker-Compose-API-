import requests  # HTTP 요청을 보내기 위한 모듈
import xml.etree.ElementTree as ET  # XML 데이터를 파싱하기 위한 모듈
import json  # JSON 파일 저장을 위한 모듈
import os  # 디렉토리 생성 등 파일 시스템 조작을 위한 모듈
from datetime import datetime  # 현재 날짜와 시간을 가져오기 위한 모듈

# 공공데이터포털에서 발급받은 API 키
API_KEY = "발급받은 API 키"

# 항공편 정보 조회 API의 기본 URL
URL = "http://apis.data.go.kr/B551177/StatusOfPassengerFlightsDeOdp/getPassengerArrivalsDeOdp?"

# 현재 날짜 및 시간 포맷팅
now = datetime.now()
today = now.strftime('%Y%m%d')  # 오늘 날짜 (예: 20250604)
hour = now.strftime('%H%M')     # 현재 시간 (예: 1430)

# API 호출 시 필요한 파라미터 정의
params = {
    'serviceKey': API_KEY,  # 인증 키
    'pageNo': '1',          # 페이지 번호
    'numOfRows': '100',     # 한 번에 가져올 데이터 수
    'type': 'xml',          # 응답 포맷 (xml)
    'lang': 'K',            # 언어 (K: 한국어)
    'from_time': hour,      # 검색 시작 시간
    'to_time': '2359',      # 검색 종료 시간 (하루 끝까지)
}

# 데이터를 API에서 가져오는 함수
def fetch_data():
    response = requests.get(URL, params=params)  # GET 요청
    print("응답 코드:", response.status_code)    # HTTP 응답 코드 출력
    print("응답 내용:", response.text[:300])     # 응답 내용 일부 출력

    # 응답 코드가 200이 아니면 실패 처리
    if response.status_code != 200:
        print("API 호출 실패:", response.status_code)
        return []

    # XML 파싱 시도
    try:
        root = ET.fromstring(response.text)
    except ET.ParseError:
        print("XML 파싱 오류")
        return []

    # 항공편 정보를 담고 있는 items 요소 찾기
    items = root.find('.//items')
    if items is None:
        print("데이터가 없습니다.")
        return []

    # 항공편 정보를 리스트로 저장
    flights = []
    for item in items.findall('item'):
        flight = {}
        for child in item:
            flight[child.tag] = child.text  # 각 태그의 텍스트를 딕셔너리로 저장
        flights.append(flight)
    return flights

# JSON 형식으로 데이터를 저장하는 함수
def save_json(data):
    os.makedirs('output', exist_ok=True)  # output 디렉토리 생성 (없을 경우)
    with open('output/flights.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)  # JSON 저장
    print("✅ JSON 저장 완료!")

# HTML 형식으로 데이터를 저장하는 함수
def save_html(data):
    os.makedirs('output', exist_ok=True)  # output 디렉토리 생성

    # 항공사 이름 기준으로 데이터 정렬 (airline 또는 airlineNm 필드 사용)
    sorted_data = sorted(data, key=lambda x: x.get('airline', x.get('airlineNm', '')))

    # HTML 파일 생성
    with open('output/flights.html', 'w', encoding='utf-8') as f:
        f.write("<html><head><meta charset='UTF-8'><title>Flight Info</title></head><body>")
        f.write("<h1>도착 항공편 정보 (항공사 이름순 정렬)</h1>")
        f.write("<table border='1'><tr><th>항목</th><th>내용</th></tr>")

        for flight in sorted_data[:20]:  # 최대 20개의 항공편만 출력
            f.write("<tr><td colspan='2'>--- 항공편 ---</td></tr>")
            for key, value in flight.items():
                f.write(f"<tr><td>{key}</td><td>{value}</td></tr>")
        f.write("</table></body></html>")

    print("✅ HTML 저장 완료!")

# 메인 실행 부분
if __name__ == "__main__":
    data = fetch_data()  # 항공편 데이터 요청
    if data:
        print(f"{len(data)}개의 항공편 데이터를 가져왔습니다.")
        save_json(data)  # JSON 저장
        save_html(data)  # HTML 저장
    else:
        print("항공편 데이터를 가져오지 못했습니다.")
