# custom_admin.py

from django.contrib.admin import AdminSite
from django.contrib.admin.sites import site as default_admin_site


class CustomAdminSite(AdminSite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.site_header = 'Enterprise Management Software'


custom_admin_site = CustomAdminSite(name='custom_admin')
custom_admin_site._registry = default_admin_site._registry


