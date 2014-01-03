.. :changelog:

History
-------

0.4.4 (2014-01-05)
++++++++++++++++++
* Changing Django management command defaults to deploy directory within the
  project instead of your ~/.ssh key directory.


0.4.3 (2014-01-02)
++++++++++++++++++
* Adding toggle for whether South should be used with a Django project 
  (django_use_south) and a toggle for whether a fixtures file should be
  loaded (django_fixtures_file).


0.4.2 (2013-12-30)
++++++++++++++++++
* Added toggle to flip whether or not SSL should be used with Nginx 
  (deploy_ssl).


0.4.0 (2013-12-26)
++++++++++++++++++
* Release now allows for 2 server web app deployments (one web server and
  one database server).
* Fixes issues with Supervisor template and Django environment variables.
* Includes templates required to tell the library where to deploy the 
  application.


0.3.0 (2013-12-24)
++++++++++++++++++
* First release on PyPI.


0.2.0 (2013-12-16)
++++++++++++++++++
* Added initial working Ansible scripts for deployment.


0.1.0 (2013-12-16)
++++++++++++++++++
* Initial codebase with Python package
