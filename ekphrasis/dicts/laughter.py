import re

# todo:catch repeating parenthesis
laughter = {
    'hah': '<laugh>',
    'haha': '<laugh>',
    'hahah': '<laugh>',
    'hahaha': '<laugh>',
    'hahahah': '<laugh>',
    'hahahaha': '<laugh>',
    'hahahahah': '<laugh>',
    'hahahahaha': '<laugh>',
    'hahahahahah': '<laugh>',
    'hahahahahaha': '<laugh>',
    'ahah': '<laugh>',
    'ahaha': '<laugh>',
    'ahahah': '<laugh>',
    'ahahaha': '<laugh>',
    'ahahahah': '<laugh>',
    'ahahahaha': '<laugh>',
    'ahahahahah': '<laugh>',
    'ahahahahaha': '<laugh>',
}

# todo: clear this mess

haha = "haha"
hehe = "hehe"
hoho = "hoho"

pattern = re.compile("^[:=\*\-\(\)\[\]x0oO\#\<\>8\\.\'|\{\}\@]+$")
mirror_emoticons = {}
for exp, tag in emoticons.items():
    if pattern.match(exp) \
            and any(ext in exp for ext in [";", ":", "="]) \
            and not any(ext in exp for ext in ["L", "D", "p", "P", "3"]):
        mirror = exp[::-1]

        if "{" in mirror:
            mirror = mirror.replace("{", "}")
        elif "}" in mirror:
            mirror = mirror.replace("}", "{")

        if "(" in mirror:
            mirror = mirror.replace("(", ")")
        elif ")" in mirror:
            mirror = mirror.replace(")", "(")

        if "<" in mirror:
            mirror = mirror.replace("<", ">")
        elif ">" in mirror:
            mirror = mirror.replace(">", "<")

        if "[" in mirror:
            mirror = mirror.replace("[", "]")
        elif "]" in mirror:
            mirror = mirror.replace("]", "[")

        if "\\" in mirror:
            mirror = mirror.replace("\\", "/")
        elif "/" in mirror:
            mirror = mirror.replace("/", "\\")

        # print(exp + "\t\t" + mirror)
        mirror_emoticons[mirror] = tag
emoticons.update(mirror_emoticons)

emoticon_groups = {
    "positive": {'<highfive>', '<laugh>', '<heart>', '<happy>'},
    "negative": {'<annoyed>', '<sad>', }
}


def print_positive(sentiment):
    for e, tag in emoticons.items():
        if tag in emoticon_groups[sentiment]:
            print(e)

# print_positive("negative")
# print(" ".join(list(emoticons.keys())))
# [print(e) for e in list(emoticons.keys())]

