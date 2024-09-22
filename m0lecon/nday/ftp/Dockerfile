# latest version at the time of writing
FROM node:22.6.0-alpine3.20

RUN apk update && apk add --no-cache vsftpd supervisor
COPY vsftpd.conf /etc/vsftpd/vsftpd.conf

# Set the working directory and add user non root
WORKDIR /home/app
RUN addgroup -S app && adduser -S app -G app

COPY supervisord/supervisord.conf /supervisord.conf

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm install

# Copy the rest of the files
COPY index.js .

ENV NODE_ENV=production

# Expose the port
EXPOSE 3000
EXPOSE 21
EXPOSE 21000-21010

# Start the app
CMD ["supervisord", "-c", "/supervisord.conf"]
