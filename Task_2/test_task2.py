import pytest

# TC_01 > Создание объявления пользователем
def test_create_announcement_positive(listings, announcement):
    listings.visit_main_page()
    listings.click_create_announcement_button()
    announcement.fill_title("Пень новый")
    announcement.fill_desc("Новый, в упаковке")
    announcement.fill_price("300")
    announcement.fill_img_url("https://thesarai.ru/media/goods/2_plAtGpG.jpg")
    announcement.click_save_button()
    listings.verify_announcement_is_created(listings)


# TC_02 > Попытка создания объявления пользователем с незаполненными обязательными полями (negative)
def test_create_announcement_using_empty_fields(listings, announcement):
    listings.visit_main_page()
    listings.click_create_announcement_button()
    announcement.click_save_button()
    announcement.verify_error_messages_is_displayed()

# TC_03 Поиск объявления пользователем
def test_find_announcement(announcement,listings):
    listings.visit_main_page()
    listings.fill_search_field("Пень")
    listings.click_search_button()
    listings.verify_announcement_is_created(listings)

# TC_04 Редактирование объявление пользователем
def test_edit_announcement(announcement,listings):
    announcement.visit_announcement_page()
    announcement.click_edit_announcement_button()
    announcement.fill_img_url(
        "https://thesarai.ru/media/thumbnails/goods/0-1_KR5tNmI.jpg.500x500_q100_crop-%2C.jpg")
    announcement.fill_title("Пень б/у")
    announcement.fill_desc_edit_page("Бывший в употреблении")
    announcement.fill_price("200")
    announcement.click_save_edited_announcement_button()
    announcement.check_announcement_fields_after_edit()

@pytest.mark.xfail(reason= "Поля не являются обязательными при редактировании объявления и сохраняются пустыми")
# TC_05 Попытка редактирования объявления - очистка обязательных полей (negative)
def test_edit_announcement_empty_fields(announcement,listings):
    announcement.visit_announcement_page()
    announcement.click_edit_announcement_button()
    announcement.fill_img_url("")
    announcement.fill_title("")
    announcement.fill_desc_edit_page("")
    announcement.fill_price("")
    announcement.click_save_edited_announcement_button()
    announcement.verify_error_messages_is_displayed()

