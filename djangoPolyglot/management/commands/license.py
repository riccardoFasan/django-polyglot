from polyglot import license
from django.conf import settings


class LicenseError(Exception):
    __key: str

    def __init__(self, key: str) -> None:
        self.__key = key
        super().__init__(
            f"\n\nThe provided license is empty or invalid.\n Your license is: {self.__key}"
        )


class DjangoLicenseManager(license.LicenseManager):
    def get_license(self) -> str:
        key: str = settings.POLYGLOT_DEEPL_LICENSE
        if key is not None and key != "":
            return key
        raise LicenseError(key)

    def set_license(self) -> None:
        pass
