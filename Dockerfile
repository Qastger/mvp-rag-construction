FROM python:3.14
WORKDIR /rag
COPY requirements.txt /rag
RUN pip install -r requirements.txt
COPY main.py /rag
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--reload"]