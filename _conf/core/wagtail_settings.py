# -*- coding: utf-8 -*-

WAGTAIL_SITE_NAME = 'opirogova'
WAGTAIL_ALLOW_UNICODE_SLUGS = False

WAGTAIL_DATE_FORMAT = '%d.%m.%Y'
WAGTAIL_DATETIME_FORMAT = '%d.%m.%Y %H:%M'


WAGTAILIMAGES_MAX_UPLOAD_SIZE = 20 * 1024 * 1024


WAGTAIL_ENABLE_UPDATE_CHECK = False

IMAGE_FORMATS = {
    'square_240': 'fill-240x240',
    'square_120': 'fill-120x120',
    'image': 'width-1000',
}


WAGTAILSEARCH_BACKENDS = {
    'default': {
        # 'BACKEND': 'wagtail.search.backends.elasticsearch5',
        'BACKEND': 'wagtail.search.backends.db',
        'INDEX': 'opirogova',
        'TIMEOUT': 60*15,
        'OPTIONS': {'from': 0, 'size': 100},
        'INDEX_SETTINGS': {
            'settings': {
                'index': {
                    'number_of_shards': 1,
                    'number_of_replicas': 0,
                    'analysis': {
                        'char_filter': {
                            'ru': {
                                'type': 'mapping',
                                'mappings': [
                                    'Ё=>Е',
                                    'ё=>е'
                                ]
                            }
                        },
                        'analyzer': {
                            'default': {
                                'alias': [
                                    'index_ru'
                                ],
                                'type': 'custom',
                                'tokenizer': 'nGram',
                                'filter': [
                                    'stopwords_ru',
                                    'stop',
                                    'custom_word_delimiter',
                                    'lowercase',
                                    'russian_morphology',
                                    'english_morphology'
                                ],
                                'char_filter': [
                                    'ru'
                                ]
                            },
                            'default_search': {
                                'alias': [
                                    'search_ru'
                                ],
                                'type': 'custom',
                                'tokenizer': 'standard',
                                'filter': [
                                    'stopwords_ru',
                                    'stop',
                                    'custom_word_delimiter',
                                    'lowercase',
                                    'russian_morphology',
                                    'english_morphology'
                                ],
                                'char_filter': [
                                    'ru'
                                ]
                            }
                        },
                        'tokenizer': {
                            'nGram': {
                                'type': 'nGram',
                                'min_gram': 2,
                                'max_gram': 20
                            }
                        },
                        'filter': {
                            'stopwords_ru': {
                                'type': 'stop',
                                'stopwords': [
                                    'а', 'без', 'более', 'бы', 'был', 'была', 'были', 'было', 'быть', 'в', 'вам', 'вас', 'весь', 'во', 'вот',
                                    'все', 'всего', 'всех', 'вы', 'где', 'да', 'даже', 'для', 'до', 'его', 'ее', 'если', 'есть', 'еще', 'же',
                                    'за', 'здесь', 'и', 'из', 'или', 'им', 'их', 'к', 'как', 'ко', 'когда', 'кто', 'ли', 'либо', 'мне', 'может',
                                    'мы', 'на', 'надо', 'наш', 'не', 'него', 'нее', 'нет', 'ни', 'них', 'но', 'ну', 'о', 'об', 'однако', 'он', 'она', 'они', 'оно',
                                    'от', 'очень', 'по', 'под', 'при', 'с', 'со', 'так', 'также', 'такой', 'там', 'те', 'тем', 'то', 'того', 'тоже', 'той', 'только',
                                    'том', 'ты', 'у', 'уже', 'хотя', 'чего', 'чей', 'чем', 'что', 'чтобы', 'чье', 'чья', 'эта', 'эти', 'это', 'я'
                                ],
                                'ignore_case': True
                            },
                            'custom_word_delimiter': {
                                'type': 'word_delimiter',
                                'generate_word_parts': True,
                                'generate_number_parts': True,
                                'catenate_words': True,
                                'catenate_numbers': False,
                                'catenate_all': True,
                                'split_on_case_change': True,
                                'preserve_original': True,
                                'split_on_numerics': False
                            }
                        }
                    }
                }
            }
        }

    },
}
