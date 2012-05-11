###################
 little-ebay
###################
Minimal auction system powered by Django

Overview
========
little-ebay is possibly the lightest auction system ever. Built on top of Django, little-ebay will provide you with the basic functionality of an auction site.
Register, bid, buy, sell and track items on little-ebay. 

Installation
============
example installation on FreeBSD 8.3

#. pkg_add -r python
#. pkg_add -r apache22
#. pkg_add -r ap22-mod_wsgi
#. pkg_add -r py27-sqlite3
#. pkg_add -r py27-virtualenv
#. virtualenv /usr/local/www/pythonenv
#. ln -s /usr/local/lib/python2.7/site-packages/_sqlite3.so /usr/local/www/pythonenv/lib/python2.7/site-packages/
#. source /usr/local/www/pythonenv/bin/activate.csh
#. pip install django
#. pip install pytz
#. pip install django-crispy-forms
#. mkdir /usr/local/www/auction_site
#. cp -r lebay /usr/local/www/auction_site
#. cp -r auction_site /usr/local/www/auction_site
#. add email address in settings.py
#. cd /usr/local/www/auction_site; python manage.py syncdb; python manage.py collectstatic
#. chown -R www:www /usr/local/www/auction_site
#. cp httpd-auction.conf /usr/local/etc/apache22/Includes
#. restart apache (/usr/local/etc/rc.d/apache22 start)

Usage
=====
Create a few item categories from admin.

More
====
Little-eBay was created by Tareque Hossain

for django 1.4 and django-crispy-forms, modified by Seiji Moriya. (moriya9n@gmail.com)

