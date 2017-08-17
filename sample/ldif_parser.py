from data.data import ldif_file
from sample.validator import *

def print_ldif_header(f, mail_list):
    f.write('dn: cn=' + mail_list + ',ou=saatio,ou=lists,dc=satakuntatalo,dc=fi\n')
    f.write('objectClass: top\n')
    f.write('objectClass: extensibleObject\n')
    f.write('objectClass: organizationalRole\n')
    f.write('cn: ' + mail_list + '\n')

def print_ldif_entry(f, email):
    if not valid_email(email):
        return

    f.write('mail: ' + email + '\n')

def get_emails(mail, apartment_entry):
    if mail in apartment_entry:
        return apartment_entry[mail].split('/')
    else:
        return []

def apartment_emails(apartment_entry):
    return get_emails('email', apartment_entry) + get_emails('tenant', apartment_entry)

def for_every_email_in(f, apartment_entry):
    entries = apartment_emails(apartment_entry)

    for i, entry in enumerate(entries):
        print_ldif_entry(f, entry.strip())

def create_entries_for_apartment(f, apartment_entry):
    for_every_email_in(f, apartment_entry)

def write_ldif(residents):
    f = open(ldif_file, 'w')

    for mail_list in residents:
        print_ldif_header(f, mail_list)

        for apartment in residents[mail_list]:
            apartment_entry = residents[mail_list][apartment]
            create_entries_for_apartment(f, apartment_entry)

        f.write('\n')

    f.close()
