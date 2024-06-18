from utils.logging_config import logging
from configparser import ConfigParser
from utils.helper import *


# class Hooks():
#   config = ConfigParser()
#   config.read('C:\\Users\\SPURGE\\PycharmProjects\\sample-selenium-python-cucumber-framework\\config.properties')


def before_all(context):
  context.logger = logging.getLogger('behave')
  context.logger.info('Starting test suite')
  context.driver = None


def before_scenario(context,scenario):
  context.logger.info(f'Starting scenario: {scenario.name}')
  context.driver=create_driver("chrome")

def after_scenario(context, scenario):
  if scenario.status == 'failed':
    context.logger.error(f'Scenario failed: {scenario.name}')
  else:
    context.logger.info(f'Scenario finished: {scenario.name}')

  if context.driver:
    context.driver.quit()
    context.driver = None


  # def before_all(context):
  #   context.logger = logging.getLogger('behave')
  #   context.logger.info('Starting test suite')

  def after_all(context):
    context.logger.info('Test suite finished')

  # def before_scenario(context, scenario):
  #   context.logger.info(f'Starting scenario: {scenario.name}')

  # def after_scenario(context, scenario):
  #   if scenario.status == 'failed':
  #     context.logger.error(f'Scenario failed: {scenario.name}')
  #   else:
  #     context.logger.info(f'Scenario finished: {scenario.name}')

  def before_step(context, step):
    context.logger.debug(f'Starting step: {step.name}')

  def after_step(context, step):
    if step.status == 'failed':
      context.logger.error(f'Step failed: {step.name}')
    else:
      context.logger.debug(f'Step finished: {step.name}')

