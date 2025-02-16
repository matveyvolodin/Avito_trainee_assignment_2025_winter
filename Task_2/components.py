from playwright.sync_api import Page, expect
from data import base_url, announcement_url

# Все компоненты хранятся в одном файле components.py в целях упрощения структуры проекта.

class Announcement:
    def __init__(self, page: Page):
        self.page = page

    def visit_announcement_page(self):
        self.page.goto(announcement_url)

    def fill_title(self, title):
        self.page.locator('//input[@name="name"]').fill(title)

    def fill_price(self, price):
        self.page.locator('//input[@name="price"]').fill(price)

    def fill_desc(self, desc):
        self.page.locator('//input[@name="description"]').fill(desc)

    def fill_img_url(self, img_url):
        self.page.locator('//input[@name="imageUrl"]').fill(img_url)

    def click_save_button(self):
        self.page.get_by_text("Сохранить").click()

    def fill_desc_edit_page(self, desc):
        self.page.locator('//textarea[@name="description"]').fill(desc)

    def verify_error_messages_is_displayed(self):
        error_messages = self.page.locator('//div[text()="Поле обязательно для заполнения."]')
        assert error_messages.count() == 4, f"Ожидалось 4 сообщения об ошибке, найдено: {error_messages.count()}"

    def click_edit_announcement_button(self):
        self.page.locator(".css-nb383z svg").click()

    def click_save_edited_announcement_button(self):
        self.page.locator(".css-nb383z svg").click()

    def check_announcement_fields_after_edit(self):
        img = self.page.locator('//img[@alt="product image"]')
        name = self.page.locator('//h2')
        price = self.page.locator('//p[@class="chakra-text css-r1bsln"]')
        desc = self.page.locator('//p[@class="chakra-text css-i3jkqk"]')

        expect(img).to_have_attribute("src", "https://thesarai.ru/media/thumbnails/goods/0-1_KR5tNmI.jpg.500x500"
                                                 "_q100_crop-%2C.jpg")
        expect(name).to_have_text("Пень б/у")
        expect(price).to_have_text("200 ₽")
        expect(desc).to_have_text("Бывший в употреблении")


class Listings:
    def __init__(self, page: Page):
        self.page = page

    def visit_main_page(self):
        self.page.goto(base_url)

    def fill_search_field(self, request):
        self.page.get_by_placeholder("Поиск по объявлениям").fill(request)

    def click_search_button(self):
        self.page.get_by_role("button", name="Найти").click()

    def click_create_announcement_button(self):
        self.page.get_by_role("button", name="Создать").click()

    def verify_announcement_presence_in_listings(self):
        announcement = self.page.locator('(//h4[text()="Пень новый"])[1]')
        expect(announcement).to_be_visible()

    def verify_announcement_is_created(self, listings):
        listings.fill_search_field("Пень")
        listings.click_search_button()
        listings.verify_announcement_presence_in_listings()
