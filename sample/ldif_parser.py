from data.data import ldif_file, residents


class LdifParser:
    def __init__(self):
        self.ldif_file_name = ldif_file
        self.mail_lists = residents

    def write_ldif(self):
        f = open(self.ldif_file_name, 'w')

        for mail_list in self.mail_lists:
            f.write(self.__print_ldif_header(mail_list))

            for email in residents[mail_list]:
                f.write('mail: ' + email + '\n')

            f.write('\n')

        f.close()

    @staticmethod
    def __print_ldif_header(mail_list):
        header = (
            'dn: cn={mail_list},ou=saatio,ou=lists,dc=satakuntatalo,dc=fi\n'
            'objectClass: top\n'
            'objectClass: extensibleObject\n'
            'objectClass: organizationalRole\n'
            'cn: {mail_list}\n'
        ).format(mail_list=mail_list)

        return header
