# bottr-template

This repository shall give a rough template to start with writing a 
reddit bot using [bottr](https://botts.readthedocs.io).

## Setup

1) First run the `setup.sh` script with a name of the new bot [a-zA-Z_]:
```bash
$ ./setup.sh my_fancy_bot
```

2) Replace the content of `subreddits.txt` and `blacklist.txt` 
   - `subreddits.txt` with subs you want to monitor
   - `blacklist.txt` with subs you want to blacklist
 
3) Fill out the credentials in `creds.props`. See also [bottr: Bot Account Setup](http://bottr.readthedocs.io/setup.html).
