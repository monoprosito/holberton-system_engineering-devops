#!/usr/bin/env bash
# Install a nginx web server listening on port 80.
#
# When querying nginx at its root / with a GET
# request, it returns a page that contains the string
# 'Holberton School'.
#
# Configures a directive of the Nginx server
# to redirect to another page with 301 HTTP Code
#
# Configures a custom 404 page that contains the string
# 'Ceci n'est pas une page'.
#

link="https://www.youtube.com/watch?v=QH2-TGUlwu4"
new_conf="server_name _;\n\trewrite ^/redirect_me/$ $link permanent;"
location_error="location = /404.html {\n\t\troot /var/www/html/;\n\t\tinternal;\n"
error_directive="error_page 404 /404.html;\n\t$location_error"
error_404="}\n\n\t$error_directive\t}"

apt update
apt install -y nginx
ufw allow 'Nginx HTTP'
echo "Holberton School" > /var/www/html/index.html
echo "Ceci n'est pas une page" > /var/www/html/404.html
sed -i "s|server_name\ _;|$new_conf|" /etc/nginx/sites-available/default
sed -i "0,/}/ s|}|$error_404|" /etc/nginx/sites-available/default
service nginx restart
