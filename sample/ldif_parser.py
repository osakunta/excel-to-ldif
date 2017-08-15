from data.data import ldif_file
from sample.validator import *

def print_ldif_entry(f, cn, email, mail_list):
    if not valid_email(email, False):
        return

    f.write('dn: cn=' + cn + ',ou=' + mail_list + ',ou=saatio,ou=lists,dc=satakuntatalo,dc=fi\n')
    f.write('objectClass: top\n')
    f.write('objectClass: extensibleObject\n')
    f.write('objectClass: organizationalRole\n')
    f.write('cn: ' + cn + '\n')
    f.write('mail: ' + email + '\n')
    f.write('\n')

def get_emails(mail, apartment_entry):
    if mail in apartment_entry:
        return apartment_entry[mail].split('/')
    else:
        return []

def apartment_emails(apartment_entry):
    return get_emails('email', apartment_entry) + get_emails('tenant', apartment_entry)

def for_every_email_in(f, apartment, apartment_entry, mail_list):
    entries = apartment_emails(apartment_entry)

    for i, entry in enumerate(entries):
        cn = apartment

        # If there are multiple emails for one apartment, give unique cn
        if i > 0:
            cn += '_' + str(i + 1)

        print_ldif_entry(f, cn, entry.strip(), mail_list)

def create_entries_for_apartment(f, apartment, apartment_entry, mail_list):
    for_every_email_in(f, apartment, apartment_entry, mail_list)

def write_ldif(residents):
    f = open(ldif_file, 'w')

    for mail_list in residents:
        for apartment in residents[mail_list]:
            apartment_entry = residents[mail_list][apartment]
            create_entries_for_apartment(f, apartment, apartment_entry, mail_list)

    f.close()
