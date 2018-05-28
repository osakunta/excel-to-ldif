#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Contains all the excel and mail list data
from data.data import list1, list2, divider, renters, again_renters, residents
from sample.cleaner import clean
from sample.validator import valid_email
import json


class MailListGenerator:

    def parse_all(self):
        self.__parse_emails(renters, 9)
        self.__parse_emails(again_renters, 3)
        #print(json.dumps(residents, indent=4, sort_keys=True))

    @staticmethod
    def __parse_emails(excel_sheet, mail_col):
        MailListGenerator.__set_list_to(list1)

        for row in range(1, excel_sheet.nrows):
            apartment = clean(excel_sheet.cell(row, 0).value).replace(' ', '_')
            emails = clean(excel_sheet.cell(row, mail_col).value).replace(' ', '')

            MailListGenerator.__set_value(emails)
            MailListGenerator.__change_list_if_right(apartment)

    @staticmethod
    def __set_list_to(list):
        global mail_list
        mail_list = list

    @staticmethod
    def __set_value(values):
        if values:
            global residents

            emails = values.split('/')

            for email in emails:
                if not valid_email(email):
                    emails.remove(email)

            residents[mail_list].extend(emails)

    @staticmethod
    def __change_list_if_right(apartment):
        if apartment == divider:
            global mail_list
            mail_list = list2
