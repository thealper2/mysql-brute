# mysql-brute

MySQL servisine kaba kuvvet saldırı yapmak için kullanılan bir araçtır.

## Gereksinimler

mysql-brute aşağıdaki kütüphaneleri kullanır.

* Colorama
* Mysql

## Kurulumu

Projeyi klonlamak için;

```python
git clone https://github.com/thealper2/mysql-brute.git
```
Gerekli kütüphaneleri kurmak için;

```python
python -m pip install -r requirements.txt
```

## Kullanımı

| Parametre | Kullanımı |
| --------- | --------- |
| -v        | Verbose. Çıktı göstermek için kullanılır. |
| -H        | Host. Hedefin IP adresini belirtmek için kullanılır. |
| -u        | User. Saldırı yapılacak kullanıcıyı belirtmek için kullanılır. |
| -U        | Userlist. Saldırı yapılacak kullanıcı adlarının bulunduğu listeyi belirtmek için kullanılır. |
| -p        | Password. Saldırı yapılacak kullanıcının parolasını belirtmek için kullanılır. |
| -d        | Kullanılacak veritabanını belirtmek için kullanılır. |
| -P        | Passwordlist. Saldırı yapılacak kullanıcının parolalarının bulunduğu listeyi belirtmek için kullanılır. |

```bash
usage: mysql_brute.py [-h] [-u U] [-U U] [-p P] [-P P] [-v] [-d D] -H H

MySQL brute force

options:
  -h, --help  show this help message and exit
  -u U        single user
  -U U        user from file
  -p P        single password
  -P P        password from file
  -v          verbose
  -d D        database
  -H H        host
```

## Örnekler

```python
python3 mysql_brute.py -H TARGET_IP -u root -p toor -D users -v
python3 mysql_brute.py -H TARGET_IP -U users.txt -p password -D users
python3 mysql_brute.py -H TARGET_IP -u root -P passwords.txt -D users -v
python3 mysql_brute.py -H TARGET_IP -U users.txt -P passwords.txt -D users-v
```
