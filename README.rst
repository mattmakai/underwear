===============================
Underwear
===============================

.. image:: https://badge.fury.io/py/underwear.png
    :target: http://badge.fury.io/py/underwear
    
.. image:: https://travis-ci.org/makaimc/underwear.png?branch=master
        :target: https://travis-ci.org/makaimc/underwear

.. image:: https://pypip.in/d/underwear/badge.png
        :target: https://crate.io/packages/underwear?version=latest


Underwear is a simple, two-command installation library for deploying any
Python-powered web application to one or more Linux servers.

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
a new web application because you have to first learn one of those tools and
then write scripts in the tool's domain-specific language.

Underwear aims to eliminate the need to learn one of the tools and write
the scripts by providing a pre-packaged, simple configurable library. 
Deployments can be executed simply by installing Underwear with 
`pip <http://www.pip-installer.org/en/latest/index.html>`_, specifying the
IP addresses of the server(s) to deploy to, then running a single command.


Features
--------
* Automated deployments to a web & database server
* Configurable via a simple YAML template


