#!/bin/sh
set -e
python3 katapult/import_words.py Source/template.js katapult/en_to_jp.json Source/content_script.js
cd Source
7z a ../EnglishToKatakana.zip content_script.js manifest.json
cd ..
mv EnglishToKatakana.zip EnglishToKatakana.crx
