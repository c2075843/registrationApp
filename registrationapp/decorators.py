from django.contrib import messages
from django.shortcuts import redirect


def login_required_with_message(message=None):
    def decorator(view_func):
        def wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                if message:
                    messages.warning(request, message)
                return redirect("accounts:login")
            return view_func(request, *args, **kwargs)

        return wrapped_view

    return decorator
