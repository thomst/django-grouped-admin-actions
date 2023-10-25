from django.contrib import admin
from grouped_admin_actions.admin import GroupedActionsModelAdmin
from .models import TestModel
from .actions import action_one
from .actions import action_two
from .actions import action_three
from .actions import action_four
from .actions import action_five
from .actions import action_six


@admin.register(TestModel)
class TestModelAdmin(GroupedActionsModelAdmin):
    list_display = ['id', 'one', 'two', 'three']
    actions = [
        action_one,
        action_two,
        action_three,
        action_four,
        action_five,
        action_six,
        ]
