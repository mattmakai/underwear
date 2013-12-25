========
Usage
========

To use Underwear in a project::

	import underwear


SSH keys
--------
Ansible runs over SSH, so we need a way to bootstrap SSH connections through
a non-root user.

One way to automate these first few steps is with Fabric. The
fabfile.py.template contains one public function, bootstrap_ansible.
bootstrap_ansible calls the other functions to create a non-root user with
sudo privileges, upload public keys for deployment, and lock down root from
logging in.

Copy fabfile.py.template to fabfile.py, fill in the commented fields at
the top of the script, then run the script with::

  fab bootstrap_ansible

Right now the script will prompt you for the password the non-root user should
be created with. I'll automate that manual step away later.

