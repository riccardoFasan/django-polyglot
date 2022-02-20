from polyglot import license
from django.conf import settings


class LicenseError(Exception):
    license: dict[str, str]

    def __init__(self, license: dict[str, str]):
        self.license = license
        super().__init__(
            f"\n\nThe provided license is empty or invalid.\n Your license is: {self.license}"
        )


class DjangoLicenseManager(license.LicenseManager):
    def get_license(self) -> license.License:
        deepl_license: dict[str, str] = settings.DEEPL_LICENSE
        try:
            key: str = deepl_license["key"]
            version: license.LicenseVersion = license.LicenseVersion(
                deepl_license["version"]
            )
            return license.License(key=key, version=version)
        except:
            raise LicenseError(license=deepl_license)

    def set_license(self) -> None:
        pass
