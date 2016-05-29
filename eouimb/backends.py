from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class EmailOrUsernameInsensitiveModelBackend(ModelBackend):
    """
    This backends lets an user authenticate with his username or email, case insensitive
    """
    def authenticate(self, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            # username may contain '@', so first try with username
            user = UserModel._default_manager.get(username__iexact=username)
        except:
            try:
                user = UserModel._default_manager.get(email__iexact=username)
            except:
                # Run the default password hasher once to reduce the timing
                # difference between an existing and a non-existing user (#20760).
                UserModel().set_password(password)
        if user.check_password(password):
            return user
