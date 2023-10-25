# CueCat helper scripts

I (still) have a [CueCat](https://en.wikipedia.org/wiki/CueCat) scanner. I (still) have lots of books. I (still) want to use a cute cat scanner to catalog the books.

Yes, there are numerous barcode scanners for sale that are probably better/cheaper than the CueCat but are they shaped like a cat? No. 

So, here we are. This repo is about making practical use of an impractical device from 23 years ago. Meow.

## cuecat.py

To scan and decode in real-time, run this script without arguments to enter an interactive mode.

```
$ python3 cuecat.py
Scan/Enter> ^[[21;3~.C3nZC3nZC3n2CNf3Chn0DxnY.cGf2.ENr7C3fXDxr2DhfZENzXENnZ.
Serial: 000000005124307601
Type: IB5
Code: 978022675720952900
Scan/Enter> ^[[21;3~.C3nZC3nZC3n2CNf3Chn0DxnY.cGen.ENr7C3bZC3f3E3f0Cq.
Serial: 000000005124307601
Type: IBN
Code: 9780300248272
Scan/Enter>
```

Otherwise, provide one line of output from the CueCat scanner as an argument. If the input is a complete barcode, the output will include Serial number (of your scanner), the Type of code (e.g. IBN for books), and the Code (e.g., 13-digit ISBN number):

```
$ python3 cuecat.py .C3nZC3nZC3n2CNf3Chn0DxnY.cGen.ENr7C3bZC3f3E3f0Cq.
Serial: 000000005124307601
Type: IBN
Code: 9780300248272
```

Alternatively, you can trim out just the code and the script will return the decoded string:

```
$ python3 cuecat.py ENr7C3bZC3f3E3f0Cq
9780300248272
```

With the help of [isbntools](https://github.com/xlcnd/isbntools), you can retrieve book metadata in one line:

```
$ python3 cuecat.py ENr7C3bZC3f3E3f0Cq | isbn_meta openl bibtex
@book{9780300248272,
     title = {Death Glitch - How Techno-Solutionism Fails Us in This Life and Beyond},
    author = {Tamara Kneese},
      isbn = {9780300248272},
      year = {2023},
 publisher = {Yale University Press}
}
```

## cat2bib.sh

My workflow involves scanning a bunch of barcodes into a plaintext file. Each line of the file contains the raw output from the CueCat scanner. Next, I decode in a batch and save the metadata in a BibTeX file for easy import into Zotero, e.g.,

```
$ ./cat2bib.sh cuecat_output.txt > cuecat.bib
```

## Attribution

The CueCat decoder script is based on code that has been floating around the web for a long time without attribution. (NB: I believe the original author may be @inklesspen!). For this version, I updated the code for Python3 compatibility.

## Further reading

For more technical information about the CueCat scanner:
- http://www.accipiter.org/projects/cat.php
- http://www.beau.lib.la.us/~jmorris/linux/cuecat/
- https://linas.org/banned/cuecat/cc.index.html
- https://www.instructables.com/Arduino-and-CueCat-barcode-scanner/

For more background on the meaning of the ISBN barcodes:
- "[ISBN Barcodes: Breakdown of a Bookland EAN Barcode](https://www.isbn-us.com/isbn-barcodes-breakdown-bookland-ean-barcode/)", Publisher Services, November 30, 2015.

For an historical glimpse of late-dotcom-era DIY barcode-scanning:
- Zarf, "[The Book Scanning Project](https://www.eblong.com/zarf/bookscan/index.html)", E BLONG, October 2, 2000

And for a present-day reflection on the CueCat campaign:
- Cory Doctorow, "[It was all downhill after the Cuecat](https://pluralistic.net/2022/10/20/benevolent-dictators/#felony-contempt-of-business-model)," Pluralistic, October 20, 2022.