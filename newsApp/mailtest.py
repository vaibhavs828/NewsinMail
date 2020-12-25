#NAYI SHURUAT

def main():
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    import datetime, time, os
    import smtplib
    #from email.message import EmailMessage
    from django.core.mail import send_mail
    from django.conf import settings


    #web-driver for chrome

    wait_time = 10 #waits for 10 seconds to get the news//if possible will take less time
    op = webdriver.ChromeOptions()
    op.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    op.add_argument("--headless")
    op.add_argument("--no-sandbox")
    op.add_argument("--disable-dev-sh-usage")
    
    driver = webdriver.Chrome(executable_path = os.environ.get("CHROMEDRIVER_PATH"), chrome_options=op)
    #Connection to google news
    print('Collecting news from Google News...\n')
    google_news = "https://news.google.com/topstories?hl=en-IN&gl=IN&ceid=IN:en"

    driver.get(google_news)
    driver.implicitly_wait(wait_time)
    elements = driver.find_elements_by_tag_name('h3')


    #Saving into string
    news = ''
    ind = 1
    for i in elements:
        news += str(ind) + ')'
        news += i.text + '\n'
        ind += 1


    #print("NOW printing world")
    #driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&   gl=IN&ceid=IN%3Aen')
    #driver.implicitly_wait(wait_time)
    #element2 = driver.find_elements_by_tag_name('h3')


    #Saving into string
    #wnews = ''
    #ind2 = 1
    #for j in element2:
     #   wnews += str(ind2) + ')'
      #  wnews += j.text + '\n'
       # ind2 += 1
        #if ind2 == 7 :
         #   break
        
   # print(wnews)
    #print("\n ")
    #print("NOW printing business")
    #driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx6TVdZU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&   gl=IN&ceid=IN%3Aen')
    #driver.implicitly_wait(wait_time)
    #element3 = driver.find_elements_by_tag_name('h3')

    #Saving into string
   # bnews = ''
    #ind3 = 1
    #for k in element3:
     #   bnews += str(ind3) + ')'
      #  bnews += k.text + '\n'
       # ind3 += 1
        #if ind3 == 7 :
         #   break


   # print("\n ")
    #print("NOW printing sports")
    #driver.get('https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRFp1ZEdvU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&   gl=IN&ceid=IN%3Aen')
    #driver.implicitly_wait(wait_time)
    #element4 = driver.find_elements_by_tag_name('h3')

    #Saving into string
    #snews = ''
    #ind4 = 1
    #for l in element4:
     #   snews += str(ind4) + ')'
      #  snews += l.text + '\n'
       # ind4 += 1
        #if ind4 == 7 :
        #    break



    driver.quit()



    #Django mail and sendgrid

    subject = "Hello! Today's headlines"
    from_email = settings.DEFAULT_FROM_EMAIL
    message = "hahahahahah"

    #msg.add_alternative("""\
    html_message = """\
    <!DOCTYPE html>
    <html>
    <body>
    <h3 style="color:SlateGray;">Today's top news headlines</h3>
    <pre>
    """+news+"""</pre>
    </body>
    </html>
    """#, subtype='html')
    send_mail(subject, message, from_email, ['vaibhavs828@gmail.com'], fail_silently=True,html_message=html_message)
    
    print("mail sent")







if __name__ == "__main__":
    main()
    







