from grouped_admin_actions.actions import ActionGroup


group_one = ActionGroup("Action One")
group_two = ActionGroup("Action Group")


@group_one
def action_one(modeladmin, request, queryset):
    """
    Action one doing nothing.
    """

@group_one
def action_two(modeladmin, request, queryset):
    pass

@group_two
def action_three(modeladmin, request, queryset):
    pass


def action_four(modeladmin, request, queryset):
    pass

@group_two
def action_five(modeladmin, request, queryset):
    pass


def action_six(modeladmin, request, queryset):
    pass
