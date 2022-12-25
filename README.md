# 4chan-image-downloader

- It will only download from threads in a single page (or from a single thread if you choose to do so)
- It Will not Auto Check the Thread for new Images. Any images present in the thread at the time of running this script **ONLY** will be downloaded

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
- sys

## Instructions

```sh
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