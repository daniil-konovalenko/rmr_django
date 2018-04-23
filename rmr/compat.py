import django


def user_is_authenticated(user):
    """
    django.contrib.auth.models.User.is_authenticated is a property since django 1.10
    """
    if django.VERSION < (1, 10):
        return user.is_authenticated()
    
    return user.is_authenticated


try:
    from django.urls import include, path, re_path, register_converter
except ImportError:
    from django.conf.urls import include, url
    path = None
    register_converter = None
    re_path = url


try:
    from django.urls import reverse
except ImportError:
    # django.core.urlresolvers.reverse is deprecated since Django 1.10 and was removed in Django 2.0
    # https://docs.djangoproject.com/en/1.11/ref/urlresolvers/
    from django.core.resolvers import reverse
