import time
from pages.RegPage import RegPage
from behave import *


@given(u'user navigates to Registartion url')
def step_impl(context):
    context.logger.info('Navigating to the registration page')
    context.regPage=RegPage(context.driver)
    context.regPage.navigate_REGPAGE_url()

@when(u'user enters Firstname,Middlename and lastname')
def step_impl(context):
    context.logger.info('Entering firstname,middlename and lastname')
    context.regPage.fill_firstname_middlename_and_lastname("Yashmanth", "Kumar", "Gouda")


@when(u'user clicks on Coarse and Gender')
def step_impl(context):
    context.regPage.select_gender()
    time.sleep(3)

@when(u'user enters MobileNumber,Address,Email,Password and ReType password')
def step_impl(context):
    context.logger.info('Entering necessary details')
    context.regPage.enter_all_inputFields("9876543210", "Orissa", "yash1@gmail.com", "Yash123@", "Yash123@")
    time.sleep(3)

@then(u'user clicks on submit Button')
def step_impl(context):
    context.logger.info('Clicking on Submit Button')
    context.regPage.click_Submit()
