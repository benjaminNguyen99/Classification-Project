

import pandas as pd

dt = pd.read_csv('congressional_tweet_training_data.csv')




hashtag_list = []
number_of_hashtag = []
for hashtags in dt['hashtags']:
    count = 0

    each_has = hashtags.split()
    for x in each_has:
        count+=1
        hashtag_list.append(x)
    number_of_hashtag.append(count)

frequency = {}
for h in hashtag_list:
    if h in frequency:
        frequency[h] += 1
    else:
        frequency[h] = 1
sort = {k: v for k, v in sorted(frequency.items(), key=lambda v: v[1])}
listt = []
for x in sort.keys():
    listt.append(x)
listt.reverse()
common = listt[0:500] #list of 500 most common hashtag


def hashtags_neuron():
    hashtag_1 = []
    hashtag_2 = []
    hashtag_3 = []
    hashtag_4 = []
    hashtag_5 = []
    hashtag_6 = []
    hashtag_7 = []
    hashtag_8 = []
    hashtag_9 = []
    hashtag_10 = []
    hashtag_11 = []
    hashtag_12 = []
    hashtag_13 = []
    hashtag_14 = []
    hashtag_15 = []
    hashtag_16 = []
    hashtag_17 = []
    hashtag_18 = []
    common_hashtag1 = []
    common_hashtag2 = []
    common_hashtag3 = []
    common_hashtag4 = []
    common_hashtag5 = []
    common_hashtag6 = []
    common_hashtag7 = []
    common_hashtag8 = []
    common_hashtag9 = []
    common_hashtag = []
    for each in dt['hashtags']:
        has_list = each.split()
        uni_list = []
        [uni_list.append(x) for x in has_list if x not in uni_list]
        count = 0

        for i in has_list:
            if i in common:
                count += 1
        common_hashtag.append(count)


        hashtag_1.append(uni_list[0])
        if len(has_list) >= 2:

            hashtag_2.append(has_list[1])
        else:
            hashtag_2.append("None")
        if len(has_list) >= 3:

            hashtag_3.append(has_list[2])
        else:
            hashtag_3.append("None")
        if len(has_list) >= 4:

            hashtag_4.append(has_list[3])
        else:
            hashtag_4.append("None")
        if len(has_list) >= 5:

            hashtag_5.append(has_list[4])
        else:
            hashtag_5.append("None")
        if len(has_list) >= 6:

            hashtag_6.append(has_list[5])
        else:
            hashtag_6.append("None")
        if len(has_list) >= 7:

            hashtag_7.append(has_list[6])
        else:
            hashtag_7.append("None")
        if len(has_list) >= 8:

            hashtag_8.append(has_list[7])
        else:
            hashtag_8.append("None")
        if len(has_list) >= 9:

            hashtag_9.append(has_list[8])
        else:
            hashtag_9.append("None")
        if len(has_list) >= 10:

            hashtag_10.append(has_list[9])
        else:
            hashtag_10.append("None")
        if len(has_list) >= 11:

            hashtag_11.append(has_list[10])
        else:
            hashtag_11.append("None")
        if len(has_list) >= 12:

            hashtag_12.append(has_list[11])
        else:
            hashtag_12.append("None")
        if len(has_list) >= 13:

            hashtag_13.append(has_list[12])
        else:
            hashtag_13.append("None")
        if len(has_list) >= 14:

            hashtag_14.append(has_list[13])
        else:
            hashtag_14.append("None")
        if len(has_list) >= 15:

            hashtag_15.append(has_list[14])
        else:
            hashtag_15.append("None")
        if len(has_list) >= 16:

            hashtag_16.append(has_list[15])
        else:
            hashtag_16.append("None")
        if len(has_list) >= 17:

            hashtag_17.append(has_list[16])
        else:
            hashtag_17.append("None")
        if len(has_list) >= 18:

            hashtag_18.append(has_list[17])
        else:
            hashtag_18.append("None")

        if len(uni_list) >= 1:
            if uni_list[0] in common:
                common_hashtag1.append(common.index(uni_list[0]))
            else:
                common_hashtag1.append(-1)
        else:
            common_hashtag1.append(-2)
        if len(uni_list) >= 2:
            if uni_list[1] in common:
                common_hashtag2.append(common.index(uni_list[1]))
            else:
                common_hashtag2.append(-1)
        else:
            common_hashtag2.append(-2)
        if len(uni_list) >= 3:
            if uni_list[2] in common:
                common_hashtag3.append(common.index(uni_list[2]))
            else:
                common_hashtag3.append(-1)
        else:
            common_hashtag3.append(-2)
        if len(uni_list) >= 4:
            if uni_list[3] in common:
                common_hashtag4.append(common.index(uni_list[3]))
            else:
                common_hashtag4.append(-1)
        else:
            common_hashtag4.append(-2)
        if len(uni_list) >= 5:
            if uni_list[4] in common:
                common_hashtag5.append(common.index(uni_list[4]))
            else:
                common_hashtag5.append(-1)
        else:
            common_hashtag5.append(-2)
        if len(uni_list) >= 6:
            if uni_list[5] in common:
                common_hashtag6.append(common.index(uni_list[5]))
            else:
                common_hashtag6.append(-1)
        else:
            common_hashtag6.append(-2)
        if len(uni_list) >= 7:
            if uni_list[6] in common:
                common_hashtag7.append(common.index(uni_list[6]))
            else:
                common_hashtag7.append(-1)
        else:
            common_hashtag7.append(-2)
        if len(uni_list) >= 8:
            if uni_list[7] in common:
                common_hashtag8.append(common.index(uni_list[7]))
            else:
                common_hashtag8.append(-1)
        else:
            common_hashtag8.append(-2)
        if len(uni_list) >= 9:
            if uni_list[8] in common:
                common_hashtag9.append(common.index(uni_list[8]))
            else:
                common_hashtag9.append(-1)
        else:
            common_hashtag9.append(-2)
    return hashtag_1, hashtag_2, hashtag_3, hashtag_4, hashtag_5, hashtag_6, hashtag_7\
        ,hashtag_8, hashtag_9, hashtag_10, hashtag_11, hashtag_12, hashtag_13, hashtag_14\
        ,hashtag_15, hashtag_16, hashtag_17, hashtag_18, common_hashtag1, common_hashtag2\
        , common_hashtag3, common_hashtag4, common_hashtag5, common_hashtag6, common_hashtag7\
        , common_hashtag8, common_hashtag9,common_hashtag