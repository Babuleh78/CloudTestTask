from playwright.sync_api import sync_playwright

def test_playwright():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=False)  
        page = browser.new_page()

        try:
            page.goto("https://example.com") # Открываем страницу

            assert "Example" in page.title(), "Заголовок не содержит 'Example'" # Проверяем, что заголовок содержит Example

            page.click("text=More information") # Находим элемент с текстом "More information" и нажимаем

            page.wait_for_url("https://www.iana.org/help/example-domains") # Проверяем, что URL изменился на нужный
            print("Все проверки прошли успешно!")

        except Exception as e:
            print(f"Возникла ошибка: {e}")
        finally:
            browser.close()

test_playwright()
