FROM python:3.14-alpine
WORKDIR /app
ENV FASTAPI_APP=main.py
ENV FASTAPI_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "-m" ,"uvicorn", "app.main:app","--host","0.0.0.0", "--port", "8000", "--reload"]