Nimbostratus target
===================

This repository holds a target infrastructure you can use for testing [nimbostratus](https://github.com/andresriancho/nimbostratus).

This code deploys an Amazon AWS infrastructure which has various vulnerabilities and weak configuration settings which 
can be exploited using [nimbostratus](https://github.com/andresriancho/nimbostratus).

**If you're not sure what this is all about, you better avoid using any of the code that lives here.**

Installation
============

```bash
sudo apt-get install python-mysqldb
git clone git@github.com:andresriancho/nimbostratus-target.git
cd nimbostratus-target
pip install -r requirements.txt
```

Usage
=====

Starting the environment
------------------------

Pre-Requisites:
1. Make sure you have configured your "root" AWS credentials in `~/.boto` before you run the fabric script.
2. Fork the nimbostratus-target repo
3. Create a new deploy key for the forked repo and configure the paths in config.py
4. Update the variable VULNWEB_REPO in servers/django_frontend/user_data.py with new repo path
5. Update variables in config.py
    NOTE: In config.py depending on your region you will have to update the AMI-ID.  Depending on your AMI-ID
    you may have to update the 'SIZE' variable.  In most regions you will have to use a t2.micro.

```bash
fab deploy
```

The console messages will show you the progress to understand what's deployed and where.
At the end you should end up with the following AWS components:

 * Front-end EC2 instance with:
   * HTTP server and vulnerable Web application
   * Celery configured to use SQS as broker
   * Deployed using user-data script
   * With an instance profile which allows acces to SQS
 * Backend worker:
   * Consumes SQS messages sent by front-end instance
   * Uses pickle as serialization method
   * No instance profile configured, hard-coded AWS credentials
   * AWS credentials can access `RDS:*` and `IAM:*`
   * Stores information in RDS database using low-privileged user
 * RDS database
 * IAM user for backend worker

A successfull run should look like [this](https://github.com/andresriancho/nimbostratus-target/wiki/Successfull-run).

Killing the environment
-----------------------

Once you finish playing with this Amazon cloud, just delete it with:

```bash
fab teardown
```


Disclaimer
==========

 * This code wasn't developed for re-usability.
 * Running this code will create Amazon AWS charges!
 * The `teardown` command might fail, charges might be applied by Amazon even after running it. You're responsible of checking the state of your services after running this tool.
Nimbostratus
============

Tools for fingerprinting and exploiting Amazon cloud infrastructures. These tools are a PoC
which I developed for my "Pivoting in Amazon clouds" talk, developed using the great 
[boto](https://github.com/boto/boto) library for accessing Amazon's API.

For more information visit [the project page](http://andresriancho.github.io/nimbostratus/)

Feel free to report bugs, fork and send pull-requests. You can also drop me a line at
[@w3af](https://twitter.com/w3af).

