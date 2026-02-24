from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from support.logger import logger
from selenium.webdriver.chrome.options import Options

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

    ### BROWSERSTACK ###
    # Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
    # bs_user = ''  # Add your user key
    # bs_key = ''  # Add your pass key
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # options = Options()
    # bstack_options = {
    #     'os': 'Windows',  # 'OS X' for macOS, 'Windows' for Windows OS
    #     'osVersion': '11',  # Specify the version you want to use
    #     'browserVersion': 'latest', # 'latest' uses newest stable version
    #     'browserName': 'Chrome',
    #     'sessionName': scenario_name # Automatically pulls name from Behave scenario
    # }
    # options.set_capability('bstack:options', bstack_options)
    # context.driver = webdriver.Remote(command_executor=url, options=options)

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
