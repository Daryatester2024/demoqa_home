from pages.swag_labs import SwagLabs

def test_check_icon (browser):

    swag_lab_page=SwagLabs(browser)
    swag_lab_page.visit()
    assert swag_lab_page.exist_icon()
    assert swag_lab_page.exist_user()
    assert swag_lab_page.exist_password()
