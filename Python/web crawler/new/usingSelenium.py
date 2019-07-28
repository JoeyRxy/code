from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(
    executable_path='C:/Users/29388/Documents/code/Python/web crawler/chromedriver.exe')
browser.get("https://www.baidu.com/")
time.sleep(5)

try:
    elem = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "dp"))
    )
except Exception as e:
    print(e)
finally:
    browser.quit()

# 判断传入的标题
# title_is
# title_contains

# 判断元素是否加载成功
# presence_of_element_located
# presence_of_all_elements_located

# 判断元素是否可见
# visibility_of_element_located
# visibility_of

# 判断frame是否可以切入
# frame_to_be_available_and_switch_to_it

# 判断元素是否被选中
# element_to_be_selected
# element_located_to_be_selected
# element_selection_state_to_be
# element_located_selectoin_state_to_be

# 判断是否有弹窗
# alert_is_present

# 判断是不是在DOM中
# staleness_of
