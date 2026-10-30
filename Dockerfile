FROM python:3.15
WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY frontend.py frontend.py
EXPOSE 8501

CMD ["streamlit", "run", "frontend.py"]