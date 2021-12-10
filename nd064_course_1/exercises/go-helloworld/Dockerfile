FROM golang:alpine

LABEL maintainer="Khalil Zouhar"

WORKDIR /go/src/app

ADD . .

RUN go build -o helloworld

EXPOSE 6111

CMD [ './helloworld']