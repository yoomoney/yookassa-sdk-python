# -*- coding: utf-8 -*-
from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb


class Settings:
    base_path = '/me'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def get_account_settings(cls):
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path)
        return response
