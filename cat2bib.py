#!/usr/bin/python3
#
# cat2bib.py
# 
# This is a tool for cataloging books.
# It will decode the output of a CueCat scanner,
# try to find a valid ISBN number, retrieve 
# metadata, and output a BibTeX entry.
#
# 2003

import cuecat
import fileinput
import isbnlib
import re
import sys
from isbnlib.registry import bibformatters

DEFAULT_SERVICE = "openl"
BACKUP_SERVICE = "goob"

cuecat_pattern = "\.([^\.]+)\.([^\.]+)\.([^\.]+)\."
cuecat_regex = re.compile(cuecat_pattern)
to_bibtex = bibformatters["bibtex"]

if __name__ == "__main__":
    outfile = sys.stdout
    for line in fileinput.input():
        encoded_input = line.strip()
        m = cuecat_regex.search(encoded_input)
        if m:
            if len(m.groups()) == 3:
                    isbn_encoded = m.group(3)
                    print("ISBN (encoded): {}".format(isbn_encoded), file=sys.stderr)
                    isbn_decoded = cuecat.decode(isbn_encoded)
                    isbn = isbnlib.get_canonical_isbn(isbn_decoded)
                    print("ISBN (decoded): {}".format(isbn), file=sys.stderr)
                    try:
                        metadata = isbnlib.meta(isbn, DEFAULT_SERVICE)
                        print("Title: {}".format(metadata.get("Title")), file=sys.stderr)
                        bibtex = to_bibtex(metadata)
                        print(bibtex, file=outfile)
                    except:
                        print("Could not retrieve metadata for ISBN: {}".format(isbn), file=sys.stderr)
        else:
            print("Not valid CueCat output: ".format(encoded_input), file=sys.stderr)