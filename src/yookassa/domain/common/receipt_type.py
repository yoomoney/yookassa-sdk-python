# -*- coding: utf-8 -*-


class ReceiptType:
    """
    Constants representing receipt types. Available values are:
    """
    PAYMENT = 'payment'
    REFUND = 'refund'


class ReceiptItemAgentType:
    """
    Constants representing receipt item agent types. Available values are:
    """
    BANKING_PAYMENT_AGENT = 'banking_payment_agent'
    BANKING_PAYMENT_SUBAGENT = 'banking_payment_subagent'
    PAYMENT_AGENT = 'payment_agent'
    PAYMENT_SUBAGENT = 'payment_subagent'
    ATTORNEY = 'attorney'
    COMMISSIONER = 'commissioner'
    AGENT = 'agent'
