from django.contrib import admin


class ListAdminMixin(object):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        super(ListAdminMixin, self).__init__(model, admin_site)


def register_models(*args):
    for model in args:
        admin_class = type('AdminClass', (ListAdminMixin, admin.ModelAdmin), {})
        try:
            admin.site.register(model, admin_class)
        except admin.sites.AlreadyRegistered:
            pass
