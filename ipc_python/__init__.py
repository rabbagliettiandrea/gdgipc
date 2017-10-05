import logging

import sys
from pyfiglet import figlet_format
from termcolor import cprint

logging.basicConfig(
    format='[%(asctime)s %(levelname)s] %(message)s', level=logging.INFO, datefmt='%H:%M:%S',
    stream=sys.stdout
)
logger = logging.getLogger(__name__)


def p_hero(s):
    cprint(figlet_format(s), 'magenta')

def p_title(s):
    cprint(figlet_format(s, font='straight'), 'yellow')


from . import rabbitmq

p_hero('Hello GDG !')
