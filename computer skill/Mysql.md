# Mysql8

```shell
set -u
set -e
cd /home/rxy/tmp
wget https://cdn.mysql.com//Downloads/MySQL-8.0/mysql-8.0.19-linux-glibc2.12-x86_64.tar.xz
tar -xzvf mysql-8.0.19-linux-glibc2.12-x86_64.tar.xz
mv mysql-8.0.19-linux-glibc2.12-x86_64 /usr/local/mysql
cd /usr/local/mysql
useradd -r -s /sbin/nologin mysql
chown -R mysql.mysql /usr/local/mysql
yum remove mariadb-libs
yum -y install numactl
bin/mysqld --initialize --user=mysql > tmp_pwd.txt
cp support-files/mysql.server /etc/init.d/mysql
service mysql start
```

