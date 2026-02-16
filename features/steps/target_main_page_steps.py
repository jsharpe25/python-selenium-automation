from behave import given


@given('Open Target main page')
def step_open_main_page(context):
    context.app.main_page.open_main_page()
