from behave import given, when, then

@given('Open Help page for Returns')
def step_open_help_returns(context):
    context.app.help_page.open_help_returns()


@when('Select Help topic {option_value}')
def step_select_topic(context, option_value):
    context.app.help_page.select_topic(option_value)


@then('Verify Help {topic} page opened')
def step_verify_help_topic_opened(context, topic):
    context.app.help_page.verify_help_topic_opened(topic)
