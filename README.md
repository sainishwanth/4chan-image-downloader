# 4chan-image-downloader

- It will only download from threads in a single page (or from a single thread if you choose to do so)
- It Will not Auto Check the Thread for new Images. Any images present in the thread at the time of running this script **ONLY** will be downloaded

## Requirements

- Python 3+

### Libraries(Third Party)

- BeautifulSoup
- urllib3
- prettytable 

```sh
pip install bs4 urllib
```

### In-built Libraries

- requests
- os
- random
- sys

## Instructions
**Run in the following order**
```sh
pip install -r requirements.txt
git clone https://github.com/sainishwanth/4chan-image-downloader
python chan.py
```

Follow On-Screen Intructions:

- If you do not specify a directory then a sub folder is created (where the repo exists) which is named after the subject of the thread 
- If the thread does not have a name then it is named in the following convention
  - "Anonymous + RandomNumber"
- Image names are based on The Subject (Anonymous for non-named threads) and an incremental counter
- Supported Image Extensions -
  - PNG
  - JPG/JPEG
  - GIF
  - TIFF

## Future Updates (TODO)

- Logging to check Progress
- Auto Thread Watcher
- Fully Working GUI
- Changing Pages in a board
- Downloading from multiple boards

#

MIT License

Copyright (c) 2022 Sai Nishwanth

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
