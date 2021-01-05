# (Chrysanthemum)Multi Chrome instances with proxy
# version : 1.0
# Author: Xiangwei Chen
# Date: 1/2/2021
# Functionality: open browsers with user's link.
#                ( independent proxy apply on every browser you open)
# Usage: access a website with different proxy

from selenium import webdriver
import getpass


# get inputs (url, number of browsers) from user

def get_input():
    global url
    global number

    url = input("Please enter the website link (Please Double Check): ")

    while True:
        try:
            global number
            number = int(input("how many browsers would you like to open: "))
            if number <= 0:
                print("come on man, you are better than this - -")
                continue
            break
        except:
            print("Please enter a number please (1-20)")


# write proxy info to list
def read_proxy():
    global proxy_list

    with open(r'C:\Users\{}\Desktop\proxy.txt'.format(getpass.getuser())) as f:
        for line in f:
            proxy_list.append(line)


# open certain number of chrome (different proxy)
def open_chrome(num):
    for i in range(0, num):
        current_profile = i + 1
        PROXY = str(proxy_list[i])
        # setting the options (profile for chrome)
        options = webdriver.ChromeOptions()
        options.add_argument(
            r'--user-data-dir=C:\Users\{}\Documents\Chrome_Profiles\Chrome_profile_{}\profile_{}'.format(
                getpass.getuser(), str(current_profile), str(current_profile)))
        options.add_argument('--profile-directory=Profile {}'.format(current_profile))
        options.add_argument('--proxy-server=%s' % PROXY)
        # keep browser open
        options.add_experimental_option("detach", True)

        # add options to driver
        driver = webdriver.Chrome(options=options)

        # open snkr account
        driver.get(url)


# use the function below to test

def open_the_one_you_like(the_one):
    options = webdriver.ChromeOptions()
    options.add_argument(
        r'--user-data-dir=C:\Users\{}\Documents\Chrome_Profiles\Chrome_profile_{}\profile_{}'.format(
            getpass.getuser(), str(the_one + 1), str(the_one + 1)))
    options.add_argument('--profile-directory=Profile {}'.format(the_one + 1))
    options.add_argument('--proxy-server=%s' % proxy_list[the_one])
    # keep browser open
    options.add_experimental_option("detach", True)

    # add options to driver
    driver = webdriver.Chrome(options=options)

    # open snkr account
    driver.get(url)


# main function
if __name__ == '__main__':
    # initialization
    url = ''
    number = 0
    proxy_list = list()

    get_input()
    read_proxy()
    open_chrome(number)
