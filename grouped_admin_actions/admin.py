from collections import OrderedDict
from django.contrib import admin
from django.db import models
from django.contrib.admin.utils import model_format_dict
from .forms import OptionAttrsActionForm


class GroupedActionsModelAdminMixin:
    """
    _summary_
    """

    action_form = OptionAttrsActionForm

    def get_action_choices(self, request, default_choices=models.BLANK_CHOICE_DASH):
        choices = [] + default_choices
        groups = OrderedDict()
        for func, name, description in self.get_actions(request).values():
            choice = (name, description % model_format_dict(self.opts))
            group_name = self._get_action_group(func)
            if group_name:
                if not group_name in groups:
                    groups[group_name] = []
                groups[group_name].append(choice)
            else:
                choices.append(choice)
        if groups:
            choices.extend(groups.items())
        return choices

    def _get_action_option_attrs(self, actions):
        extra_attrs = {}
        for func, name, _ in actions.values():
            description = self._get_action_verbose_description(func)
            if description:
                extra_attrs[name] = {'title': description}
        return extra_attrs

    def get_actions(self, request):
        actions = super().get_actions(request)

        option_attrs = self._get_action_option_attrs(actions)
        self.action_form.base_fields['action'].widget.option_attrs = option_attrs
        return actions

    @staticmethod
    def _get_action_verbose_description(func):
        return getattr(func, "description", func.__doc__ or None)

    @staticmethod
    def _get_action_group(func):
        return getattr(func, "group", None)


class GroupedActionsModelAdmin(GroupedActionsModelAdminMixin, admin.ModelAdmin):
    """
    _summary_
    """
