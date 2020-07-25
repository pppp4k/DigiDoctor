# DigiDoctor
## by Pratyush Kore and Saathvik Somujayabalan

DigiDoctor is the backbone for a software which uses machine learning to diagnose patients based on images of their skin (rashes, pimples, cuts, pustules, etc.)

## Contents

The files with suffix "ignore" are old, failed, or obsolete attemps at communicating with the machine learning API.
There are 2 files you will find useful: 

### RUN_THIS.py

RUN_THIS.py is the first of these files. It is reccommended that you run this file through the command line. It takes one argument, which is the file path for an image. An example of running this might be: 

```bash
python3 RUN_THIS.py 'testacne.jpg'
```

To change the way the program takes arguments, you will need to edit line 14:

```python
fpath=sys.argv[1]
```

You can put the whole code inside a function which takes a string as an argument or parameter (we'll call this string "str" for the example here) and then set fpath to that string:

```python
def new(str):
  fpath = str
```
### index.html

index.html is the backbone for a potential website that would run this software. The program is self-explanatory, and you can use and edit the files in the images and assets folders, as well as the elements.html file.

## Usage and Contributions

You are welcome to download, test, and develop this software. Pull requests are welcome, but please specify what changes you would like to make if you do want to pull. Please make sure to update tests as appropriate.

## Resources

Multiple libraries were used, all of which come with Python by default.
Libraries used: requests, json, base64, sys
Ximilar and urllib libraries also used

```python
import requests
import json
import base64
import sys
```

## Credits
Pratyush Kore and Saathvik Somujayabalan
Website template from TEMPLATED (templated.co)
Model training and API from ximilar.com (vize.ai)
Images from Unsplash
