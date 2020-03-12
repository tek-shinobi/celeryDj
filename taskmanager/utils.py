'''Demo script to implement a task that takes time and fails randomly'''
import logging
import os
import sys
import time

def make_log_entry(count):
    logging.info(f'Log entry #{count}')

def time_taking_task():
    i: int = 0
    while i < 100:
        make_log_entry(i)
