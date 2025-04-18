# Yummy Email Or Username Insensitive Auth model backend for Django

[![PyPI version](https://badge.fury.io/py/yeouia.svg)](https://pypi.org/project/yeouia)
[![Tests](https://github.com/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/actions/workflows/test.yml/badge.svg)](https://github.com/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/actions/workflows/test.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/main.svg)](https://results.pre-commit.ci/latest/github/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/main)
[![codecov](https://codecov.io/gh/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/branch/main/graph/badge.svg?token=APCEYTJRV3)](https://codecov.io/gh/nim65s/django-YummyEmailOrUsernameInsensitiveAuth)
[![Maintainability](https://api.codeclimate.com/v1/badges/6737a84239590ddc0d1e/maintainability)](https://codeclimate.com/github/nim65s/django-YummyEmailOrUsernameInsensitiveAuth/maintainability)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## Instructions

1. `pip install yeouia`
2. Add `AUTHENTICATION_BACKENDS = ['yeouia.backends.YummyEmailOrUsernameInsensitiveAuth']` to your `settings.py`
3. Enjoy

## Requirements

Tested for

* Python 3.10, 3.11, 3.12, 3.13
* Django 5+

May work otherwise, but you should run tests :P

## Case Insensitive ?

Django's default auth username is *not* case insensitive.
(See [#2273](https://code.djangoproject.com/ticket/2273) and [#25617](https://code.djangoproject.com/ticket/25617))

But… Who cares ?

This backend tries:

1. username, case sensitive
2. username, case insensitive
3. email, case insensitive

And follows [#20760](https://code.djangoproject.com/ticket/20760).
