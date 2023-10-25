

class ActionGroup:
    def __init__(self, name, permissions=None):
        self.name = name
        self.permissions = permissions

    def __call__(self, func):
        func.group = self.name
        if self.permissions:
            action_perms = getattr(func, 'allowed_permissions', [])
            func.allowed_permissions = list(set(action_perms + self.permissions))
        return func