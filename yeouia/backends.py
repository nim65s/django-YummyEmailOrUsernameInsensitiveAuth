from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class YummyEmailOrUsernameInsensitiveAuth(ModelBackend):
    """
    Backend that authenticates with username or email, case insensitively
    """
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()  # noqa
        # username may contain '@', so first try with username
        # username are case sensitive by default, try case sensitively first
        try:
            user = UserModel._default_manager.get(username=username)
        except:
            try:
                user = UserModel._default_manager.get(username__iexact=username)
            except:
                try:
                    user = UserModel._default_manager.get(email__iexact=username)
                except:
                    # Run the default password hasher once to reduce the timing
                    # difference between an existing and a non-existing user (#20760).
                    user = UserModel()
        if user.check_password(password):
            return user
