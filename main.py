from selenium import webdriver
from selenium.webdriver import Keys
# Библиотека, которая позволяет вводить данные на сайт с клавиатуры
from selenium.webdriver.common.by import By
#Библиотека с поиском элементов на сайте
import time

import random


#Если мы работаем с Chrome
browser = webdriver.Chrome()

browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")

#paragraphs = browser.find_elements(By.TAG_NAME, "p")
# #Для перебора пишем цикл
# for paragraph in paragraphs:
#     print(paragraph.text)
#     input()

hatnotes = []
for element in browser.find_elements(By.TAG_NAME, "div"):
    # Чтобы искать атрибут класса
    cl = element.get_attribute("class")
    if cl == "hatnote navigation-not-searchable ts-main":
        hatnotes.append(element)

print(hatnotes)
hatnote = random.choice(hatnotes)

#Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
link = hatnote.find_element(By.TAG_NAME, "a").get_attribute("href")
browser.get(link)

# browser.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")
# #Проверяем по заголовку, тот ли сайт открылся

# assert "Википедия" in browser.title
# time.sleep(2)
# #Находим окно поиска
# search_box = browser.find_element(By.ID, "searchInput")
# #Прописываем ввод текста в поисковую строку. В кавычках тот текст, который нужно ввести
# search_box.send_keys("Солнечная система")
# #Добавляем не только введение текста, но и его отправку
# search_box.send_keys(Keys.RETURN)
# time.sleep(2)
#
#
# a = browser.find_element(By.LINK_TEXT, "Солнечная система")
# #Добавляем клик на элемент
# a.click()
# browser.get("https://ru.wikipedia.org/wiki/%D0%A1%D0%BE%D0%BB%D0%BD%D0%B5%D1%87%D0%BD%D0%B0%D1%8F_%D1%81%D0%B8%D1%81%D1%82%D0%B5%D0%BC%D0%B0")







# hatnotes = []
# for element in browser.find_elements(By.TAG_NAME, "div")
# #Чтобы искать атрибут класса
# cl = element.get.attribute("class")
# if cl == "hatnote navigation-not-searchable":
# hatnotes.append(element)
#
# print(hatnotes)
# hatnote = random.choice(hatnotes)
#
# #Для получения ссылки мы должны найти на сайте тег "a" внутри тега "div"
# link = hatnote.find_element(By.TAG_NAME, "a").get.attribute("href")
# browser.get(link)




# browser.get("https://en.wikipedia.org/wiki/Document_Object_Model")
# browser.save_screenshot("dom.png")
# time.sleep(5)
# browser.get("https://ru.wikipedia.org/wiki/Selenium")
# browser.save_screenshot("selenium.png")
# time.sleep(3)
# browser.refresh()


# browser.quit()
