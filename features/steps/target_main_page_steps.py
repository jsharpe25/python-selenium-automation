from behave import given


@given('Open Target main page')
def steps_open_main_page(context):
    context.app.main_page.open_main_page()
