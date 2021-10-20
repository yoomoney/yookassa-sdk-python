# -*- coding: utf-8 -*-
from yookassa.client import ApiClient
from yookassa.domain.common.http_verb import HttpVerb


class Settings:
    base_path = '/me'

    def __init__(self):
        self.client = ApiClient()

    @classmethod
    def get_account_settings(cls, params=None):
        """
        Shop Info

        :param params: (dict | None) Параметры поиска.
            В настоящее время доступен только {'on_behalf_of': account_id}
        :return: dict
        """
        instance = cls()
        path = cls.base_path

        response = instance.client.request(HttpVerb.GET, path, params)
        return response
