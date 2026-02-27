import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.remote.client_config import ClientConfig
from selenium.webdriver.remote.remote_connection import RemoteConnection
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger


### RUN ALLURE REPORT ###
# Install allure behave (first time only), use command line: pip install allure-behave
# All tests, use command line: behave -f allure_behave.formatter:AllureFormatter -o test_results/features/tests
# Tagged tests, use command line: behave -f allure_behave.formatter:AllureFormatter -o test_results/ --tags=smoke

def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """
    ### CHROME ###
    context.driver = webdriver.Chrome()

    ### FIREFOX AND SAFARI ###
    # context.driver = webdriver.Firefox()
    # context.driver = webdriver.Safari()

    ### BROWSERSTACK WEB ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''  # Add your user key
    # bs_key = ''  # Add your pass key
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = { # Define your options
    #     'os': 'OS X',  # 'OS X' for macOS, 'Windows' for Windows OS
    #     'osVersion': 'Tahoe',  # Specify the version you want to use
    #     'browserName': 'Safari', # Specify the browser you want to use
    #     'browserVersion': 'latest', # 'latest' uses newest stable version
    #     'sessionName': scenario_name # Automatically pulls name from Behave scenario
    # }
    # options.set_capability('bstack:options', bstack_options)
    # prefs = {"profile.default_content_setting_values.notifications": 2} # Removes notifications
    # options.add_experimental_option("prefs", prefs)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

    ### BROWSERSTACK MOBILE ###
    # bs_user = os.getenv("BROWSERSTACK_USERNAME")
    # bs_key = os.getenv("BROWSERSTACK_ACCESS_KEY")
    # if not bs_user or not bs_key:
    #     raise Exception("BrowserStack credentials not set in .env file.")
    # client_config = ClientConfig(remote_server_addr="https://hub-cloud.browserstack.com/wd/hub", username=bs_user, password=bs_key)
    # remote_connection = RemoteConnection(client_config=client_config)
    # bstack_options = {
    #     'osVersion': '16.0',
    #     'deviceName' : 'Samsung Galaxy S24',
    #     'browserName': 'Chrome',
    #     'projectName': 'Project Title',
    #     'buildName': 'software_build',
    #     'sessionName': scenario_name,
    # }
    # options = Options()
    # options.add_argument('--disable-notifications')
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=remote_connection, options=options)
    # context.is_mobile = True

    ### MOBILE EMULATION ###
    # mobile_emulation = {"deviceName": "iPhone XR"}
    # options = Options()
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(options=options)

    ### HEADLESS MODE ####
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # context.driver = webdriver.Chrome(options=options)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    logger.info(f'\nStarted scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    logger.info(f'Started step: {step}')
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    if hasattr(context, "driver"):
        context.driver.quit()
