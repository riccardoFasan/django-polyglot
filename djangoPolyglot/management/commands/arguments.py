from polyglot import arguments
from . import license


class DjangoArgumentsCollector(arguments.ArgumentsCollector):

    action: str
    source_file: str
    target_lang: str
    output_directory: str
    source_lang: str

    def __init__(
        self,
        action: str,
        source_file: str = "",
        target_lang: str = "",
        output_directory: str = "",
        source_lang: str = "",
    ):
        self.action = action
        self.source_file = source_file
        self.target_lang = target_lang
        self.output_directory = output_directory
        self.source_lang = source_lang
        super().__init__()

    def _collect_arguments(self) -> None:
        self.arguments = arguments.Arguments(
            action=self.action,
            source_file=self.source_file,
            target_lang=self.target_lang,
            output_directory=self.output_directory,
            source_lang=self.source_lang,
            license_manager=license.DjangoLicenseManager(),
        )

    def _validate_arguments(self) -> None:
        pass
