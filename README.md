# samori

A repo for a Digital Edition of Amadu Kurubari's "History of Samori Toure" from Delafosse's 1901 Jula Grammar (see this [blog post](https://www.ankataa.com/blog/2019/2/7/samori-kurubari-delafosse) for more context).

## To Do

- Write scripts to automatically manipulate and change the original OCR text into a critical markdown format
  - ~~Remove the page headers and page numbers and make them into markdown headers~~
  - ~~Extract footnotes from prose~~
  - Clean up and match the semi-automated footnote markers and text.
  
- Figure out auto-replacements for the modern version of the text
  - <yè> for `yɛ`
  - <rh> for intervocalic `g`
  - <ane> for `ani` 'and'
  - <-ru> for plural
  - <kù-tigi> for `kuntigi`
  - <sya> for `siya` 'many'
  - <e-le> for `ele`
  - <m v> for `n f`
  - <fwo> for `fò`
  - <gy> for `j`
  - <sya-> as part of `siyaman` (It can be `sya-ma` or `sya-mà` etc.)
  - <ty> for `c`
  - <ny> for `ɲ`
  - <lô> for `lɔ́n`
  - <kyè> for `cɛ`
  - <-ra> for `???`

## History of OCR clean up

- Started with the `samori-ocr.txt` file.
- Separated the French language introduction from the text proper
- Added markdown page number headers (e.g., `### 149`) using the script `pages.py`
- Removed original document headers and page numbers that were caught in the text
  (semi-manually using search and replace in an editor)
- Partially automated the conversion of Delafosse's footnotes into markdown footnotes using `footnotes.py`

