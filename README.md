# Django-Polyglot: DeepL integration for Django

Django-Polyglot is an integration of [**Polyglot**](https://github.com/riccardoFasan/polyglot) for [**Django**](https://www.djangoproject.com/) Web Framework.

It provides a CLI command that, using the [**DeepL API**](https://www.deepl.com/it/docs-api/), automates the translation of your static texts.

## Installation

Django Polyglot can be easily installed by running:

```shell
pip install django-polyglot-translator
```

Make sure you've configured Django [internationalization](https://docs.djangoproject.com/en/4.0/topics/i18n/).

Now you have to register Django-Polyglot in your settings like this:

```python
INSTALLED_APPS = [
    ...
    'djangoPolyglot'
]
```

Finally, you need to store your DeepL API key in your settings.

```python
POLYGLOT_DEEPL_LICENSE = {
    'key' : 'your_key',
    'version' : 'free' # Write "pro" if you're using the pro version.
}
```

## Usage

### Translate

Django-Polyglot will run for you the Django "makemessages" command, preparing the .po files with the text to be translated. Then Polyglot will use the DeepL APIs to translate this files. Finally the Django "compilemessages" command will be ran and your static translations will be ready.

```shell
./manage.py django-polyglot translate
```

> ⚠️To use the translate command you need to set **LANGUAGE_CODE**, **LANGUAGES** and **LOCALE_PATHS** in your settings, according the Django documentation.

### Usage info

It returns DeepL usage info related to your API key, run with:

```shell
./manage.py django-polyglot print_usage_info
```

### Supported languages

It returns the list of languages currently supported by DeepL, run with:

```shell
./manage.py django-polyglot print_supported_languages
```

## Dependencies

The only dependency is [**Polyglot**](https://github.com/riccardoFasan/polyglot).

## License

Django-Polyglot is provided under the MIT license.
