import sys
import json
import re

def gen_regex(jp_to_en):
    regexlist = [re.escape(a[1]) for a in jp_to_en]
    regexlist.sort()
    regexlist.sort(key=lambda a: -len(a))
    return "|".join(regexlist)

def gen_map(jp_to_en):
    m = {}
    for i in jp_to_en:
        m[i[1].lower()] = i[0]
    return json.dumps(m, ensure_ascii=False, sort_keys=True, indent=2)

def clean(a):
    if "/" in a[1]:
        return (a[0], a[1].split("/")[0])
    return a

MIN_LEN = 3

def filter_none(jp_to_en):
    return [clean(a) for a in jp_to_en if a is not None and len(a[1]) > MIN_LEN]

def main():
    if len(sys.argv) != 4:
        print("usage: import_words.py template.js jp_to_en.json content_script.js")
    with open(sys.argv[1], "r") as infile:
        template = infile.read()
    with open(sys.argv[2], "r") as infile:
        jp_to_en = filter_none(json.load(infile))
    output = template.replace("THEREGEX", gen_regex(jp_to_en)). \
        replace("THEMAP", gen_map(jp_to_en))
    with open(sys.argv[3], "w") as outfile:
        outfile.write(output)

if __name__ == "__main__":
    main()