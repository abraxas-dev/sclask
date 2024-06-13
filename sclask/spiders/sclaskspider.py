import random
import re
import string
import time

import scrapy
from scrapy import FormRequest


class SclaskspiderSpider(scrapy.Spider):
    name = "sclaskspider"
    username = None
    password = None
    url = "http://127.0.0.1"
    port = "8000"
    origin_url = url + ":" + str(port)

    def __init__(self, username=None, password=None, *args, **kwargs):
        super(SclaskspiderSpider, self).__init__(*args, **kwargs)
        if username == None and password == None:
            username_input = input("Enter your username. If you don't have an account, it will be created automatically, just press Enter\n")
            if username_input.strip():
                password_input = input("Now enter you password. If you don't have an account, it will be created automatically, just press Enter\n")
                if password_input.strip():
                    self.username = username_input
                    self.password = password_input
        port_input = input("Enter your port, otherwise the default 8000 will be taken\n")
        if port_input.strip():
            self.origin_url = self.url + ":" + str(port_input)


    def start_requests(self):
        if self.username is None and self.password is None:
            self.username, self.password = self.generate_username_and_password()
        yield from self.login()

    def login(self):
        with open('my_profile.txt', 'a') as f:
            f.write("Username: " + str(self.username) + "; Password : " + str(self.password) + "\n")
        self.output('login', self.username)
        yield FormRequest(url=self.origin_url + "/auth/login", formdata={'username' : self.username, 'password' : self.password}, callback=self.parse_number, dont_filter=True)

    def parse_number(self, response):
        text_parse = response.css('main p::text').get()
        number = re.search(r'\d+', text_parse).group()
        self.output('parse_number', number)
        yield FormRequest(url= self.origin_url + "/check", formdata={'number' : number}, callback=self.check_number, dont_filter=True)

    def check_number(self, response):
        if "You have already entered this number !" in response.text:
            self.output('check_number', 0)
            time.sleep(30)
        else:
            self.output('check_number', 1)
        yield FormRequest(url = self.origin_url + "/profile", callback=self.check_points, dont_filter=True)

    def check_points(self, response):
        text_profile = response.css('main p::text').get()
        points = int(re.search(r'\d+', text_profile).group())
        if (points >= 100):
            self.output('check_points', points)
        else:
            yield FormRequest(url = self.origin_url, callback=self.parse_number, dont_filter=True)

    def generate_username_and_password(self, length_username = 10 ,length_password = 15):
        chars = string.ascii_letters + string.digits
        username = ''.join(random.choice(chars) for _ in range(length_username))
        password = ''.join(random.choice(chars) for _ in range(length_password))
        return username, password

    def output(self, option, parameter = None):
        output = ""
        match option:
            case 'login':
                output = "Your username : {}".format(parameter)
            case 'check_number':
                if (parameter):
                    output = "Yeah + 10 Points !"
                else:
                    output = "Scrapy is sleeping..."
            case 'check_points':
                output = "Done :) You have already scored enough points! Your points : {}".format(parameter)
            case 'parse_number':
                output = "Scrapy got number: {}".format(parameter)
        print('-' * 80 + "\n\n" + output + "\n\n" + '-' * 80)