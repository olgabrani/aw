# -*- coding: utf-8 -*-
from django import template
from datetime import date

register = template.Library()

@register.filter(name='calculate_age')
def calculate_age(born):
    today = date.today()
    try: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=today.year)
    except ValueError:
        birthday = born.replace(year=today.year, day=born.day-1)
    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year

@register.filter
def force_two_digit_num(num):
    if num < 10:
	return '0'+str(num)
    else:
	return num

@register.filter
def translate_stick(s):
    if s == 'RT':
	return 'Δεξί'
    else:
	return 'Αριστερό'


