# -*- coding: utf-8 -*-
from yookassa.domain.common.user_agent import Version


class ConfigurationError(Exception):
    pass


class Configuration(object):
    """
    A class representing the configuration.
    """
    api_url = "https://api.yookassa.ru/v3"
    account_id = None
    secret_key = None
    timeout = 1800
    max_attempts = 3
    auth_token = None
    agent_framework = None
    agent_cms = None
    agent_module = None

    def __init__(self, **kwargs):
        self.assert_has_api_credentials()

    @staticmethod
    def configure(account_id, secret_key, **kwargs):
        Configuration.account_id = account_id
        Configuration.secret_key = secret_key
        Configuration.auth_token = None
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)

    @staticmethod
    def configure_auth_token(token, **kwargs):
        Configuration.account_id = None
        Configuration.secret_key = None
        Configuration.auth_token = token
        Configuration.timeout = kwargs.get("timeout", 1800)
        Configuration.max_attempts = kwargs.get("max_attempts", 3)

    @staticmethod
    def configure_user_agent(framework=None, cms=None, module=None):
        if isinstance(framework, Version):
            Configuration.agent_framework = framework
        if isinstance(cms, Version):
            Configuration.agent_cms = cms
        if isinstance(module, Version):
            Configuration.agent_module = module

    @staticmethod
    def instantiate():
        return Configuration(
            shop_id=Configuration.account_id,
            shop_password=Configuration.secret_key,
            timeout=Configuration.timeout,
            max_attempts=Configuration.max_attempts,
            auth_token=Configuration.auth_token,
            agent_framework=Configuration.agent_framework,
            agent_cms=Configuration.agent_cms,
            agent_module=Configuration.agent_module
        )

    @staticmethod
    def api_endpoint():
        return Configuration.api_url

    def has_api_credentials(self):
        return self.account_id is not None and self.secret_key is not None

    def assert_has_api_credentials(self):
        if self.auth_token is None and not self.has_api_credentials():
            raise ConfigurationError("account_id and secret_key are required")
        elif self.auth_token and self.has_api_credentials():
            raise ConfigurationError("Could not configure authorization with auth_token and basic auth")
