from behave import given, when


@given('Open Target App page')
def step_open_app_page(context):
    context.app.app_page.open_app_page()


@when('Click Privacy Policy link')
def step_click_pp_link(context):
    context.app.app_page.click_pp_link()
