from sample.validator import *

# parse_all()

# f = open(ldif_file, 'w')
# write_ldif(residents)
# f.close()

validate_emails(renters, 9, False)
validate_emails(again_renters, 3, True)
