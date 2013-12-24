===============================
Underwear
===============================

.. image:: https://badge.fury.io/py/underwear.png
    :target: http://badge.fury.io/py/underwear
    
.. image:: https://travis-ci.org/makaimc/underwear.png?branch=master
        :target: https://travis-ci.org/makaimc/underwear

.. image:: https://pypip.in/d/underwear/badge.png
        :target: https://crate.io/packages/underwear?version=latest


Automated deployments for Python-powered web applications

* Free software: MIT license
* Documentation: http://underwear.rtfd.org.

Features
--------

* Automagical deployments to a web & database server
* Configurable via a simple YAML template


Why Create Underwear?
---------------------
I build a lot of Django projects and I needed an easy way to deploy them to
a traditional virtual private server stack instead of just defaulting to
Heroku. I previously wrote extensive Fabric scripts to automate the
server configuration and deployment process, but those scripts were very 
difficult to maintain.


First steps
-----------
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

