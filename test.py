Ну, удачи.
/////////
from selenium import webdriver
chrome = webdriver.Chrome()

chrome.get("https://www.ultimateqa.com/complicated-page/")
chrome.find_elements_by_link_text("Button")[7].click()

chrome.find_element_by_xpath('//div[@class="et_pb_column et_pb_column_1_2 et_pb_column_7    et_pb_css_mix_blend_mode_passthrough"]//a[@title="Follow on Twitter"]').click()

chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_id("s").send_keys("Oscar")
chrome.find_element_by_id("searchsubmit").click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_name("email").send_keys("123@123.123")
chrome.find_element_by_name("jetpack_subscriptions_widget").click()
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_name("et_pb_contact_name_0").send_keys("OsCar")
chrome.find_element_by_name("et_pb_contact_email_0").send_keys("123@123.123")
chrome.find_element_by_name("et_pb_contact_message_0").send_keys("Hello Yugen")
chrome.get("https://www.ultimateqa.com/complicated-page/")

chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="log"]').send_keys("OsC")
chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//input[@name="pwd"]').send_keys("PASS")
chrome.find_element_by_xpath('//div[@class="et_pb_newsletter_form et_pb_login_form"]//button[@class="et_pb_newsletter_button et_pb_button"]').click()
chrome.get("https://www.ultimateqa.com/complicated-page/")