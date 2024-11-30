from django.contrib.auth.mixins import UserPassesTestMixin


class SupervisorsGroupRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='supervisors').exists()

class SalesmenGroupRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='salesmen').exists()

class CustomersGroupRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.groups.filter(name='customers').exists()