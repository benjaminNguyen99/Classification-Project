import re
import pandas as pd

dt = pd.read_csv('congressional_tweet_training_data.csv')


def URL_neuron():
    url_list = []
    for text in dt['full_text']:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', text)
        for x in url:
            url_list.append(x)
    url_frequency = {}
    for h in url_list:
        if h in url_frequency:
            url_frequency[h] += 1
        else:
            url_frequency[h] = 1
    url_sort = {k: v for k, v in sorted(url_frequency.items(), key=lambda v: v[1])}
    url_l = []

    for x in url_sort.keys():
        url_l.append(x)

    url_l.reverse()
    common_url = url_l[0:200]

    max_url = 0
    lu = []
    url1 = []
    url2 = []
    url3 = []
    url4 = []
    url5 = []
    url6 = []
    url7 = []
    common_url1 = []
    common_url2 = []


    for each in dt['full_text']:
        url = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', each)
        off_url = []
        [off_url.append(x) for x in url if x not in off_url]
        if len(url) >= 1:
            url1.append(url[0])
        else:
            url1.append("None")
        if len(url) >= 2:
            url2.append(url[1])
        else:
            url2.append("None")
        if len(url) >= 3:
            url3.append(url[2])
        else:
            url3.append("None")
        if len(url) >= 4:
            url4.append(url[3])
        else:
            url4.append("None")
        if len(url) >= 5:
            url5.append(url[4])
        else:
            url5.append("None")
        if len(url) >= 6:
            url6.append(url[5])
        else:
            url6.append("None")
        if len(url) >= 7:
            url7.append(url[6])
        else:
            url7.append("None")

        if len(off_url) >= 1:
            if off_url[0] in common_url:
                common_url1.append(common_url.index(off_url[0]))
            else:
                common_url1.append(-1)
        else:
            common_url1.append(-2)
        if len(off_url) >= 2:
            if off_url[1] in common_url:
                common_url2.append(common_url.index(off_url[1]))
            else:
                common_url2.append(-1)
        else:
            common_url2.append(-2)

    return url1, url2, url3, url4, url5, url6, url7, common_url1\
        , common_url2
