FROM python:3.11
WORKDIR /app
COPY app.py requirements.txt HKBU_ChatGPT.py ./
RUN pip install --upgrade pip && pip install -r requirements.txt

ENTRYPOINT ["python","app.py"]

#LABEL authors="yuanbao"
#ENTRYPOINT ["top", "-b"]