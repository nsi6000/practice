# Alpine

* apk search -v <software_name> | sort
* apk info -vv | sort
* apk add -u <software_name> //upgrade only one package.
* apk update && apk upgrade //upgrade all packages.
* apk add <software_name>
* apk del <software_name>


# Bash commands

* CTRL+L //clears the screen.
* ls -la
* cd .. ~ - / path
* pwd
* mv -v
* cp -v
* rm
* rm -rf
* dd if=file of=file bs=128k
* du -h
* df -h
* cat
* echo
* cal
* date
* uptime
* tar
* id
* uname -a / id / whoami
* su
* mkdir
* vim
* ps -aux
* kill(all) PID
* grep / sed / awk.
* ping URL.
* tar -c(z)vf / -x(z)vf / -t(z)vf file.
* CTRL+C / CTRL+D / CTRL+S.
* CTRL+L.
* shutdown -h/-r now
* chown 777 file
* bc
* !<COMMAND-STRING> //rerun a command.
* sudo !! //rerun previous command as sudo.
* service apache2 start //start service.
* service apache2 stop //stop service.
* python -m SimpleHTTPServer 80
* ping google.com -c 10 > ip.txt
* sort -o <output-file> <input-file>
* mkdir foo && cd "$_" //make directory and cd to it.
* adduser -m myuser && su - myuser //make user and go to it.
----------
* curl cht.sh/:intro
* curl cht.sh/python/append+file
* curl cht.sh/java/Array
----------
* fdisk
* mount / umount
* PS1="\W\$"
* cat /etc/shells

## basic IP sweep script
```bash
vim ipsweep.sh
```
```bash
#!/bin/bash

if [ "$1" == "" ] then
  echo "forgot ip. syntax: ./ipsweep.sh <ip-address>"
else
  for ip in `seq 1 254`; do
    ping -c $1.$ip | grep "64 bytes" |cut -d " " -f 4 | tr -d ":" &
  done
fi
```
```bash
./ipsweep.sh <ip-address> > iplist.txt
for ip $(cat iplist.txt); do nmap -sS -p 80 -T4 $ip & done
```


# Alpine packages

* bash
* vim
* make //compile linux kernel.
* git
* wget|curl
* gcc //compile linux kernel.
* libc-dev //required to compile with GCC.
* binutils //compile linux kernel.
* gdb
* radare2
* nasm


