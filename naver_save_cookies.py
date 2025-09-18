# ✅ 1단계: 처음 한 번 수동 로그인하고 쿠키 저장 (naver_save_cookies.py)

from selenium import webdriver
import time
import pickle

# 브라우저 열기
driver = webdriver.Chrome()
driver.get("https://nid.naver.com/nidlogin.login")

print("🔐 수동 로그인 후 로봇인증까지 마친 뒤, 엔터를 누르세요.")
input()

# 쿠키 저장
with open("naver_cookies.pkl", "wb") as f:
    pickle.dump(driver.get_cookies(), f)

print("✅ 쿠키 저장 완료!")
driver.quit()