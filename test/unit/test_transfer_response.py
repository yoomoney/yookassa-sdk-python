# -*- coding: utf-8 -*-
import unittest

from yookassa.domain.models import Amount, Currency
from yookassa.domain.response import TransferResponse, TransferStatus


class TestTransferResponse(unittest.TestCase):

    def test_transfer_cast(self):
        self.maxDiff = None
        transfer = TransferResponse()
        transfer.status = TransferStatus.SUCCEEDED
        transfer.account_id = '79990000000'
        transfer.amount = Amount({
            "value": '100.01',
            "currency": Currency.RUB
        })
        transfer.metadata = {
            "meta1": 'metatest 1',
            "meta2": 'metatest 2'
        }

        self.assertEqual({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)
        self.assertEqual(TransferStatus.SUCCEEDED, transfer.status)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(float(transfer.amount.value), 100.01)
        self.assertEqual({"meta1": 'metatest 1', "meta2": 'metatest 2'}, dict(transfer.metadata))

        with self.assertRaises(TypeError):
            transfer.amount = 'invalid type'

    def test_transfer_value(self):
        self.maxDiff = None
        transfer = TransferResponse({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        })

        self.assertEqual({
            "account_id": "79990000000",
            "amount": {
                "value": 100.01,
                "currency": Currency.RUB
            },
            "status": TransferStatus.SUCCEEDED,
            "metadata": {
                "meta1": 'metatest 1',
                "meta2": 'metatest 2'
            }
        }, dict(transfer))

        self.assertEqual('79990000000', transfer.account_id)
        self.assertEqual(TransferStatus.SUCCEEDED, transfer.status)

        self.assertEqual({"value": 100.01, "currency": Currency.RUB}, dict(transfer.amount))
        self.assertEqual(float(transfer.amount.value), 100.01)
        self.assertEqual({"meta1": 'metatest 1', "meta2": 'metatest 2'}, dict(transfer.metadata))
