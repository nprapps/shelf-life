#!/usr/bin/env python

"""
Project-wide application configuration.

DO NOT STORE SECRETS, PASSWORDS, ETC. IN THIS FILE.
They will be exposed to users. Use environment variables instead.
"""

import os

PROJECT_NAME = 'What the Fridge'
PROJECT_SLUG = 'what-the-fridge'
REPOSITORY_NAME = 'what-the-fridge'

PRODUCTION_S3_BUCKETS = ['apps.npr.org', 'apps2.npr.org']
PRODUCTION_SERVERS = ['50.112.9.120']

STAGING_S3_BUCKETS = ['tumblr-stage.npr.org']
# STAGING_SERVERS = ['50.112.87.147']
STAGING_SERVERS = PRODUCTION_SERVERS

S3_BUCKETS = []
SERVERS = []
DEBUG = True

PROJECT_DESCRIPTION = 'An opinionated project template for client-side apps.'
SHARE_URL = 'http://%s/%s/' % (PRODUCTION_S3_BUCKETS[0], PROJECT_SLUG)

TWITTER = {
    'TEXT': PROJECT_NAME,
    'URL': SHARE_URL
}

FACEBOOK = {
    'TITLE': PROJECT_NAME,
    'URL': SHARE_URL,
    'DESCRIPTION': PROJECT_DESCRIPTION,
    'IMAGE_URL': '',
    'APP_ID': '138837436154588'
}

NPR_DFP = {
    'STORY_ID': '171421875',
    'TARGET': '\/news_politics;storyid=171421875'
}

GOOGLE_ANALYTICS_ID = 'UA-5828686-4'

TUMBLR_TAGS = 'food, noms'

def get_secrets():
    """
    A method for accessing our secrets.
    """
    secrets = [
        'TUMBLR_OAUTH_TOKEN',
        'TUMBLR_OAUTH_TOKEN_SECRET',
        'TUMBLR_APP_SECRET',
        'AWS_SECRET_ACCESS_KEY',
        'AWS_ACCESS_KEY_ID'
    ]
    secrets_dict = {}
    for secret in secrets:
        secrets_dict[secret] = os.environ.get(secret, None)

    return secrets_dict

def configure_targets(deployment_target):
    """
    Configure deployment targets. Abstracted so this can be
    overriden for rendering before deployment.
    """
    global S3_BUCKETS
    global SERVERS
    global DEBUG
    global TUMBLR_URL
    global TUMBLR_BLOG_ID

    if deployment_target == 'production':
        S3_BUCKETS = PRODUCTION_S3_BUCKETS
        SERVERS = PRODUCTION_SERVERS
        DEBUG = False
        # TUMBLR_URL = '{{ project_slug }}.tumblr.com'
        # TUMBLR_BLOG_ID = '{{ project_slug }}'

        # Hard-coding due to obfuscated tumblr URL
        TUMBLR_URL = 'wukkdi.tumblr.com'
        TUMBLR_BLOG_ID = 'wukkdi'

    else:
        S3_BUCKETS = STAGING_S3_BUCKETS
        SERVERS = STAGING_SERVERS
        DEBUG = True
        # TUMBLR_URL = '{{ project_slug }}-staging.tumblr.com'
        # TUMBLR_BLOG_ID = '{{ project_slug}}-staging'

        # Hard-coding due to obfuscated tumblr URL
        TUMBLR_URL = 'wukkdi-staging.tumblr.com'
        TUMBLR_BLOG_ID = 'wukkdi-staging'

DEPLOYMENT_TARGET = os.environ.get('DEPLOYMENT_TARGET', None)

configure_targets(DEPLOYMENT_TARGET)
