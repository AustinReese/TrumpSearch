# TrumpSearch

An intentionally vunerable search engine which filters trump tweets by keystrings, metioned users, and hashtags

## Project Summary

This is an incredibly lightweight application which is prone to SQL injection. SQLite database contains additional (mocked) data not used by the application. Compromising the data is easy if the source code and database are viewed, so for more of a challenge I recommend not opening any files.

## Running

```
pip install -r requirements.txt
```
```
python3 app.py
```
