FROM python:3.7
LABEL maintainer="tankov457@gmail.com"

WORKDIR /app
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port
#ENV PORT 8080
EXPOSE 8180
#EXPOSE 8181

COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
