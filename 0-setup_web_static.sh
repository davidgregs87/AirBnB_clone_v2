#!/usr/bin/env bash
# A bash script that sets up your web servers for the deployment of web_static

# Update your machine
sudo apt-get -y update
# Install nginx
sudo apt-get -y install nginx
# checking if directory dosen't exist if true we create it
# else don't create it since it already exist

if [ ! -d "/data/" ];
then
        sudo mkdir "/data/"
fi

if [ ! -d "/data/web_static/" ];
then
        sudo mkdir "/data/web_static/"
fi

if [ ! -d "/data/web_static/releases/" ];
then
        sudo mkdir "/data/web_static/releases/"
fi

if [ ! -d "/data/web_static/shared/" ];
then
        sudo mkdir "/data/web_static/shared/"
fi

if [ ! -d "/data/web_static/releases/test/" ];
then
        sudo mkdir "/data/web_static/releases/test/"
fi

echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee "/data/web_static/releases/test/index.html"

# Create a symbolic link, if it already exist delete it
# And it shoulb created every instance the script is ran

if [ -L "/data/web_static/current" ];
then
        sudo rm "/data/web_static/current"
fi

sudo ln -s "/data/web_static/releases/test/" "/data/web_static/current"

# Give ownership to ubuntu for user and group for all members
# of the /data/ folder

sudo chown -R ubuntu:ubuntu /data/

# Re-configure our server with alias
echo "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    root /var/www/html;
    index index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    location /redirect_me {
	return 301 https://stackoverflow.com/;
    }
    
    error_page 404 /404.html;
    location = /404.html {
	root /var/www/html;
	internal;
    }
    add_header X-Served-By \$hostname;
}" > default

sudo mv -f default /etc/nginx/sites-available/default

# Restart nginx
sudo service nginx restart

# Exit program
exit 0
