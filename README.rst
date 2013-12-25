===============================
Underwear
===============================

.. image:: https://badge.fury.io/py/underwear.png
    :target: http://badge.fury.io/py/underwear
    
.. image:: https://travis-ci.org/makaimc/underwear.png?branch=master
        :target: https://travis-ci.org/makaimc/underwear

.. image:: https://pypip.in/d/underwear/badge.png
        :target: https://crate.io/packages/underwear?version=latest


Underwear is a library for easily deploying any Python-powered web 
application to one or more Linux servers.

Underwear is free software under the MIT license. Additional documentation
can be found on the `Underwear Read the Docs <http://underwear.rtfd.org>`_ 
page.


What Problem Does Underwear Solve?
----------------------------------
Despite the advent of configuration management tools such as 
`Puppet <http://puppetlabs.com/puppet/what-is-puppet>`_,
`Chef <http://www.getchef.com/chef/>`_, 
`Ansible <http://www.ansibleworks.com/>`_, and 
`Salt <http://www.saltstack.com/community/>`_, it remains difficult to deploy
a web application because you have to first learn one of those tools and
then write scripts in the tool's domain-specific language.

Underwear makes deploying to a traditional Linux server stack as easy as 
deploying to Heroku by providing a pre-packaged, easily configurable library. 
Deployments can be executed simply by installing Underwear with 
`pip <http://www.pip-installer.org/en/latest/index.html>`_, specifying the
IP addresses of the server(s) to deploy to, then running a couple of commands.


Quick Start
-----------
*These instructions will be simplied in future releases as the library
is further developed*.

1. Install Underwear to your 
   `virtualenv <https://pypi.python.org/pypi/virtualenv>`_:: 

     pip install underwear

2. Add 'underwear' to INSTALLED_APPS in your Django
   project. *Underwear currently only supports Django (Flask and Bottle 
   will be added in the 0.5 release).* 

3. Create a deploy directory under your Django project::

     mkdir deploy; cd deploy


4. Download the Fabric file for uploading SSH keys, configuration template, 
   and hosts file to your project under the deploy/ directory::

     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/fabfile.py.template
     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/hosts
     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/underwear.yml

5. Fill in the **hosts** file with your servers' IP addresses. For example,
   the file may look like the following::

    [webservers]
    192.168.1.1

    [dbservers]
    192.168.1.2

6. 


Features
--------
* Automated deployments to a web & database server
* Configurable via a simple YAML template


