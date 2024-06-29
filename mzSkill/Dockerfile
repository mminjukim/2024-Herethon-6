# 베이스 이미지로 Python 사용
FROM python:3.12

# 작업 디렉터리 설정
WORKDIR /code

# 종속성 파일 복사 및 설치
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . /code/

# 명령어 설정
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

