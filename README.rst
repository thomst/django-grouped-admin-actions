=======================================
Welcome to django-grouped-admin-actions
=======================================

.. image:: https://github.com/thomst/django-grouped-admin-actions/actions/workflows/tests.yml/badge.svg
   :target: https://github.com/thomst/django-grouped-admin-actions/actions/workflows/tests.yml
   :alt: Run tests for django-grouped-admin-actions

.. image:: https://coveralls.io/repos/github/thomst/django-grouped-admin-actions/badge.svg?branch=main
   :target: https://coveralls.io/github/thomst/django-grouped-admin-actions?branch=main
   :alt: coveralls badge

.. image:: https://img.shields.io/badge/python-3.8+-blue
   :target: https://img.shields.io/badge/python-3.8+-blue
   :alt: python: 3.8+

.. image:: https://img.shields.io/badge/django-2.2%20%7C%203.0%20%7C%203.1%20%7C%203.2%20%7C%204.0%20%7C%204.1%20%7C%204.2%20%7C%205.0%20%7C%205.1%20%7C%205.2%20%7C%206.0-orange
   :target: https://img.shields.io/badge/django-2.2%20%7C%203.0%20%7C%203.1%20%7C%203.2%20%7C%204.0%20%7C%204.1%20%7C%204.2%20%7C%205.0%20%7C%205.1%20%7C%205.2%20%7C%206.0-orange
   :alt: django: 2.2, 3.0, 3.1, 3.2, 4.0, 4.1, 4.2, 5.0, 5.1, 5.2, 6.0


Description
===========
You habe lots of admin actions in your django admin? Improve the usability of
your admin action dropdown by using option groups and the action's docstring as
title tag.


Installation
============
Install from pypi.org::

    pip install django-grouped-admin-actions


Usage
=====
Use the `GroupedAdminActionsMixin` in your `ModelAdmin` classes::

    from django.contrib import admin
    from grouped_admin_actions.admin import GroupedAdminActionsMixin
    from .models import YourModel

    @admin.register(YourModel)
    class YourModelAdmin(GroupedAdminActionsMixin, admin.ModelAdmin):
        actions = [
            'action_one',
            'action_two',
            'action_three',
            ...
        ]

Setup your admin actions with meaningful docstrings and use action groups as
decorator::

    from grouped_admin_actions.admin import action_group

    group_one = ActionGroup("Action 1")
    group_two = ActionGroup("Action 2")

    @group_one
    def action_one(modeladmin, request, queryset):
        """This is action one in group 1."""
        ...

    @group_one
    def action_two(modeladmin, request, queryset):
        """This is action two in group 1."""
        ...

    @group_two
    def action_three(modeladmin, request, queryset):
        """This is action three in group 2."""
        ...

Now you get a grouped action dropdown in your dango admin changelist views with
the action's docstring as title tag of each option.
