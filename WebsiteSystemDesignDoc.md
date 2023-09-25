# Ch1: High Level overview of purpose:

The purpose of this document is to outline my process.

The progress I make while building my website and the different things I try.

Ideally, I would want this document to be as diverse as possible, using
different frameworks and libraries across different languages.

Given my current limitation though, this may take time…

So bear with me.

PS: I'm definitely excited about this and what potential it holds

Summary and additional features (af) :

Build a website to pull in data from my google keepnotes

  1. Build website
  2. Create API integration with google keep notes

  1. (Af) For this, also add an integration that programmatically created a GitHub repo for all notes with "idea" in title, keyword, and key: "body" where "body" is title**

  1. Will need to manually vet each repo then programmatically drop repos that aren't relevant (something along the lines of deleting the keywords from the notes? Then deleting where not matched?)

  3. (Af) Also add YouTube and IG data - future state

# Ch2. Hello World - research and whatnot

Day one: Looking up Django vs different JS frameworks and libraries
(apparently React is a lib, not a framework…whatever that means)

Django Project:

This should have been included earlier on, but what I will show now is a high
level overview of the project plan and architecture.

More details can be found for each stage by clicking into the link:

Project flow chart / plan:

Front end(client) -

JavaScript - Angular, Vue, React, Node*

CSS - Tailwind*

HTML

* - TBD

Back end (server):

WEbserver - NGINX for DNS routing and load balancing? TBD

Language: Python via Django

Database - TBD

# Ch3 System Design and Architecture diagram

Step 1 - Hello world html - 1hr - DONE

Step 2 - Check if you can actually host on your raspberry pi - Yes, but
difficult

Step 3 -

  1. Product Requirements: High level diagram

  1. Most important features, 
  2. Resilience (to avoid a single point of failure) - load balancing
  3. Extensibility: How easy is it to change the solution, 

  1. E.g. send code to multiple users, and implement read receipts.
  2. Need to make sure that you can scale horizontally  and make sure that you can expand this
  3. Build a system that can Scale and extend as more users use it.

  4. Testing: Edge cases and common cases. - use tools to load test, before getting into the code.

  2. Features/Abstract Concepts
  3. Data Definitions 
  4. Mapped (data def) into Objects
  5. Mapped (Objects) into DB - APIs (FTP, Rest, GRPC, HTML, FTP, doesn't matter rn)
  6. Low level diagram

  1. Use case diagram: 

Customer use case, how you want them to interact with the product

  2. Class Diagrams:

Objects needed to achieve the specific use cases

  3. Sequence Diagram:

How the flow works from the User, to services and so on (including DB?) -
Think API calls

NOTE: Important to use placeholders first for different parts of your website
to make sure that they work, in linking together before expanding on the more
robust parts.

2.1.1 - Product Requirements:

        Most important features

  1. Resilience (to avoid a single point of failure) - load balancing, server access

  1. Raspberry Pi server \- NGINX? AWS, - on Docker?

Maybe use GODADDY or BLUEHOST if all else fails.

  2. Extensibility: How easy is it to change the solution and expand on it 

  1. E.g. update the code, include features for adding new django projects, apps and models to those projects

  1. In this use case, it should be flexible enough to include details on multiple projects that you are working on.

  2. Need to make sure that you can scale horizontally  and make sure that you can expand this.
  3. Build a system that can Scale and extend as more users use it.

  3. Testing: Edge cases and common cases. - use tools to load test, before getting into the code.

Client --\- HTTP, TCP, UDP WebRTC-->  Server ---S3, Mysql, JSON,
NoSQL--------> Database

How to approach:

Think of the data you need to store:

Or

Think of the end user: Favourable approach, as long as your data is not too
complex.

Use case diagram

# Ch2.x. Procrastination station - personal notes

This probably won't make it to the final draft, but it has been a while since
I last updated the "site"

Today, I went back to the basics and did some research on architecture types
and registered the domain:

[kitanogunkoya.com](https://www.google.com/url?q=http://kitanogunkoya.com&sa=D&source=editors&ust=1695601724697697&usg=AOvVaw3_xcM0lEWFarze7DUGF57Q)

I also want to add kitanog.com and kitogsol.com to direct to either the same
page or different parts of the site.

But I promised myself that I would only do that after I've made some
significant progress

Getting a bit ahead of myself but yeah.

# Ch3.x - SERVER SIDE Django

Some things to consider first:

Use a virtualenvironment:

E.g. pipenv or virtualenv:

[https://learndjango.com/tutorials/django-best-practices-projects-vs-
apps](https://www.google.com/url?q=https://learndjango.com/tutorials/django-
best-practices-projects-vs-
apps&sa=D&source=editors&ust=1695601724698806&usg=AOvVaw1HsVAgBTWoEGNaZOwoMYcW)

The goal of this portion is to document the use of the Django framework as my
backend.

[https://docs.djangoproject.com/en/4.1/intro](https://www.google.com/url?q=https://docs.djangoproject.com/en/4.1/intro&sa=D&source=editors&ust=1695601724699144&usg=AOvVaw1Q7ay86DXj9hjhR1nOSgS9)

Google Keep Notes -> Backend (Server side) - Continuous Sync

Backend (Server side): Dango App.

Within the Django app, there will be multiple models

Model: Each model is a Python class, which makes up the Table in your DB (in
my case SQLite).

You create the model, or tell Django that changes have been made to the model
by running:

Manage.py makemigrations

The contents (fields) of the python class, make up the columns of the table as
well as the data definitions of the column types -
[https://docs.djangoproject.com/en/4.1/intro/tutorial02/](https://www.google.com/url?q=https://docs.djangoproject.com/en/4.1/intro/tutorial02/&sa=D&source=editors&ust=1695601724700306&usg=AOvVaw2BJoSz-
u-B_yh9tHtq9PAn)

SQL code is executed to create these tables, when you run -

manage.py migrate

NOTE:

You can run manage.py SQLmigrate to see the SQL code that will be executed to
generate the tables, this can be changed as well.

The auto generated SQL also adds IDs for each table created (i.e, IDs that can
be used to run queries, think of
[Sequences](https://www.google.com/url?q=https://docs.snowflake.com/en/sql-
reference/sql/create-
sequence.html&sa=D&source=editors&ust=1695601724700855&usg=AOvVaw0U1c9eUwguP1aOWZO2i2Gc)
in Snowflake)

Chx: Milestones

  1. Learn basics of Django
  2. Basic system design. High level
  3. Build framework for website
  4. Detailed system design, classes for site framework.
  5. Push keep notes data to website (V1. Mod Feb)
  6. Look into layout and design options
  7. 

Ch 3.xx:

Issues:

The test for the keep notes has proven difficult.

Apparently Google doesn't let you access the API u less you're an enterprise?

I tried using OAuth as well as the service account but kept getting no files

Note: for the service account, you will need to copy the service account email
and share it directly.

Might end up needing to use some 3rd party app, such as this GitHub app (will
link later)

I tested with access to the drive API and was able to successfully list files
using both OAuth and the service account (shared one file here)

SOLUTION:

        Using an open source github repo, I was able to get most of the high level requirements:

Forked and saved here:

[https://github.com/kitanog/gkeepapi_ko](https://www.google.com/url?q=https://github.com/kitanog/gkeepapi_ko&sa=D&source=editors&ust=1695601724702855&usg=AOvVaw0SjfeIZvQ9TR630fSu4bAZ)

