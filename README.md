# e2 repo




## Ad Poc

A tiny flask app to slightly hack the Pocket API.

* N.B. there's also a manually-executed even ad-hocker selenium WebDriver/Safari script, executed with python src/automated.py, which looks for POCKET_USERNAME and POCKET_PASSWORD in os.environ (so run with `$export POCKET_USERNAME=x && export POCKET_PASSWORD=y && python src/automated.py`), then, even more specifically, goes through the links in /Users/PeterParkinson/Downloads/ril_export-3.html (!) with bs4/beautifulsoup and adds each one to pocket via direct manipulation. Necessary since Pocket seems to have blocked my access to their API!.



### Run like this:

1. Execute: 
```
cd adpoc
pip install -r requirements.txt
cd src
python app.py &
open http://127.0.0.1:5000/

```

2. Authorize "pockmarked" app in Pocket.

3. Into the form in the second of the two authentication links, paste in list of links such as:
 
-        https://app.getpocket.com/read/2063169981
-        https://app.getpocket.com/read/2165130375
-        https://app.getpocket.com/read/1679570702
-        https://app.getpocket.com/read/2131397900
-        https://app.getpocket.com/read/2074693879
-        https://app.getpocket.com/read/1588834267
-        https://app.getpocket.com/read/1623704058
-        https://app.getpocket.com/read/2198137324

4. Submit. The result ought to be a list of original links.

### Still to do:

1. Handle the meta data (which is fairly abundant, including e.g., excerpt, derived title, "top image").







## Transpose, qv
