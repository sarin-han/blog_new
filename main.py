from selenium import webdriver
import time
import pickle
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

def naver_test():
    # 1. 크롬 > 네이버 열기
    driver = webdriver.Chrome()
    driver.get("https://naver.com")
    time.sleep(2)

    # 2. 쿠키로 네이버 로그인
    with open("naver_cookies.pkl","rb") as f:
        cookies = pickle.load(f)
        for cookie in cookies:
            driver.add_cookie(cookie)
        driver.refresh()
    time.sleep(2)

    # 3. 블로그 글쓰기 창으로 이동
    driver.get("https://blog.naver.com/GoBlogWrite.naver")
    time.sleep(3)

    # 4. mainFrame 진입
    driver.switch_to.frame("mainFrame")
    print("mainFrame 그냥 selenium 으로 할게.. 블로그 글쓰기에서 사진 클릭하면 이렇게 나오네진입 성공")
    time.sleep(1)

    # 5. 본문 입력
    action = ActionChains(driver)
    action.send_keys("text test").perform()
    print("본문 입력 성공")
    time.sleep(1)

    # 6. 제목 입력
    title = driver.find_element(By.XPATH,"//span[contains(text(),'제목')]")
    time.sleep(1)
    title.click()
    print("제목 클릭 완료")
    time.sleep(1)
    action.send_keys("title test").perform()
    print("제목 입력 완료")
    time.sleep(1)

    # 7. 도움말 창 닫기
    close_button = driver.find_element(By.XPATH,"//article[@class='se-help-panel se-is-on']//div[@class='se-help-container']//header//button[@class='se-help-panel-close-button']")
    print("닫기 버튼 찾음")
    time.sleep(1)

    close_button.click()
    print("닫기 버튼 클릭 성공")
    time.sleep(3)

    # 8. 블로그 글 발행하기
    post_button = driver.find_element(By.XPATH,"//div[@class='header__Ceaap']//div[@class='header_menu__UJgdY']//div[@class='publish_btn_area__KjA2i']//button[@class='publish_btn__m9KHH']")
    print("발행 버튼 찾음")
    time.sleep(1)

    post_button.click()
    print("발행 버튼 클릭 성공")
    time.sleep(2)

    post2_button = driver.find_element(By.XPATH,"//div[@class='layer_btn_area__UzyKH']//div[@class='btn_area__fO7mp']//button[@class='confirm_btn__WEaBq']")
    print("발행 버튼 2 찾기 성공")
    post2_button.click()
    print("발행 버튼2 클릭 성공")
    time.sleep(3)

    driver.quit()

    


if __name__ == "__main__":
    naver_test()


