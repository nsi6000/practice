# HAProxy

on CentOS
ip a s
> get IP address
systemctl status firewalld
systemctl stop firewalld
systemctl disable firewalld
vi /etc/selinux/config
> change SELINUX=enforcing to SELINUX=disabled
reboot
yum install httpd
systemctl start httpd
systemctl enable httpd
systemctl status httpd
yum install haproxy
vi /var/www/html/index.html
>1 (for first server)
>2 (for second server)
test it by going to IP address in web browser. Should see 1 and 2.
vi /etc/haproxy/haproxy.cfg
>fronted  main *:8080
> comment out the 2 ACL and 1 use_backend lines below with "#".
>backend app
>    server  websrv01 (name of the server) <IP address server 1> check
>    server  websrv02 (name of the server) <IP address server 2> check
systemctl restart haproxy
192.168.12.145:8080
>refresh multiple times. The number change between 1 and 2.

>    server  websrv02 (name of the server) <IP address server 2> backup
=> use the second server as backup. Always use 1 until 1 is down.
systemctl stop httpd on server 1.
refresh browser.
webpage goes on to 2.

in backend app
change "balance roundrobin" to "balance url_param userid"
restart haproxy service
go on webbroswer: <p address>:8080/?userid=1
go on webbroswer: <p address>:8080/?userid=2
go on webbroswer: <p address>:8080/?userid=3
go on webbroswer: <p address>:8080/?userid=4
...

in backend app
change "balance roundrobin" to "balance hdr(User-Agent)"
restart haproxy service
go on webbrowser.
the server changes based on the webbrowser used (firefox, chrome, IE,...).

in backend app
change "balance roundrobin" to "balance first"
restart haproxy service
every connection is sent to the first server until it reachs its limit.

in backend app
change "balance roundrobin" to "balance leastconn"
restart haproxy service
every connection is sent to the server with least connections.

Usage and statistics
in "frontend main *:80".
> stats enable
> stats auth admin:password
> stats hide-version
> stats show-node
> stats refresh 60s
> stats uri /haproxy?stats
go to <IP address>/haproxy?stats


Show access logs
tail -f /var/log/httpd/access_log
=> only shows the access IP address of the HAProxy server, not the "true" incoming IP address.
=> ensure that the ForwardedFor option is enabled in HAPorxy.conf file.
vi /etc/httpd/conf/httpd.conf
=> add {X-Forwarded-For}i as shown below.
> LogFormat "%{X-Forwarded-For}i   <the rest...>   combined
apachectl -t
> Syntax OK
restart httpd service
make new requests by refreshing the webpage.
tail -f /var/log/httpd/access_log
=> shows the true IP address of your laptop. (check with ifconfig)


> ACLs to forward requests to different backends based on content (js, css,...) in request address.
> SSL Termination: add SSL certificates to avoid HAProxy being seen as man-in-the-middle attack.
> Avoid SPOF by creating multiple HAProxy (with the same configuration) as a cluster using "Pacemaker" which will create a Virtual IP address for the whole cluster.
