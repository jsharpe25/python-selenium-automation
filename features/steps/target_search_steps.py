from behave import then


@then('Search results for {product} are shown')
def steps_verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)
