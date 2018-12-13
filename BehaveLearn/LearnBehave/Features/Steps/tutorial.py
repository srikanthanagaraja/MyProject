'''
Created on 20-Nov-2018

@author: 105011
'''

from behave import *


    
@given(u'we have behave installed')
def step_impl(context):
    print('This is given statement')


@when(u'we implement scenario outline')
def step_impl(context):
        print("This is when statement in Scenario outline")

def before_step(context, step):
    print('before step')

@then(u'{a} and {b} should be printed')
def step_impl(context,a,b):
    print("This is then statement ",a,b)

def after_step(context,step):
    print("This is after test")
 


#@then(u'6 and 8 should be printed')
#def step_impl(context):
#    raise NotImplementedError(u'STEP: Then 6 and 8 should be printed')

@when(u'we implement a test')
def step_impl(context):
    print("This is when statement")
    


@then(u'behave will test it for us')
def step_impl(context):
    print("This is then statement")