import os
from django.core.management.base import BaseCommand, CommandParser
from django.core import management
from django.conf import settings

from polyglot import polyglot, arguments
from . import arguments as django_arguments


class Command(BaseCommand):
    help = "A custom command to easily make your translations using the DeepL API."

    __languages: list[str]
    __actions: list[str] = [
        "translate",
        "print_supported_languages",
        "print_usage_info",
    ]

    def __init__(self):
        super().__init__()
        self.__languages = [seq[0] for seq in settings.LANGUAGES]

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "action",
            type=str,
            help="The command that will be exectued. The following options are for the translate command.",
            choices=self.__actions,
        )

    def handle(self, *args, **options) -> None:
        method: str = options["action"]
        getattr(self, method)()

    def print_usage_info(self) -> None:
        collector: arguments.ArgumentsCollector = (
            django_arguments.DjangoArgumentsCollector(action="print_usage_info")
        )
        options: arguments.Arguments = collector.arguments
        polyglot.Polyglot(options).execute_command()

    def print_supported_languages(self) -> None:
        collector: arguments.ArgumentsCollector = (
            django_arguments.DjangoArgumentsCollector(
                action="print_supported_languages"
            )
        )
        options: arguments.Arguments = collector.arguments
        polyglot.Polyglot(options).execute_command()

    def translate(self) -> None:
        self.__make_messages()
        self.__run_polyglot()
        self.__compile_messages()

    def __make_messages(self) -> None:
        print("\n========== makemessages ==========")
        management.call_command(
            "makemessages", locale=self.__languages, domain="django"
        )

    def __run_polyglot(self) -> None:
        print("\n========== polyglot ==========")

        source_lang: str = settings.LANGUAGE_CODE
        target_langs: list[str] = [
            lang[0] for lang in settings.LANGUAGES if lang[0] != source_lang
        ]

        for locale in settings.LOCALE_PATHS:
            source_file: str = f"{locale}/{source_lang}/LC_MESSAGES/django.po"
            print(f'Tranlating locale: "{source_file}"...\n')
            for lang in target_langs:
                output_dir: str = f"{locale}/{lang}/LC_MESSAGES/"
                collector: arguments.ArgumentsCollector = (
                    django_arguments.DjangoArgumentsCollector(
                        action="translate",
                        source_file=source_file,
                        target_lang=lang.upper(),
                        output_directory=output_dir,
                        source_lang=source_lang.upper(),
                    )
                )
                options: arguments.Arguments = collector.arguments
                polyglot.Polyglot(options).execute_command()

                # Polyglot names output files like this: "{lang_code}.po" so we have to rename in "django.po"
                os.rename(f"{output_dir}/{lang}.po", f"{output_dir}/django.po")
                os.rename(f"{output_dir}/{lang}.mo", f"{output_dir}/django.mo")

    def __compile_messages(self) -> None:
        print("\n========== compilemessages ==========")
        management.call_command("compilemessages", locale=self.__languages)
