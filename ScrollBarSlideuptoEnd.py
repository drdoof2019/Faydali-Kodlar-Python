#Sınırsız scrolling için(en aşağı iner)
#for unlimited number of scrolling
lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

#5 kere scrolling için
#for 5 times scrolling
scrollCounter = 0

while scrollCounter <= 5:
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    scrollCounter += 1
    time.sleep(2)


#fayladanılabilecek websitesi
    https://stackoverflow.com/questions/26566799/wait-until-page-is-loaded-with-selenium-webdriver-for-python
