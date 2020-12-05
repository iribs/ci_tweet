import re

with open('tweets_full.txt', 'r') as f:
    with open('tweets.txt', 'w') as w:
        for line in f.readlines():
            #delete urls
            line = re.sub(r'(https?:\/\/)(\s)*(www\.)?(\s)*((\w|\s)+\.)*([\w\-\s]+\/)*([\w\-]+)((\?)?[\w\s]*=\s*[\w\%&]*)*', "", line, flags=re.MULTILINE)
            #clear unknown characters like emoji or languages that are not English
            line = re.sub(r"[^\u4e00-\u9fa5^a-z^A-Z^0-9^' '^'\n'^','^'.'^'!'^'?'^':'^'‘'^'\"'^'('^')'^'\-'^'#'^'~'^'；'^'/'^'&'^'['^']'^'|']", "", line, flags=re.MULTILINE)
            if line != '\n':
                if line != " ": #delete blank lines
                    if 'RT' not in line: #delete retweets
                        w.write(line)
f.close()
w.close()

