from django.db.models import CharField, EmailField

from django_case_insensitive_field import CaseInsensitiveFieldMixin


class CaseInsensitiveCharField(CaseInsensitiveFieldMixin, CharField):
    """[summary]
    Makes django CharField case insensitive
    Extends both the `CaseInsensitiveMixin` and  CharField
    Then you can import 
    """

    def __init__(self, *args, **kwargs):

        super(CaseInsensitiveFieldMixin, self).__init__(*args, **kwargs) 

class CaseInsensitiveEmailField(CaseInsensitiveFieldMixin, EmailField):
    """
    Makes the django emailfield case insensitive
    """

    def __init__(self, *args, **kwargs):
        super(CaseInsensitiveFieldMixin, self).__init__(*args, **kwargs)

