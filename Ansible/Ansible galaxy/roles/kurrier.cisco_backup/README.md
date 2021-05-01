Ansible Role: cisco_backup [![Build Status](https://travis-ci.org/kurrier/ansible-role_cisco_backup.svg?branch=master)](https://travis-ci.org/kurrier/ansible-role_cisco_backup)
=========

Cisco Backup Control for ASA and IOS

Requirements
------------

Git / Cisco Products

Role Variables
--------------

vars/main.yml - Contains default variables
* cisco_backup_repo_dest: destination of repo cloning
* cisco_backup_dest: destination to backup cisco inside of cloned repo
* cisco_backup_file: name of config backup

vars/asa.yml - Contains ASA connection settings
* asa_connection: host/username/passowrd/auth_pass setting

vars/ios.yml - Contains IOS connection settings
* ios_connection: host/username/passowrd/auth_pass setting

## Backup Setup ##
* cisco_backup: [true/false] - enable/disable cisco backup
* cisco_function_encrypt: [true/false] enable/disable use of Vault for auth
* cisco_auth_user: user for auth (use vault var if encryption is enabled)
* cisco_auth_pass: pass for auth (use vault var if encryption is enabled)
* cisco_backup_repo: cisco backups repo
* cisco_backup_repo_url: url of cisco backups repo

## Base Setup ##
can be set as global vars
* function: router/switches/firewall - host devices type
* sub_function: inside/outside - location of devices

## Message Setup: ##
* cisco_function_msg: [true/false] - enable/disable cisco alerts

Dependencies
------------

kurrier.alerts - if want to use alerts

Example Playbook
----------------

Example:

    - hosts: switch1
      connection: local
      gather_facts: no
      vars:
        cisco_function_encrypt: true
        cisco_auth_user: "{{ vault_cisco_auth_user }}"
        cisco_auth_pass: "{{ vault_cisco_auth_pass }}"

        cisco_backup: true
        cisco_backup_repo: https://github.com/repo.git
        cisco_backup_repo_url: https://github.com

      roles:
         - kurrier.cisco_backup

Test
----------------

ansible-playbook tests/test.yml -i tests/inventory

Plans
----------------
- Add restore to Cisco Device from Git

License
-------

GPLv3

Author Information
------------------

Nick Lalumiere
