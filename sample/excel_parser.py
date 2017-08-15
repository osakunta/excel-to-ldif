#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contains all the excel and mail list data
from data.data import *
from sample.cleaner import clean
import json

def set_list_to(list):
    global mail_list
    mail_list = list

def change_list_if_right(apartment):
    if apartment == divider:
        global mail_list
        mail_list = list2

def set_value(apartment, key, value):
    if value:
        global residents
        residents[mail_list][apartment][key] = value

def parse_emails(excel_sheet, mail_col, mail_entry, entry_required):
    set_list_to(list1)

    for row in range(1, excel_sheet.nrows):
        apartment = clean(excel_sheet.cell(row, 0).value).replace(' ', '_')
        email = clean(excel_sheet.cell(row, mail_col).value)

        if not entry_required:
            residents[mail_list][apartment] = {}

        if entry_required and not (apartment in residents[mail_list]):
            raise ValueError(
                'Unknown apartment "' + apartment + '": Again renters, line ' + \
                str(row + 1)
            )

        set_value(apartment, mail_entry, email)

        change_list_if_right(apartment)

def parse_all():
    parse_emails(renters, 9, 'email', False)
    parse_emails(again_renters, 3, 'tenant', True)
    #print(json.dumps(residents, indent=4, sort_keys=True))
