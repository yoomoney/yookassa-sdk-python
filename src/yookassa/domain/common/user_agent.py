# -*- coding: utf-8 -*-
import platform
import sys

import distro

import yookassa


class UserAgent:
    """
    """
    VERSION_DELIMITER = '/'
    PART_DELIMITER = ' '

    __os = None
    __python = None
    __framework = None
    __cms = None
    __module = None
    __sdk = None

    def __init__(self):
        self.os = self.define_os()
        self.python = self.define_python()
        self.sdk = self.define_sdk()

    def define_os(self):
        simple = self.__define_simple_os()
        if simple.name == 'Windows':
            return Version(simple.name, simple.version)
        elif simple.name == 'Linux':
            smart = self.__define_linux_os()
            return Version(smart.name.capitalize(), smart.version)
        else:
            return Version(simple.name, simple.version)

    @staticmethod
    def define_python():
        info = sys.version_info
        version = str(info.major) + '.' + str(info.minor) + '.' + str(info.micro)
        return Version('Python', version)

    @staticmethod
    def define_sdk():
        version = yookassa.__version__
        return Version('YooKassa.Python', version)

    @property
    def os(self):
        return self.__os

    @os.setter
    def os(self, value):
        self.__os = str(value)

    @property
    def python(self):
        return self.__python

    @python.setter
    def python(self, value):
        self.__python = str(value)

    @property
    def framework(self):
        return self.__framework

    @framework.setter
    def framework(self, value):
        self.__framework = str(value)

    @property
    def cms(self):
        return self.__cms

    @cms.setter
    def cms(self, value):
        self.__cms = str(value)

    @property
    def module(self):
        return self.__module

    @module.setter
    def module(self, value):
        self.__module = str(value)

    @property
    def sdk(self):
        return self.__sdk

    @sdk.setter
    def sdk(self, value):
        self.__sdk = str(value)

    def set_framework(self, name, version):
        self.framework = Version(name, version)
        return self

    def set_cms(self, name, version):
        self.cms = Version(name, version)
        return self

    def set_module(self, name, version):
        self.module = Version(name, version)
        return self

    def get_header_string(self):
        headers = [str(self.os), str(self.python)]
        if self.framework is not None:
            headers.append(str(self.framework))
        if self.cms is not None:
            headers.append(str(self.cms))
        if self.module is not None:
            headers.append(str(self.module))
        headers.append(str(self.sdk))

        return self.PART_DELIMITER.join(headers)

    @staticmethod
    def __define_simple_os():
        return Version(platform.system(), platform.release())

    @staticmethod
    def __define_linux_os():
        dist = distro.linux_distribution(full_distribution_name=False)
        os = Version(dist[0], dist[1])
        return os

    @staticmethod
    def create_version(name, version):
        strip_data = ' ' + UserAgent.PART_DELIMITER + UserAgent.VERSION_DELIMITER
        return name.strip(strip_data).replace(UserAgent.PART_DELIMITER, '.').replace(UserAgent.VERSION_DELIMITER, '.') \
               + UserAgent.VERSION_DELIMITER \
               + version.strip(strip_data).replace(UserAgent.PART_DELIMITER, '.').replace(UserAgent.VERSION_DELIMITER, '.')


class Version:
    __name = None
    __version = None

    def __init__(self, name, version):
        self.name = name
        self.version = version

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = str(value)

    @property
    def version(self):
        return self.__version

    @version.setter
    def version(self, value):
        self.__version = str(value)

    def __str__(self):
        return UserAgent.create_version(self.name, self.version)
