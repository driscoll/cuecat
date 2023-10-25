#!/bin/sh
cut -d\. -f4 $1 | xargs -r -L 1 -I {} python3 cuecat.py {} | isbn_meta openl bibtex  
