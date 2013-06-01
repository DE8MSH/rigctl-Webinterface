rigctl-Webinterface
===================

rigctl Webinterface for Raspberry Pi

Usage:

*** Install hamlib-uitls

sudo apt-get install libhamlib-utils

*** Create directory named 'web' and clone repo

cd ~/

git pull https://github.com/DE8MSH/rigctl-Webinterface.git

cd rigctl-Webinterface

chmod +x cgi-bin/set.cgi

*** Start webservice

python -m CGIHTTPServer 8092

Now start browser and control rx via webinterface on rpiip:8092.


Big 'thank you' must go to Youtube edy555san for his RTLSDR webiterface that inspires me.

> http://ttrftech.tumblr.com/post/38016199555/receiving-amature-radio-using-rtl2832u-and-browser

And to DK7MW for his idea to remote control a rig with help of CGI script and Icecast2 server for sound-over-ip

> http://www.darc.de/cq-dl/cq-dl-digital volume CQDL 06-2013 

Thank you, guys!

===================

Todo:

Clean up
Expand functions 
Etc pp
