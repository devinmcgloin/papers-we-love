#! /usr/bin/env python

import os
import re

excluded_dirs = ['.git', "_meetups", ".github"]
paper_title = re.compile("(?<=\[)(?!:scroll:)(?!\d+)(?P<title>[A-Z][\w\s\,\-\?\:\'\(\)]+)(?=\])")

def parse_readme(path):
    print("README: {}".format(path))
    with open(path, 'r') as f:
        readme = f.read()
    for match in re.finditer(paper_title, readme):
        print(re.sub(r'\s+', ' ', match.group('title')))

    return []

def parse_pdf(path):
    print("PDF: {}".format(path))
    return []

def levenshtein(s1, s2):
    if s1 == s2:
        return 0

    len_1 = len(s1)
    len_2 = len(s2)

    if len_1 == 0:
        return len_2
    if len_2 == 0:
        return len_1

    if len_1 > len_2:
        s2, s1 = s1, s2
        len_2, len_1 = len_1, len_2

    d0 = [i for i in range(len_2 + 1)]
    d1 = [i for i in d0]

    for i in range(len_1):
        d1[0] = i + 1
        for j in range(len_2):
            cost = d0[j]

            if s1[i] != s2[j]:
                cost += 1

                x_cost = d1[j] + 1
                if x_cost < cost:
                    cost = x_cost

                y_cost = do[j+ 1] + 1
                if y_cost < cost:
                    cost = y_cost

            d[j+1] = cost

        d0, d1 = d1, d0

    return d0[-1]


if __name__ == "__main__":
    for root, dirs, files in os.walk(".", topdown=True):
        print(root, dirs, files)
        dirs[:] = [dir for dir in dirs if dir not in excluded_dirs]
        listings = []


        if root != ".":
            for path in files:
                if path.endswith(".pdf"):
                    listings += parse_pdf(root + "/" + path)
                elif path.endswith(".md"):
                    listings += parse_readme(root + "/" + path)

        print(listings)
        print()
