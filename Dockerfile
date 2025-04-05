FROM python:3.11
WORKDIR /app
COPY app.py requirements.txt HKBU_ChatGPT.py ./
RUN pip install --upgrade pip && pip install -r requirements.txt



#ENV TELE_ACCESS_TOKEN=7742600615:AAGyw6sKWtwkGasBwQLyG7pZKMRYB51zEBI
#ENV REDIS_HOST=redis-10223.crce178.ap-east-1-1.ec2.redns.redis-cloud.com
#ENV REDIS_PASSWORD=pvSmEnD23qCB3zMTpicyTpnsKQQobu82
#ENV REDIS_PORT=10223
#ENV REDIS_DECODE_RESPONSE=true
#ENV REDIS_USER_NAME=default
#ENV LLM_BASIC_URL=https://genai.hkbu.edu.hk/general/rest
#ENV LLM_MODEL_NAME=gpt-4-o-mini
#ENV LLM_API_VERSION=2024-05-01-preview
#ENV LLM_ACCESS_TOKEN=b2d166f0-cb72-433e-b627-ea26451a45fd
ENTRYPOINT ["python","app.py"]

#LABEL authors="yuanbao"
#ENTRYPOINT ["top", "-b"]