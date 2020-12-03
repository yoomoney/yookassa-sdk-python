# -*- coding: utf-8 -*-


class CardType:
    """
    Class representing credit cards available types enum
    """
    MASTER_CARD = 'MasterCard'
    VISA = 'Visa'
    MIR = 'MIR'
    UNION_PAY = 'UnionPay'
    CUP = 'CUP'
    JCB = 'JCB'
    AMERICAN_EXPRESS = 'AmericanExpress'
    DINERS_CLUB = 'DinersClub'
    UNKNOWN = 'Unknown'


class CardSource:
    """
    Class representing enum of available sources of credit cards
    """
    APPLE_PAY = 'apple_pay'
    GOOGLE_PAY = 'google_pay'
