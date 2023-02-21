# GYM API

```bash
#------------- 실행을 위한 가상환경 설치 -------------#
python3 -m venv venv # 가상환경 생성
pip3 install poetry  # poetry 설치
poetry install       # pyproject.toml 을 기반으로 하여 필요한 패키지 설치
#-----------------------------------------------#

#------------- 실행을 위한 가상환경 설치 -------------#
# PostgreSQL 이 먼저 실행되어야 합니다.
alembic upgrade head
uvicorn app.main:app --reload
```