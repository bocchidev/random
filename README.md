# random-down
Ceritanya gabut gitu
# usage 
```python
import re
from Main import Facebook as fb, YouTube as yt, Instagram as ig
url = input("Masukan url")
if re.search("facebook", url):
  #video
  print(fb(url))
elif re.search("youtu(be|.be)", url):
  #audio
  print(yt(url).audio())
  #video
  print(yt(url).video())
elif re.search("instagram", url):
  #hanya ada igtv 
  print(ig.igtv(url))
else print("Unsupported url!")
```
