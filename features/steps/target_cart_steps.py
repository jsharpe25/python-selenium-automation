from behave import then


@then('Verify empty cart message')
def step_verify_empty_cart_message(context):
    context.app.cart_page.verify_empty_cart_message()


@then('Verify cart has {amount} item(s)')
def step_verify_cart_items (context, amount):
    context.app.cart_page.verify_cart_items(amount)


@then('Verify product in cart is correct')
def step_verify_product(context):
    context.app.cart_page.verify_product(context.product_name)
