Shelf Life
=========================

* [About this app](#about-this-app)
* [Assumptions](#assumptions)
* [What's in here?](#whats-in-here)
* [Copy the app](#copy-the-app)
* [Configure the project](#configure-the-project)
* [Install requirements](#install-requirements)
* [Project secrets](#project-secrets)
* [Bootstrap issues](#bootstrap-issues)
* [Adding a template/view](#adding-a-templateview)
* [Run the project locally](#run-the-project-locally)
* [Deploy the app](#deploy-to-s3)

About this app
-------------------

This app provides an HTML form for embedding and a mechanism to crowdsource user-submitted content via a Tumblog.

Assumptions
-----------

The following things are assumed to be true in this documentation.

* You are running OSX.
* You are using Python 2.7. (Probably the version that came OSX.)
* You have [virtualenv](https://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](https://pypi.python.org/pypi/virtualenvwrapper) installed and working.

What's in here?
---------------

The project contains the following folders and important files:

* ``confs`` -- Server configuration files for nginx and uwsgi. Edit the templates, don't touch anything in ``confs/rendered``.
* ``data`` -- Data files, such as those used to generate HTML.
* ``etc`` -- Miscellaneous scripts and metadata for project bootstrapping.
* ``jst`` -- Javascript ([Underscore.js](http://documentcloud.github.com/underscore/#template)) templates.
* ``less`` -- [LESS](http://lesscss.org/) files, will be compiled to CSS and concatenated for deployment.
* ``templates`` -- HTML ([Jinja2](http://jinja.pocoo.org/docs/)) templates, to be compiled locally.
* ``tests`` -- Python unit tests.
* ``www`` -- Static and compiled assets to be deployed. (a.k.a. "the output")
* ``www/live-data`` -- "Live" data deployed to S3 via cron jobs or other mechanisms. (Not deployed with the rest of the project.)
* ``www/test`` -- Javascript tests and supporting files.
* ``app.py`` -- A [Flask](http://flask.pocoo.org/) app for rendering the project locally.
* ``app_config.py`` -- Global project configuration for scripts, deployment, etc.
* ``crontab`` -- Cron jobs to be installed as part of the project.
* ``fabfile.py`` -- [Fabric](http://docs.fabfile.org/en/latest/) commands automating setup and deployment.
* ``public_app.py`` -- A simple Flask dynamic app that provides an endpoint for form POSTs.

Copy the app
-----------------

```
git clone git@github.com:nprapps/shelf-life.git

cd shelf-life
```

Configure the project
---------------------

Edit ``app_config.py`` and update ``PROJECT_NAME``, ``DEPLOYED_NAME``, ``REPOSITORY_NAME`` any other relevant configuration details.

NPR apps-specific: Update relevant environment variables with API keys, etc., from Dropbox:

You can either source ``~/Dropbox/nprapps/tumblr_oauth_keys.txt`` (variables will only be set for the life of your current shell):

```
. ~/Dropbox/nprapps/tumblr_oauth_keys.txt
```

Or you can append its contents to your bash_profile|bashrc|zshrc:

```
cat ~/Dropbox/nprapps/tumblr_oauth_keys.txt >> ~/.zshrc
```

Install requirements
--------------------

Node.js is required for the static asset pipeline. If you don't already have it, get it like this:

```
brew install node
curl https://npmjs.org/install.sh | sh
```

Then install the project requirements:

```
cd shelf-life
npm install less universal-jst
mkvirtualenv shelf-life
pip install -r requirements.txt
```

Project secrets
---------------

Project secrets should **never** be stored in ``app_config.py`` or anywhere else in the repository. They will be leaked to the client if you do. Instead, always store passwords, keys, etc. in environment variables and document that they are needed here in the README.

Bootstrap issues
----------------

The app-template can automatically setup your Github repo with our default labels and tickets by running ``fab bootstrap_issues``. You will be prompted for your Github username and password.

Adding a template/view
----------------------

A site can have any number of rendered templates (i.e. pages). Each will need a corresponding view. To create a new one:

* Add a template to the ``templates`` directory. Ensure it extends ``_base.html``.
* Add a corresponding view function to ``app.py``. Decorate it with a route to the page name, i.e. ``@app.route('/filename.html')``
* By convention only views that end with ``.html`` and do not start with ``_``  will automatically be rendered when you call ``fab render``.

Run the project locally
-----------------------

A flask app is used to run the project locally. It will automatically recompile templates and assets on demand.

```
workon shelf-life
python app.py
```

`app.py` is used for the Tumblr form which will be baked out to a flat file.

To run the simple app that will post to Tumblr (via intermediate server for image uploads):

```
python public_app.py
```

This will run on `:8001`.

Visit [localhost:8000](http://localhost:8000) in your browser.

Deploy the app
------------

There are two parts – deploy the form to S3 and the simple app (`public_app.py`) to EC2.

* Run ``fab <ENV> master setup`` to configure the server (where ENV is either staging or production).
* Run ``fab <ENV> master deploy`` to deploy the app.
* Run ``fab <ENV> deploy_confs`` to render the server conf files (nginx and uwsgi) and then deploy them to the server. This will also restart your app on the server.
