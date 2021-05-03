# homework-assignmentv2

Ansible role to install and configure RabbitMQ for Debian OS


Example Playbook
--------------

To run launch role you can use a sample playbook that is designed to run on localhost

    ansible-playbook --ask-vault-pass playbook.yml

This role also performs an installation for yamllint. The files can be verified using

     yamllint path_to_file


Role Variables
--------------
Available variables described in defaults/main.yml


RabbitMQ & Erlang repository, GPG signing key url locations:

     rabbitmq_deb_url: https://packagecloud.io/rabbitmq/rabbitmq-server/packages/
     rabbitmq_deb_gpg_url: https://github.com/rabbitmq/signing-keys/releases/download/2.0/rabbitmq-release-signing-key.asc

     erlang_repo_url: http://packages.erlang-solutions.com/debian/
     erlang_deb_gpg_url: http://packages.erlang-solutions.com/debian/erlang_solutions.asc

Requirements
--------------

     ansible-galaxy install -r collections/requirements.yml
