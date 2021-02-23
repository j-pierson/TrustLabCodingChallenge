from warcio.archiveiterator import ArchiveIterator
import re
import requests
import sys

keywords = [re.compile("pandemic"), re.compile("economy"), re.compile("business"),
            re.compile("coronavirus"), re.compile("covid"), re.compile("jobs")]

good_urls = []

entries = 0
hits = 0
word_matches = 0

# data.txt contains the file_name for 15 sections in the may/june, july, and august data sets

data = open('data.txt', 'r')
lines = data.readlines()

for line in lines:

    file_name = line.rstrip("\n")

    stream = requests.get(file_name, stream=True).raw

    for record in ArchiveIterator(stream):

        url = record.rec_headers.get_header("WARC-TARGET-URI")
        if record.rec_type == "warcinfo":
            continue
        if not ".com/" in url:
            continue

        entries = entries + 1

        contents = (record.content_stream().read().decode("utf-8", "replace"))

        for word in keywords :
            m = word.search(contents)
            if m:
                word_matches = word_matches + 1
                hits = hits + 1
                m = word.search(contents, m.end())

            while m:
                m = word.search(contents, m.end())
                hits = hits + 1

        if word_matches >= 4 and hits >= 10 :
            good_urls.append(url)

        word_matches = 0
        hits = 0

for url in good_urls:
    print(url)

print(
    str(len(good_urls))
    + " urls found from "
    + str(entries)
    + " total urls taken from May through August of 2020."
)
