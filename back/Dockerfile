FROM python:3.11-alpine

RUN apk add --no-cache make

COPY src/ ./src/
COPY Makefile ./

RUN make install

CMD ["make", "run"]