FROM python:3.8
COPY requirements.txt /usr/src/app/
COPY app.py /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
EXPOSE 5000
CMD ["python3", "/usr/src/app/app.py"]
