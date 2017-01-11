
Automated provisioning
======================


- Ansible vs salt vs bash
  Look, bash is just *fine*
  We could use fabric for everything if we wanted.
  Now fabric supports parallel execution, there is limited need for other solutions
  I will use salt for basic infrastructure buildouts, its integreation with AWS etc.
  and then use fabirc once we have managed the state of PKI / servers up and pinabgle.
  This may be too complex but it is at least clear.

  Use fabric to build basic modules that ansible runs
  http://bsdploy.readthedocs.org/en/latest/usage/ansible-with-fabric.html

  in a venv...
  ::

     pip install ansible

  /etc/ansible/hosts::

     # /etc/ansible/hosts
     localhost ansible_connection=local


- pyholodeck
- holoconfig

