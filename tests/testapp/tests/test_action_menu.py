# from bs4 import BeautifulSoup as bs
from django.urls import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from testapp.utils import create_test_data
from testapp.models import TestModel
from testapp.admin import TestModelAdmin
from grouped_admin_actions.actions import ActionGroup
from grouped_admin_actions import __version__


class ActionMenuTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_data()

    def setUp(self):
        self.user = User.objects.get(username='admin')
        self.client.force_login(self.user)
        url_pattern = f'admin:{TestModel._meta.app_label}_{TestModel._meta.model_name}_changelist'
        self.url = reverse(url_pattern)

    def test_action_docstring_description(self):
        def action_one(m, r, q): pass
        action_one.__doc__ = 'foobar'
        TestModelAdmin.actions = [action_one]
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        html = '<option value="action_one" title="foobar">Action one</option>'
        self.assertInHTML(html, resp.content.decode('utf8'))

    def test_action_description(self):
        def action_one(m, r, q): pass
        action_one.description = 'foobar'
        TestModelAdmin.actions = [action_one]
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        html = '<option value="action_one" title="foobar">Action one</option>'
        self.assertInHTML(html, resp.content.decode('utf8'))

    def test_action_group(self):
        group_one = ActionGroup(name="Group One")
        group_two = ActionGroup(name="Group Two")
        def action_one(m, r, q): pass
        def action_two(m, r, q): pass
        def action_three(m, r, q): pass
        def action_four(m, r, q): pass
        TestModelAdmin.actions = [
            group_one(action_one),
            group_one(action_two),
            group_two(action_three),
            group_two(action_four),
        ]
        resp = self.client.get(self.url)
        self.assertEqual(resp.status_code, 200)
        html = """
            <optgroup label="Group One">
                <option value="action_one">Action one</option>
                <option value="action_two">Action two</option>
            </optgroup>
            """
        self.assertInHTML(html, resp.content.decode('utf8'))
        html = """
            <optgroup label="Group Two">
                <option value="action_three">Action three</option>
                <option value="action_four">Action four</option>
            </optgroup>
            """
        self.assertInHTML(html, resp.content.decode('utf8'))

    def test_group_permissions(self):
        group_one = ActionGroup(
            name="Group One",
            permissions=['view', 'change']
            )
        def action_one(m, r, q): pass
        action_one.allowed_permissions = ['view', 'delete']
        group_one(action_one)
        perms = ['view', 'change', 'delete']
        self.assertCountEqual(perms, action_one.allowed_permissions)
        self.assertEqual(set(perms), set(action_one.allowed_permissions))
