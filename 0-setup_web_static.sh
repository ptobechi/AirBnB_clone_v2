#!/bin/bash

# check if nginx is installed
if ! command -v nginx &> /dev/null; then
	# update package list
	sudo apt-get update

	# install nginx
	sudo apt-get install -y nginx
fi

# start nginx server
# sudo service nginx start

# create directories for static contents
sudo mkdir -p /var/www/html/web_static
# sudo mkdir -p /data/web_static/releases/test /data/web_static/shared

# create a test html for verification
echo "<html>
	<head>
	<title>Deployed Web static</title>
	</head>
	<body>
	<p>This is a test page for your deployed web static content.</p>
	</body>
	</html>"  | sudo tee /data/web_static/releases/test/index.html

# create a symbolic link to the shared directory
sudo ln -sf /data/web_static/realeses/test /data/web_static/current

# give ownership to the www-data user and group
sudo chown -R ubuntu:ubuntu /data

#update nginx configuratrion
nginx_config="
server {
	listen 80;
	server_name _;

	location /hbnb_static/ {
		alias /data/web_static/current/;
		index index.html;
	}

	location / {
		try_files \$uri \$uri/ =404;
	}
}
"
echo "$nginx_config" | sudo tee /etc/nginx/sites-available/default > /dev/null

# upate nginx confiuration to serve static content
# sudo sed -i 's|server_name localhost;|server_name localhost;\n\n\tlocation /web_static/ {\n\t\talias /data/web_atatic/current/;n\t}\n|' /etc/nginx/site-available/default

# restart service to apply changes
sudo service nginx restart

#display a message indication successful setup
echo "Nginx configured. Access the test page at http://your-server-ip/hbnb_static/"
