from django.contrib.admin.helpers import ActionForm
from django.utils.translation import gettext_lazy as _
from django import forms


class OptionAttrsSelect(forms.widgets.Select):
    """
    Select that allows to pass option-specific extra-attributes.
    """
    def __init__(self, attrs=None, option_attrs=None, choices=()):
        super().__init__(attrs, choices)
        self.option_attrs = option_attrs or dict()

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        option['attrs'].update(self.option_attrs.get(option['value'], dict()))
        return option


class OptionAttrsActionForm(ActionForm):
    """
    _summary_
    """
    action = forms.ChoiceField(label=_("Action:"), widget=OptionAttrsSelect())
