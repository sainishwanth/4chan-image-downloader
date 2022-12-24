# 4chan-image-downloader

* Recommended Usage with **THREADS ONLY**, this will not auto expand all threads in a board and recursively download them so please only try to input a single thread*

## Requirements
- Python 3+
### Libraries(Third Party)

- BeautifulSoup
- urllib
```sh
pip install bs4 urllib
```

### In-built Libraries
- requests
- os
- random

## Instructions

```sh
python chan.py
```

Follow On-Screen Intructions after running 
- If you do not specify a directory then a sub folder is created (where the repo exists) which is named after the subject of the thread (otherwise a random number if empty)
- Image names are based on The Subject and an incremental counter
- Supported Image Extensions -
  - PNG
  - JPG/JPEG
  - GIF
  - TIFF