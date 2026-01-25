from behave import when, then


@when('Click on Add to cart button')
def step_add_to_cart_button(context):
    context.app.search_results_page.add_to_cart_button()


@when('Store product name')
def step_store_product_name(context):
    context.product_name = context.app.search_results_page.store_product_name()
    print(f'Stored product name: {context.product_name}')


@when('Confirm Add to cart button')
def step_confirm_cart_button(context):
    context.app.search_results_page.confirm_cart_button()


@when('Click on View cart button')
def step_view_cart_button(context):
    context.app.search_results_page.view_cart_button()


@then('Search results for {product} are shown')
def steps_verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
