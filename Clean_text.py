import re
import pandas as pd

dt = pd.read_csv('congressional_tweet_training_data.csv')
dt['year'].fillna(int(dt['year'].mean()), inplace = True)


is_using_URL = []
plain_text = []
num_mention =[]
list_amp=[]
nohashtag_text =[]
nomention_text =[]
nourl_text =[]
nodecode_text = []
full_text = []
RT_list = []
num_hashtag = []
full_word = []
without_hashtag_word = []
without_mention_word = []
without_url_word = []
plain_word = []

def text_features():
    for x in dt['full_text']:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', x)
        is_using_URL.append(len(url))

        amp = re.findall("&amp", x)
        list_amp.append(len(amp))

        mentions = re.findall("@([a-zA-Z0-9_]{1,50})", x)
        num_mention.append(len(mentions))

        full_text.append(len(x))

    for x in dt['full_text']:
        x = x.split()
        count= 0
        for i in x:
            if i == 'b"RT' or i == 'RT':
                count+=1
        if count != 0:
            RT_list.append(1)
        else:
            RT_list.append(0)

    for x in dt['full_text']:
        x = re.sub("#[A-Za-z0-9_]+", "", x)
        nohashtag_text.append(len(x))
        x = x.split()
        without_hashtag_word.append(len(x))

    for x in dt['full_text']:
        x = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "", x)
        nourl_text.append(len(x))
        x = x.split()
        without_url_word.append(len(x))


    for x in dt['full_text']:
        x = re.sub("@([a-zA-Z0-9_]{1,50})", "", x)
        nomention_text.append(len(x))
        x = x.split()
        without_mention_word.append(len(x))

    for x in dt['full_text']:
        x = re.sub("#[A-Za-z0-9_]+", "", x)
        x = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', "", x)
        x = re.sub("@([a-zA-Z0-9_]{1,50})", "", x)
        x = re.sub(r'[^\x00-\x7f]+', '', x)
        plain_text.append(len(x))
        x = x.split()
        plain_word.append(len(x))

    for x in dt['full_text']:
        x = re.sub(r'[^\x00-\x7f]+',r'', x)
        nodecode_text.append(len(x))

    for x in dt['full_text']:
        x = x.split()
        full_word.append(len(x))



    for x in dt['hashtags']:
        each = x.split()
        num_hashtag.append(len(each))

    year = []
    for each in dt['year']:
        year.append(str(each))

    parti = []
    for each in dt['party_id']:
        if each == 'D':
            parti.append(1)
        elif each == 'R':
            parti.append(0)

    return is_using_URL, num_mention, list_amp, num_hashtag, plain_text, year, parti, nohashtag_text\
        ,nomention_text, nourl_text, nodecode_text, full_text, RT_list, full_word\
        ,without_mention_word, without_hashtag_word, without_url_word, plain_word