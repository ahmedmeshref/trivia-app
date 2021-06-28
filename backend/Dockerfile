FROM python:3-alpine
WORKDIR /app
ENV IBM_POSTGRESQL=postgresql://admin:1742afec2c77858b1e67fa0272e237877dc46fec1876a830271f@2d68da9f-7d5f-4308-8a4a-a6d1c3619015.68ea2cbd8c8d4c30b5b8450be6b8593a.databases.appdomain.cloud:30375/
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD [ "python", "wsgi.py" ]