#!/bin/sh
set -e
python3 katapult/import_words.py Source/template.js katapult/en_to_jp.json Source/content_script.js
node node_modules/crx/src/cli.js pack Source -o EnglishToKatakana.crx
