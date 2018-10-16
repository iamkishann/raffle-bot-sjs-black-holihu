import requests, random, time, json, threading
from threading import Thread
from time import sleep
from time import gmtime, strftime
from datetime import datetime
from faker import Faker
import functools
from random import getrandbits
import datetime
from python_anticaptcha import AnticaptchaClient, NoCaptchaTaskProxylessTask



print ("#########################################################")
print ("        SJSRAFFLEBOT  DEVELOPED BY @IAMKISHANN ©.        ")
print ("#########################################################")

def main():

    faker = Faker()
    s = requests.Session()
    s.headers = {
            'origin':'https://slamjamsocialism-drops.com',
            'referer':'https://slamjamsocialism-drops.com/drops/55',
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
    s.headers.update()
    requrl = "https://slamjamsocialism-drops.com/graphql"



########edit  this##########
    size = ['5', '5 ½', '6 ½', '6', '7', '7 ½', '8', '8 ½', '9', '9 ½', '10', '10 ½', '11']
    fname = faker.first_name()
    lname = faker.last_name()
    #change to your domain
    mail = [fname + lname + "{}@email1.club".format(getrandbits(20)), fname + lname + "{}@email2.club".format(getrandbits(20)) ]
    email = random.choice(mail)
    a = functools.partial(random.randint, 0, 9)
    phone = "{}{}{}{}{}{}{}{}{}{}".format(a(), a(), a(), a(), a(), a(), a(), a(), a(), a())
    api_key = ("xxx") #add ur anticap api key
#####################

    site_key = '6LfYhz0UAAAAAJFKp28Sg0NnAEIPMfKI1RJSGsdB'  # grab from site
    url = 'https://slamjamsocialism-drops.com/drops/55'

    client = AnticaptchaClient(api_key)
    task = NoCaptchaTaskProxylessTask(url, site_key)
    job = client.createTask(task)
    job.join()
    solved_captcha = (job.get_solution_response())

    raw_date = datetime.datetime.now()
    r_date = str(raw_date).split(' ')[0]
    r_time = str(raw_date).split(' ')[1].split('.')[0]
    date_time = '{}T{}+00:00'.format(r_date, r_time)

    data = {"query":"mutation RequestOrdertMutation($data: OrderRequestInput!) {\n  requestOrder(data: $data)\n}\n","operationName":"RequestOrdertMutation","variables":{"data":{"firstName":fname,"lastName":lname,"email":email,"phone":phone,"country":"840","city":"Artesia","order":[{"product":"50","size":random.choice(size)}],"raffle":"55","captcha":solved_captcha,"date":date_time}}}


    re = s.post(requrl, json=data)
    
    if "true" in re.text:
        print(date_time, "Entry Successful with ", email, "success")
    else:
        print("Error submitting entry", "error")       

while True:
    threads = []
    for i in range(30):
        t = threading.Thread(target=main)
        threads.append(t)
        t.start()
    main()
    #time.sleep(2)
