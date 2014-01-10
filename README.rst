===============================
Underwear
===============================

.. image:: https://badge.fury.io/py/underwear.png
    :target: http://badge.fury.io/py/underwear
    
.. image:: https://travis-ci.org/makaimc/underwear.png?branch=master
        :target: https://travis-ci.org/makaimc/underwear


Underwear is a library for easily deploying any Python-powered web 
application to one or more Linux servers. Underwear is configurable by
a YAML template and takes care of installing packages, configuring web/WSGI
servers, and securing the server.


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
After these ten steps your app should be completely configured, 
secured, and deployed to remote servers. 

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


4. Download the Fabric file for uploading SSH keys, YAML configuration 
   template, and hosts file to your project under the deploy/ directory::

     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/fabfile.py
     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/underwear.yml
     wget https://raw.github.com/makaimc/underwear/master/underwear/deploy/hosts

5. Fill in blank variables fields in **fabfile.py**.

6. Execute the Fabric script (the script will prompt you for the non-root 
   password)::
    
     fab bootstrap_ansible

7. Fill in blank fields and modify desired settings in the **underwear.yml**
   file so that Underwear knows where to install your web application.

8. Fill in the **hosts** file with your servers' IP addresses. For example,
   the file may look like the following::
    
    [webservers]
    192.168.1.1

    [dbservers]
    192.168.1.2

8. Deploy your application::

    python manage.py deploy

9. Underwear will output each step in the deployment process to standard
   output as it happens.

10. Access your application from the domain name you provided in the 
    underwear.yml file.


License and Documentation
-------------------------
Underwear is free software under the MIT license. 

Additional Underwear documentation can be found on 
`Read the Docs <http://underwear.rtfd.org>`_.


About the Name "Underwear"
--------------------------
This library goes underneath your WSGI application to help you quickly deploy
it to traditional servers. Otherwise no one knows you're using it, and you
can swap it out at any time for another deployment process when you outgrow
the standard LAMP-stack setup.

There also weren't any projects on GitHub by the name of underwear that had
more than two stars and "underwear" was an open library name on PyPi :)


Features
--------
* Automated WSGI application deployments to a web & database server
* Configurable via a simple YAML template
* Support for ad hoc deployment needs without SSH-ing into remote servers


