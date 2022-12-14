FROM python:3-alpine
LABEL maintainer="nu11secur1typentest@gmail.com"

WORKDIR /root/
ADD . /root/

RUN apk add \
    gcc \
    musl-dev \
    libffi-dev \
    openssl-dev \
    libffi-dev

RUN pip install -r requirements.txt

ENTRYPOINT ["./insect.py"]
CMD ["--help"]
