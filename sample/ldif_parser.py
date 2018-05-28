
class LdifParser:
    def __init__(self, ldif_file_name, mail_lists):
        self.ldif_file_name = ldif_file_name
        self.mail_lists = mail_lists

    def write_ldif(self):
        f = open(self.ldif_file_name, 'w')

        for mail_list in self.mail_lists:
            f.write(self.__print_ldif_header(mail_list['name']))

            for email in mail_list['emails']:
                f.write('mail: ' + email + '\n')

            f.write('\n')

        f.close()

    @staticmethod
    def __print_ldif_header(mail_list_name):
        header = (
            'dn: cn={mail_list_name},ou=saatio,ou=lists,dc=satakuntatalo,dc=fi\n'
            'objectClass: top\n'
            'objectClass: extensibleObject\n'
            'objectClass: organizationalRole\n'
            'cn: {mail_list_name}\n'
        ).format(mail_list_name=mail_list_name)

        return header
