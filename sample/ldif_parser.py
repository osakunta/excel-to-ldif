from sample.validator import *


def print_ldif_header(f, mail_list):
    f.write('dn: cn=' + mail_list + ',ou=saatio,ou=lists,dc=satakuntatalo,dc=fi\n')
    f.write('objectClass: top\n')
    f.write('objectClass: extensibleObject\n')
    f.write('objectClass: organizationalRole\n')
    f.write('cn: ' + mail_list + '\n')


def write_ldif(residents):
    f = open(ldif_file, 'w')

    for mail_list in residents:
        print_ldif_header(f, mail_list)

        for email in residents[mail_list]:
            f.write('mail: ' + email + '\n')

        f.write('\n')

    f.close()
