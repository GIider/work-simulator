# -*- coding: utf-8 -*-
import os

DEBUG = True

# Use os.urandom(32) to generate a new secret key every time we restart
# to invalidate the session.
# If you want a persisting session while you modify files simply use a static
# string
SECRET_KEY = 'Bruce Schneier knows Alice and Bob\'s shared secret.'  # os.urandom(32)

SQLALCHEMY_DATABASE_URI = 'sqlite:///db{}work_simulator.db'.format(os.sep)