# -*- coding: utf-8 -*-
from functools import wraps

from flask import session, request, redirect, url_for


def login_required(f):
    """Decorator for pages that require the user to be logged in"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('username', None) is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)

    return decorated_function