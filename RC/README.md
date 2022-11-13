# DEMO SELENIUM REMOTE CONTROL

- Chạy [selenium RC](https://www.selenium.dev/documentation/legacy/selenium_1/) test sử dụng python

## Chuẩn bị
- Phần mềm [Visual studio code](https://code.visualstudio.com/download)
- [Python & Pip](https://www.python.org/downloads/)
- [Selenium RC Server](./selenium-server-standalone-2.53.1.jar)
- [Selenium Server](./selenium-server-4.6.0.jar)
- Thư viện Selenium `pip install selenium`
- `pip install html-testRunner`

## Chạy test
- Mỗi khi chạy, cần chạy Selenium Server (mặc định ở LocalHost:4444): `java -jar selenium-server-4.6.0.jar standalone`
    (hoặc `java -jar selenium-server-4.6.0.jar hub`, `java -jar selenium-server-4.6.0.jar node`)

- Ở một terminal khác, chạy file [main.py](./main.py): `py main.py`

## Lưu ý
- File [test.py](./tests/test.py) chỉ chạy được ở các phiên bản selenium từ 1 và 2. 
    - Để tải thư viện Selenium client library, cần chạy lệnh `pip install selenium==2.53.1`
    - Để chạy Selenium Server tương ứng, chạy lệnh `java -jar selenium-server-standalone-2.53.1.jar`

