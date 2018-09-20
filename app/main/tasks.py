# -*- coding: utf-8 -*-
"""
This module implements the tasks to run.
"""
# import random
import time
# from flask import current_app
# from .. import r

def run(task):
    if 'error' in task:
        time.sleep(1)
        1 / 0
    if task.startswith('Short'):
        result = wait_a_bit(1, task)
    elif task.startswith('Long'):
        result = wait_a_bit(9, task)
    elif task.startswith('The good one'):
        result = new_custom_task()
    else:
        result = "unrecognized task request"
        # seconds = 9 #random.randint(2, current_app.config['MAX_TIME_TO_WAIT'])
    # time.sleep(seconds)
#    r.hset('task:%s'%job_id, 'status', job.get_status())
    # return '{} done in {}s'.format(task, seconds)
    return result

def new_custom_task():
    time.sleep(2)
    return 'new task happened!'

def wait_a_bit(seconds, task):
    time.sleep(seconds)
    return '{} done in {}s'.format(task, seconds)
