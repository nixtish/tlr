[![Ansible Galaxy](https://img.shields.io/badge/ansible--galaxy-percona__mysql-blue.svg)](https://galaxy.ansible.com/list#/roles/5068) [![Build Status](https://travis-ci.org/systemli/ansible-sshd.svg)](https://travis-ci.org/aydintd/percona_mysql)


# Ansible Role: percona_mysql

An ansible role for Percona MySQL which you can install and manage the server and the database itself. Also clients.
 Which runs on Debian and Ubuntu.  RHEL installations will be imported asap.

### Requirements

python-mysql package should be installed before apply the role. (Actually role itself will do that in the main section, you don't have to install manually)

### Role Variables

Percona MySQL will be installed default 5.6 version.

All mysql server and client variables are in default/main.yml, check it out for more information.

For extra, you can create all your databases and db-users like this in default/main.yml :

        # Databases.
        # Full example:
        mysql_databases:
         - { name: test, 
             collation: utf8_general_ci, 
             encoding: utf8 
           }
        
        # Users
        # Full Example:
        mysql_users:
         - { name: test, 
             host: localhost, 
             password: t3st, 
             priv: "test.*:ALL"
           }
        
### Dependencies

No dependencies at all.

### Example Playbook
        ---
        - hosts: default
          sudo: true
          gather_facts: yes
        
          pre_tasks:  ====(optional)==== 
            - name: Ensure wget git and unzip installed
              apt: pkg={{item}} state=installed update_cache=true
              with_items:
                - wget
                - git
                - vim
                - unzip
        
          roles:
            - aydintd.percona_mysql
        
### License

GPLv2

### Author Information

- Aydin Doyak 
- Linux System Administrator 
- http://aydintd.net

