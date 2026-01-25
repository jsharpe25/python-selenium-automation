from behave import then

@then('Verify Terms page opened')
def step_verify_terms_page(context):
    context.app.terms_page.verify_terms_page()
