FROM golang:alpine3.19

# Install system packeges
RUN apk add --update --no-cache supervisor

COPY config/supervisord.conf /etc/supervisord.conf

# Copy challenge files
COPY challenge /app

# Copy flag
COPY flag.txt /flag.txt

WORKDIR /app

RUN go mod download

RUN go build -o /app/main *.go

EXPOSE 1337

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]