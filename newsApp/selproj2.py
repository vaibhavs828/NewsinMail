

#NAYI SHURUAT


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import datetime, time, os
import smtplib
from email.message import EmailMessage

#Storing Date

td = datetime.date.today()

#web-driver for chrome

wait_time = 10;#waits for 10 seconds to get the news//if possible will take less time
chr_op = webdriver.ChromeOptions()
chr_op.add_experimental_option('useAutomationExtension',False)#The useAutomationExtension: false option disables the driver to install other chrome extensions, such as CaptureScreenshot and others.
chr_op.add_argument('--start-maximized')
driver = webdriver.Chrome(r'C:\Users\vaibh\OneDrive\Desktop\chromedriver.exe',options=chr_op)

#Connection to google news

google_news = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"


driver.get(google_news)
driver.implicitly_wait(wait_time)
elements = driver.find_elements_by_tag_name('h3')

EMAIL_HOST = 'vaibhavlucky991@gmail.com'
EMAIL_PASSWORD = 'pass12345@#'
USER_EMAIL = 'vaibhavs828@gmail.com'

# Compose message
msg = EmailMessage()
msg['From'] = EMAIL_HOST
msg['To']   = USER_EMAIL
msg['Subject'] = " Hello ! Today's TOP news HEADLINES >>"


# Body of email  
msg.set_content("News News News .. ")



#Saving into string
news = ''
ind = 1
for i in elements:
    news += str(ind) + ')'
    news += i.text + '\n'
    ind += 1
    

driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
driver.implicitly_wait(wait_time)
element2 = driver.find_elements_by_tag_name('h3')


#Saving into string
wnews = ''
ind2 = 1
for j in element2:
    wnews += str(ind2) + ')'
    wnews += j.text + '\n'
    ind2 += 1
    if ind2 == 7 :
        break
    

driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
driver.implicitly_wait(wait_time)
element3 = driver.find_elements_by_tag_name('h3')

#Saving into string
bnews = ''
ind3 = 1
for k in element3:
    bnews += str(ind3) + ')'
    bnews += k.text + '\n'
    ind3 += 1
    if ind3 == 7 :
        break



driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen')
driver.implicitly_wait(wait_time)
element4 = driver.find_elements_by_tag_name('h3')

#Saving into string
snews = ''
ind4 = 1
for l in element4:
    snews += str(ind4) + ')'
    snews += l.text + '\n'
    ind4 += 1
    if ind4 == 7 :
        break



driver.quit()

msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
<h3 style="color:SlateGray;">Today's top news headlines</h3>
<pre>
"""+news+"""</pre>
<h3 style="color:SlateGray;">World news headlines</h3>
<pre>
"""+wnews+"""</pre>
<h3 style="color:SlateGray;">Business news headlines</h3>
<pre>
"""+bnews+"""</pre>
<h3 style="color:SlateGray;">Sports news headlines</h3>
<pre>
"""+snews+"""</pre>
</body>
</html>
""", subtype='html')




with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_HOST, EMAIL_PASSWORD)
    smtp.send_message(msg)

