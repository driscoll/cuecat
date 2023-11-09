#!/usr/bin/python3
#
# isbn2bib.py
# 
# This is a tool for cataloging books.
# Type in an ISBN number, retrieve 
# metadata, and output a BibTeX entry.
#
# 2003

import fileinput
import isbnlib
import sys
from isbnlib.registry import bibformatters

DEFAULT_SERVICE = "openl"
BACKUP_SERVICE = "goob"

to_bibtex = bibformatters["bibtex"]

if __name__ == "__main__":
    outfile = sys.stdout
    for line in fileinput.input():
        isbn_transcribed = line.strip()
        isbn = isbnlib.get_canonical_isbn(isbn_transcribed)
        print("ISBN (canonical): {}".format(isbn), file=sys.stderr)
        try:
            metadata = isbnlib.meta(isbn, DEFAULT_SERVICE)
            print("Title: {}".format(metadata.get("Title")), file=sys.stderr)
            bibtex = to_bibtex(metadata)
            print(bibtex, file=outfile)
        except:
            print("Could not retrieve metadata for ISBN: {}".format(isbn), file=sys.stderr)
