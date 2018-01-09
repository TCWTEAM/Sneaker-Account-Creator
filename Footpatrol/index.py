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
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, link Gecko) Chrome/59.0.3071.115 Safari/537.36',
        'origin': 'https://www.footpatrol.com/'
        }
        number = randint(111,9999999)
        email = '{}+{}@gmail.com'.format(prefix, number)
        data = {
        'email_address':email,
        'password':password,
        'verify_password':password,
        'signup':'Sign Up'
        }
        r = scraper.post("https://www.footpatrol.com/members/", data=data, headers=headers)
        if r.status_code == 200:
            accounts.append("{}:{}".format(email, password))
            print("Created Account - {}:{}".format(email, password))
        else:
            print("Failed to generate account")
    file = open("accounts.txt", "w")
    for account in accounts:
        file.write("{}\n".format(account))
    file.close
    return

if __name__ == '__main__':
    print("FOOTPATROL ACCOUNT GENERATOR")
    print("CREATED BY XO")
    prefix = input("\nEMAIL Prefix: ")
    password = input("PASSWORD: ")
    num = input("# OF ACCOUNTS: ")
    generate(prefix, password, num)
