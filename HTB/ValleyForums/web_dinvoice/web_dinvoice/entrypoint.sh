#!/bin/bash

# Secure entrypoint
chmod 600 /entrypoint.sh

# Initialize & Start MariaDB
mkdir -p /run/mysqld
chown -R mysql:mysql /run/mysqld
mysql_install_db --user=mysql --ldata=/var/lib/mysql
mysqld --user=mysql --console --skip-name-resolve --skip-networking=0 &

# Wait for mysql to start
while ! mysqladmin ping -h'localhost' --silent; do echo "not up" && sleep .2; done

# Generate random password
ADMIN_PASS=$(echo -n $RANDOM | md5sum | head -c 20)

mysql -u root << EOF
CREATE DATABASE dinvoice;

CREATE TABLE dinvoice.users (
    id         INT          NOT NULL AUTO_INCREMENT,
    username   VARCHAR(256) NOT NULL,
    password   VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    UNIQUE (username)
);

INSERT INTO dinvoice.users (username, password)
VALUES
    ('admin', '${ADMIN_PASS}');

CREATE TABLE dinvoice.invoices (
    id          INT NOT NULL          AUTO_INCREMENT,
    username    VARCHAR(256) NOT NULL,
    invoice     VARCHAR(256) NOT NULL,
    created_at  DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP(),
    PRIMARY KEY (id)
);

GRANT ALL PRIVILEGES ON dinvoice.* TO 'dinvoice'@'%' IDENTIFIED BY 'dinvoice';
FLUSH PRIVILEGES;
EOF

# Generate JWT Secret
export JWT_SECRET=$(echo -n $RANDOM | md5sum | head -c 32)

/usr/bin/supervisord -c /etc/supervisord.conf

