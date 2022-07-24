

FROM ubuntu:18.04

WORKDIR /app

RUN apt-get update \
  && apt-get -y install tesseract-ocr \
  && apt-get install -y python3 python3-distutils python3-pip \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/*

RUN apt update \
  && apt-get install ffmpeg libsm6 libxext6 -y
RUN pip3 install pytesseract
RUN pip3 install opencv-python
RUN pip3 install pillow
RUN pip3 install python-multipart
RUN apt-get update
RUN apt-get install poppler-utils -y

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt



COPY .. .

ENTRYPOINT ["python3"]
CMD ["deploy.py"]