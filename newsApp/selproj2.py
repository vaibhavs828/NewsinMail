# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 10:03:05 2020

@author: vaibh
"""

def main():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import datetime, time, os
    import smtplib
    from email.message import EmailMessage

    #Storing Date

    td = datetime.date.today()
    
    #Assign path variables
    GOOGLE_CHROME_PATH = '/app/.apt/usr/bin/google_chrome'
    CHROMEDRIVER_PATH = '/app/.chromedriver/bin/chromedriver'

    #web-driver for chrome

    wait_time = 10#waits for 10 seconds to get the news//if possible will take less time
    #chr_op = webdriver.ChromeOptions()
    #chr_op.add_experimental_option('useAutomationExtension',False)#The useAutomationExtension: false option disables    the driver to install other chrome extensions, such as CaptureScreenshot and others.
    #chr_op.add_argument('--start-maximized')
    #driver = webdriver.Chrome(r'C:\Users\vaibh\OneDrive\Desktop\chromedriver.exe',options=chr_op)
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.binary_location = GOOGLE_CHROME_PATH
    
    #Building the browser
    driver = webdriver.Chrome(execution_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

    #Connection to google news
    print('Collecting news from Google News...\n')
    google_news = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"
    print (" ------------------------------------------------------------------------------------------- ")
    print (">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  TODAY's TOP NEWS HEADLINES  <<<<<<<<<<<<<<<<<<<<<<<<<<<<< ")
    print("Date : ",td.strftime("%b-%d-%Y"))
    print("\n")

    driver.get(google_news)
    driver.implicitly_wait(wait_time)
    elements = driver.find_elements_by_tag_name('h3')

    #Writing in a text file
    file_loc = 'newsfile.txt'
    file_to_write = open(file_loc,'w+')
    file_to_write.write("Today's Top News Headlines\n")
    ind = 1
    for i in elements:
        file_to_write.write(str(ind)+ ") ")
        file_to_write.write(i.text+'\n')
        ind+=1
    file_to_write.close()
    print("\n")
    #driver.quit()

    #Appendin World news to it
    driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN& ceid=IN%3Aen')
    driver.implicitly_wait(wait_time)
    element2 = driver.find_elements_by_tag_name('h3')

    #Appending
    file_ap = open(file_loc, 'a')
    file_ap.write("\nWorld news\n")
    index=1
    for j in element2:
        file_ap.write(str(index)+ ") ")
        file_ap.write(j.text+'\n')
        index+=1
        if index ==7:
            break
    file_ap.close()

    #Appending business news to it

    driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN& ceid=IN%3Aen')
    driver.implicitly_wait(wait_time)
    element3 = driver.find_elements_by_tag_name('h3')

    #Appending
    file_ap2 = open(file_loc, 'a')
    file_ap2.write("\nBusiness News\n")
    index2=1
    for k in element3:
        file_ap2.write(str(index2)+ ") ")
        file_ap2.write(k.text+'\n')
        index2+=1
        if index2 ==7:
            break
    file_ap2.close()

    #Appending sports news to it

    driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN& ceid=IN%3Aen')
    driver.implicitly_wait(wait_time)
    element4 = driver.find_elements_by_tag_name('h3')

    #Appending
    file_ap3 = open(file_loc, 'a')
    file_ap3.write("\nSports News\n")
    index3=1
    for l in element4:
        file_ap3.write(str(index3)+ ") ")
        file_ap3.write(l.text+'\n')
        index3+=1
        if index3 ==7:
            break
    file_ap2.close()




    driver.quit()



    #E-mail part

    from newsApp import myEnvVar
    myEnvVar.setVar()
    EMAIL_HOST = os.getenv('EMAIL_HOST')
    EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
    USER_EMAIL = os.getenv('USER_EMAIL')

    # Compose message
    msg = EmailMessage()
    msg['From'] = EMAIL_HOST
    msg['To']   = USER_EMAIL
    msg['Subject'] = " Hello ! Today's TOP news HEADLINES >>"

    with open(file_loc,'rb') as f:
        N_file = f.read()
        #msg.set_content(f.read)

    # Body of email  
    msg.set_content("Find the attached document for detailed NEWS .. ")
    msg.add_attachment(N_file, maintype = 'document',subtype = 'txt', filename = f.name )

    #Configure Server
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_HOST,EMAIL_PASSWORD)
    server.send_message(msg)
    print ("Mail sent")
    server.quit()

if __name__ == "__main__":
    main()
