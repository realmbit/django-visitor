.. django-visitor documentation master file, created by
   sphinx-quickstart on Tue Jul 26 07:25:04 2011.

Welcome to django-visitor's documentation!
==========================================

Requirements
------------

Django 1.1 or newer

Code Repo
---------

 * https://bitbucket.org/kencochrane/django-visitor

Installation
------------

Use pip to fetch the code::

    pip install django-visitor
    
Make sure that that sessions are activated::

    INSTALLED_APPS = (
        'django.contrib.sessions',
        ...   
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        ...
    )    
    
Add `visitor` to your INSTALLED_APPS::

    INSTALLED_APPS = (
        ...
        'visitor',
    )

Add the visitor middleware::

    MIDDLEWARE_CLASSES = (
        ...
        'visitor.middleware.VisitorMiddleware'
        ...
    )

Now load up the tables in your database::

    python manage.py syncdb

Required Settings
-----------------

Add the following two properties to your settings file::

    COOKIE_DOMAIN
        Default = None # Which means local domain only  www.domain.com but no funky.domain.com
        # if you want cookie to work across all subdomains, put '.domain.com' 
        COOKIE_DOMAIN = None # .domain.com

    COOKIE_MAX_AGE
        Default = 31536000 # or 1 year.
        # This is how long the cookie will live in your visitors browser before it expires on it's own
        COOKIE_MAX_AGE = 31536000 # 1 year

Custom settings
---------------

These settings can be overridden::

    VISITOR_KEY
        Default = 'visitor_key'

    COOKIE_SAVED
        Default = 'cookie_saved'

    COOKIE_VISITOR_KEY
        Default = 'vk'

    REQUEST_LOG_ID
        Default = 'request_log_id'
        
References
----------
        
.. toctree::
    :maxdepth: 2

    ref_visitor_managers
    ref_visitor_middleware
    ref_visitor_models
    ref_visitor_utils
    


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

