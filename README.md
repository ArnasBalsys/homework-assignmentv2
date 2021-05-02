# homework-assignmentv2

Ansible role to install and configure RabbitMQ


Example Playbook
--------------

To run this role you can use a sample playbook that is designed to run on localhost
     
    ansible-playbook --ask-vault-pass playbook.yml 

      
Role Variables
--------------
Available variables described in defaults/main.yml


RabbitMQ repository & GPG signing key url:

    rabbitmq_deb_repo_url: https://dl.bintray.com/rabbitmq/debian
    rabbitmq_deb_gpg_url: https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc

