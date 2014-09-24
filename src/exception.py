# -*- coding: utf-8 -*-


class NotEnoughMoneyException(BaseException):
    """Exception to raise when a purchase can't be made due to lack of fonds"""
    pass