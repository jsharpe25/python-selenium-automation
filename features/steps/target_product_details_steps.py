from selenium.webdriver.common.by import By
from behave import given, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


COLOR_OPTIONS = (By.CSS_SELECTOR, "li[class*='CarouselItem'] img")
SELECTED_JEANS_COLOR = (By.CSS_SELECTOR, "[data-test='@web/VariationComponent'] div")
SELECTED_SHIRT_COLOR = (By.CSS_SELECTOR, 'div[class*="styles_ndsVariationSelector"] div[class*="styles_headerWrapper"]')


@given('Open target product A-91269718 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/wranglers-men-39-s-relaxed-fit-straight-jeans/-/A-91269718?preselect=90919011#lnk=sametab')
    context.driver.wait.until(
        EC.element_to_be_clickable(COLOR_OPTIONS),
        message='Color options not clickable'
    )


@given('Open target product A-89562092 page')
def open_target(context):
    context.driver.get(f'https://www.target.com/p/x-ray-men-s-basic-henley-neck-short-sleeve-t-shirt/-/A-89562092?preselect=1003759939#lnk=sametab')
    sleep(10)


#Example of a loop
@then('Verify user can click through jeans colors')
def click_and_verify_colors(context):
    expected_colors = ['Navy Denim', 'Dark Wash', 'Light Wash']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for color in colors:
        color.click()
        # for visibility only:
        sleep(0.5)

        selected_color = context.driver.find_element(*SELECTED_JEANS_COLOR).text  # 'Color\nBlack'
        print('Current color', selected_color)

        selected_color = selected_color.split('\n')[1]  # .split removes 'Color\n' part so colors match
        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'


@then('Verify user can click through shirt colors')
def click_and_verify_colors(context):
    expected_colors = ['cranberry', 'dusty mint', 'iron']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)
    print(colors)

    for color in colors[5:8]:
        color.click()
        sleep(0.5)

        selected_banners = context.driver.find_elements(*SELECTED_SHIRT_COLOR) #selects 2 locators (no unique locator)
        selected_banner = selected_banners[1].text # selects the second locator
        selected_color = selected_banner.split('-')[1] # selects only the color name

        print('Current color', selected_color)

        actual_colors.append(selected_color)
        print(actual_colors)

    assert expected_colors == actual_colors, f'Expected {expected_colors} did not match actual {actual_colors}'
