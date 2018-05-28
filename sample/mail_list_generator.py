#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contains all the excel and mail list data
from data.data import *
from sample.cleaner import clean
from sample.validator import valid_email
import json


def set_list_to(list):
    global mail_list
    mail_list = list


def change_list_if_right(apartment):
    if apartment == divider:
        global mail_list
        mail_list = list2


def set_value(apartment, key, values):
    if values:
        global residents

        emails = values.split('/')

        for email in emails:
            if not valid_email(email):
                emails.remove(email)

        residents[mail_list].extend(emails)


def parse_emails(excel_sheet, mail_col, mail_entry, entry_required):
    set_list_to(list1)

    for row in range(1, excel_sheet.nrows):
        apartment = clean(excel_sheet.cell(row, 0).value).replace(' ', '_')
        emails = clean(excel_sheet.cell(row, mail_col).value).replace(' ', '')

        set_value(apartment, mail_entry, emails)

        change_list_if_right(apartment)


def parse_all():
    parse_emails(renters, 9, 'email', False)
    parse_emails(again_renters, 3, 'tenant', True)
    #print(json.dumps(residents, indent=4, sort_keys=True))