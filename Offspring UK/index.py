import requests
from bs4 import BeautifulSoup as bs
from random import randint
import cfscrape

def generate(prefix, password, num):
	print("")
	accounts = []
	for i in range(int(num)):
		scraper = cfscrape.create_scraper()
		headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'origin': 'https://www.sneakersnstuff.com'
		}
		r = scraper.get("https://www.offspring.co.uk/view/component/registration/submit", headers=headers)
		number = randint(111,9999999)
		email = '{}+{}@gmail.com'.format(prefix, number)
		data = {
        'pageLabel':'login',
        'componentUid':'registration',
        'destPath':'',
        'title':'mr',
        'firstname':'Johnny',
        'lastname':'Pierson',
        'dobDay':'',
        'dobMonth':'',
        'dobYear':'',
        'email':email,
        'confirmEmail':email,
        'password':password,
        'confirmPassword':password,
        'newsletter':'true',
        '_newsletter':'on',
        'registerButton':'Register'
		}
		r = scraper.post("https://www.offspring.co.uk/view/component/registration/submit", data=data, headers=headers)
		if r.status_code == 200:
			accounts.append("{}:{}".format(email, password))
			print("Created Account - {}:{}".format(email, password))
		else:
			print("Failed to generate account!")
	file = open("accounts.txt", "w")
	for account in accounts:
		file.write("{}\n".format(account))
	file.close()
	return

if __name__ == '__main__':
	print("OFFSPRING UK ACC GEN")
	prefix = input("\nEMAIL PREFIX: ")
	password = input("PASSWORD: ")
	num = input("# OF ACCOUNTS: ")
	generate(prefix, password, num)
