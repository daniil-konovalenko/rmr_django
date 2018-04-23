import django


def user_is_authenticated(user):
    """
    django.contrib.auth.models.User.is_authenticated is a property since django 1.10
    """
    if django.VERSION < (1, 10):
        return user.is_authenticated()
    
    return user.is_authenticated
