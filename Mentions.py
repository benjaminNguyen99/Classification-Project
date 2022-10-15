import re
import pandas as pd

dt = pd.read_csv('congressional_tweet_training_data.csv')
list_of_mention = []
for text in dt['full_text']:
    mentions = re.findall("@([a-zA-Z0-9_]{1,50})", text)
    for x in mentions:
        list_of_mention.append(x)
mention_frequency = {}
for h in list_of_mention:
    if h in mention_frequency:
        mention_frequency[h] += 1
    else:
        mention_frequency[h] = 1
ment_sort = {k: v for k, v in sorted(mention_frequency.items(), key=lambda v: v[1])}
men_l = []
for x in ment_sort.keys():
    men_l.append(x)
men_l.reverse()
common_mention = men_l[0:500] #list of 50 most common mention

# max_mention = 0
# ll = []
# for each in dt['full_text']:
#     mentions = re.findall("@([a-zA-Z0-9_]{1,50})", each)
#     off_men = []
#     [off_men.append(x) for x in mentions if x not in off_men]
#     count = 0
#     la = []
#     for x in off_men:
#         if x in common_mention:
#             la.append(x)
#     if len(la) >= max_mention:
#         max_mention = len(la)
#         ll = la
# print(max_mention)
# print(ll)

def mention_neuron():
    mention_1 = []
    mention_2 = []
    mention_3 = []
    mention_4 = []
    mention_5 = []
    mention_6 = []
    mention_7 = []
    mention_8 = []
    mention_9 = []
    mention_10 = []
    mention_11 = []
    mention_12 = []
    mention_13 = []
    mention_14 = []
    mention_15 = []
    mention_16 = []
    mention_17 = []
    mention_18 = []
    mention_19 = []
    mention_20 = []
    mention_21 = []
    mention_22 = []
    mention_23 = []
    mention_24 = []
    mention_25 = []
    mention_26 = []
    mention_27 = []
    mention_28 = []
    mention_29 = []
    mention_30 = []
    mention_31 = []
    mention_32 = []
    mention_33 = []
    mention_34 = []
    mention_35 = []
    mention_36 = []
    mention_37 = []
    mention_38 = []
    mention_39 = []
    mention_40 = []
    mention_41 = []
    mention_42 = []
    mention_43 = []
    mention_44 = []

    common_mention1 = []
    common_mention2 = []
    common_mention3 = []
    common_mention4 = []
    common_mention5 = []
    common_mention6 = []
    common_mention7 = []
    common_mention8 = []
    common_mention9 = []
    common_mention10 = []
    common_mention11 = []
    common_mention12 = []
    common_mention13 = []

    for each_text in dt['full_text']:
        mentions = re.findall("@([a-zA-Z0-9_]{1,50})", each_text)
        off_men = []
        [off_men.append(x) for x in mentions if x not in off_men]
        if len(mentions) >= 1:
            mention_1.append(mentions[0])
        else:
            mention_1.append("None")
        if len(mentions) >= 2:
            mention_2.append(mentions[1])
        else:
            mention_2.append("None")
        if len(mentions) >= 3:
            mention_3.append(mentions[2])
        else:
            mention_3.append("None")
        if len(mentions) >= 4:
            mention_4.append(mentions[3])
        else:
            mention_4.append("None")
        if len(mentions) >= 5:
            mention_5.append(mentions[4])
        else:
            mention_5.append("None")
        if len(mentions) >= 6:
            mention_6.append(mentions[5])
        else:
            mention_6.append("None")
        if len(mentions) >= 7:
            mention_7.append(mentions[6])
        else:
            mention_7.append("None")
        if len(mentions) >= 8:
            mention_8.append(mentions[7])
        else:
            mention_8.append("None")
        if len(mentions) >= 9:
            mention_9.append(mentions[8])
        else:
            mention_9.append("None")
        if len(mentions) >= 10:
            mention_10.append(mentions[9])
        else:
            mention_10.append("None")
        if len(mentions) >= 11:
            mention_11.append(mentions[10])
        else:
            mention_11.append("None")
        if len(mentions) >= 12:
            mention_12.append(mentions[11])
        else:
            mention_12.append("None")
        if len(mentions) >= 13:
            mention_13.append(mentions[12])
        else:
            mention_13.append("None")
        if len(mentions) >= 14:
            mention_14.append(mentions[13])
        else:
            mention_14.append("None")
        if len(mentions) >= 15:
            mention_15.append(mentions[14])
        else:
            mention_15.append("None")
        if len(mentions) >= 16:
            mention_16.append(mentions[15])
        else:
            mention_16.append("None")
        if len(mentions) >= 17:
            mention_17.append(mentions[16])
        else:
            mention_17.append("None")
        if len(mentions) >= 18:
            mention_18.append(mentions[17])
        else:
            mention_18.append("None")
        if len(mentions) >= 19:
            mention_19.append(mentions[18])
        else:
            mention_19.append("None")
        if len(mentions) >= 20:
            mention_20.append(mentions[19])
        else:
            mention_20.append("None")
        if len(mentions) >= 21:
            mention_21.append(mentions[20])
        else:
            mention_21.append("None")
        if len(mentions) >= 22:
            mention_22.append(mentions[21])
        else:
            mention_22.append("None")
        if len(mentions) >= 23:
            mention_23.append(mentions[22])
        else:
            mention_23.append("None")
        if len(mentions) >= 24:
            mention_24.append(mentions[23])
        else:
            mention_24.append("None")
        if len(mentions) >= 25:
            mention_25.append(mentions[24])
        else:
            mention_25.append("None")
        if len(mentions) >= 26:
            mention_26.append(mentions[25])
        else:
            mention_26.append("None")
        if len(mentions) >= 27:
            mention_27.append(mentions[26])
        else:
            mention_27.append("None")
        if len(mentions) >= 28:
            mention_28.append(mentions[27])
        else:
            mention_28.append("None")
        if len(mentions) >= 29:
            mention_29.append(mentions[28])
        else:
            mention_29.append("None")
        if len(mentions) >= 30:
            mention_30.append(mentions[29])
        else:
            mention_30.append("None")
        if len(mentions) >= 31:
            mention_31.append(mentions[30])
        else:
            mention_31.append("None")
        if len(mentions) >= 32:
            mention_32.append(mentions[31])
        else:
            mention_32.append("None")
        if len(mentions) >= 33:
            mention_33.append(mentions[32])
        else:
            mention_33.append("None")
        if len(mentions) >= 34:
            mention_34.append(mentions[33])
        else:
            mention_34.append("None")
        if len(mentions) >= 35:
            mention_35.append(mentions[34])
        else:
            mention_35.append("None")
        if len(mentions) >= 36:
            mention_36.append(mentions[35])
        else:
            mention_36.append("None")
        if len(mentions) >= 37:
            mention_37.append(mentions[36])
        else:
            mention_37.append("None")
        if len(mentions) >= 38:
            mention_38.append(mentions[37])
        else:
            mention_38.append("None")
        if len(mentions) >= 39:
            mention_39.append(mentions[38])
        else:
            mention_39.append("None")
        if len(mentions) >= 40:
            mention_40.append(mentions[39])
        else:
            mention_40.append("None")
        if len(mentions) >= 41:
            mention_41.append(mentions[40])
        else:
            mention_41.append("None")
        if len(mentions) >= 42:
            mention_42.append(mentions[41])
        else:
            mention_42.append("None")
        if len(mentions) >= 43:
            mention_43.append(mentions[42])
        else:
            mention_43.append("None")
        if len(mentions) >= 44:
            mention_44.append(mentions[43])
        else:
            mention_44.append("None")

        if len(off_men) >= 1:
            if off_men[0] in common_mention:
                common_mention1.append(common_mention.index(off_men[0]))
            else:
                common_mention1.append(-1)
        else:
            common_mention1.append(-2)
        if len(off_men) >= 2:
            if off_men[1] in common_mention:
                common_mention2.append(common_mention.index(off_men[1]))
            else:
                common_mention2.append(-1)
        else:
            common_mention2.append(-2)
        if len(off_men) >= 3:
            if off_men[2] in common_mention:
                common_mention3.append(common_mention.index(off_men[2]))
            else:
                common_mention3.append(-1)
        else:
            common_mention3.append(-2)
        if len(off_men) >= 4:
            if off_men[3] in common_mention:
                common_mention4.append(common_mention.index(off_men[3]))
            else:
                common_mention4.append(-1)
        else:
            common_mention4.append(-2)
        if len(off_men) >= 5:
            if off_men[4] in common_mention:
                common_mention5.append(common_mention.index(off_men[4]))
            else:
                common_mention5.append(-1)
        else:
            common_mention5.append(-2)
        if len(off_men) >= 6:
            if off_men[5] in common_mention:
                common_mention6.append(common_mention.index(off_men[5]))
            else:
                common_mention6.append(-1)
        else:
            common_mention6.append(-2)
        if len(off_men) >= 7:
            if off_men[6] in common_mention:
                common_mention7.append(common_mention.index(off_men[6]))
            else:
                common_mention7.append(-1)
        else:
            common_mention7.append(-2)
        if len(off_men) >= 8:
            if off_men[7] in common_mention:
                common_mention8.append(common_mention.index(off_men[7]))
            else:
                common_mention8.append(-1)
        else:
            common_mention8.append(-2)
        if len(off_men) >= 9:
            if off_men[8] in common_mention:
                common_mention9.append(common_mention.index(off_men[8]))
            else:
                common_mention9.append(-1)
        else:
            common_mention9.append(-2)
        if len(off_men) >= 10:
            if off_men[9] in common_mention:
                common_mention10.append(common_mention.index(off_men[9]))
            else:
                common_mention10.append(-1)
        else:
            common_mention10.append(-2)
        if len(off_men) >= 11:
            if off_men[10] in common_mention:
                common_mention11.append(common_mention.index(off_men[10]))
            else:
                common_mention11.append(-1)
        else:
            common_mention11.append(-2)
        if len(off_men) >= 12:
            if off_men[11] in common_mention:
                common_mention12.append(common_mention.index(off_men[11]))
            else:
                common_mention12.append(-1)
        else:
            common_mention12.append(-2)
        if len(off_men) >= 13:
            if off_men[12] in common_mention:
                common_mention13.append(common_mention.index(off_men[12]))
            else:
                common_mention13.append(-1)
        else:
            common_mention13.append(-2)

    return mention_1, mention_2, mention_3, mention_4, mention_5, mention_6\
        ,mention_7, mention_8, mention_9, mention_10, mention_11, mention_12\
        ,mention_13, mention_14, mention_15, mention_16, mention_17, mention_18\
        , mention_19, mention_20, mention_21, mention_22, mention_23, mention_24\
        , mention_25, mention_26, mention_27, mention_28, mention_29, mention_30\
        ,mention_31, mention_32, mention_33, mention_34, mention_35, mention_36\
        , mention_37, mention_38, mention_39, mention_40, mention_41, mention_42\
        ,mention_43, mention_44, common_mention1, common_mention2, common_mention3\
        , common_mention4, common_mention5, common_mention6, common_mention7, common_mention8\
        , common_mention9, common_mention10, common_mention11, common_mention12, common_mention13