# Bing Image Downloader 패키기 설치하기
!pip install bing_image_downloader


# 다운로드할 이미지 키워드와 개수 지정하여 다운로드하기
from bing_image_downloader import downloader
import os

keywords = input("검색할 이미지 키워드를 입력하세요 (예: 노란바나나) => ")
limit = int(input("다운로드할 이미지의 개수를 입력하세요 =>  "))

# 현재 디렉토리의 절대 경로 가져오기
current_directory = os.path.abspath('.')

# 다운로드 정보 기록
record = {
    "keywords": keywords,
    "limit": limit
}

# 이미지 다운로드 실행
downloader.download(
    record['keywords'], 
    limit=record['limit'],
    output_dir=current_directory,  # 현재 디렉토리를 다운로드 경로로 설정
    adult_filter_off=True,
    force_replace=False,
    timeout=60
)
