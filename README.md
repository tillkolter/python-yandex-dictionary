python-yandex-dictionary
=======================

Python module for Yandex.Dictionary API.

Thanks to tyrannosaurus for well done API concept (https://github.com/tyrannosaurus/python-yandex-translate).


Usage
=======================


```python
from yandex_translate import YandexDictionary
dictionary = YandexDictionary('Your API key here.')
print('Languages:', dictionary.langs)
print('Dictionary directions:', dictionary.directions)
print('Word translations:', dictionary.lookup('Привет', 'ru', 'en'))  # or just 'en'
```

This will output:

```
Languages: {'en', 'el', 'ca', 'it', ..}
Translate directions: '['az-ru', 'be-bg', 'be-cs', ..]'
Translate: '{"head":{},"def":[{"text":"hello","pos":"noun","ts":"ˈheˈləʊ","tr":[{"text":"привет","pos":"существительное","syn":[{"text":"приветствие","pos":"существительное","gen":"ср"}],"mean":[{"text":"hi"},{"text":"greeting"}]}]},{"text":"hello","pos":"verb","ts":"ˈheˈləʊ","tr":[{"text":"поздороваться","pos":"глагол","asp":"сов","syn":[{"text":"здороваться","pos":"глагол","asp":"несов"}],"mean":[{"text":"salute"}]}]}]}'
```

License
=======================
WTFPL (Public Domain)
