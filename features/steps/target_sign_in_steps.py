from behave import when, then


@when('Open Target sign in form')
def step_open_sign_in_form(context):
    context.app.sign_in_page.open_sign_in_form()


@then('Verify sign in form opened')
def step_verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form()
