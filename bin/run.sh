#!/bin/bash

cd /app/monitoring-scripts/excel-to-ldif/

python3 run.py

cd /app/vagrant/ldap

vagrant ssh -- -t 'sudo su && ldapdelete -r -h 127.0.0.1 -D "cn=admin,dc=satakuntatalo,dc=fi" -w $LDAPPW "ou=talolaiset,ou=saatio,ou=lists,dc=satakuntatalo,dc=fi"'
vagrant ssh -- -t 'sudo su && ldapdelete -r -h 127.0.0.1 -D "cn=admin,dc=satakuntatalo,dc=fi" -w $LDAPPW "ou=osakehuoneistot,ou=saatio,ou=lists,dc=satakuntatalo,dc=fi"'
vagrant ssh -- -t 'sudo su && ldapadd -h 127.0.0.1 -D "cn=admin,dc=satakuntatalo,dc=fi" -w $LDAPPW -f `ls -t /home/vagrant/ldif/*.ldif | head -1`'
