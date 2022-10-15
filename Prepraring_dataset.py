import pandas as pd

dt = pd.read_csv('congressional_tweet_training_data.csv')

def new_dataset(hashtag_1, hashtag_2, hashtag_3, hashtag_4, hashtag_5, hashtag_6, hashtag_7
, hashtag_8, hashtag_9, hashtag_10, hashtag_11, hashtag_12, hashtag_13, hashtag_14
, hashtag_15, hashtag_16, hashtag_17, hashtag_18, common_hashtag1, common_hashtag2
, common_hashtag3, common_hashtag4, common_hashtag5, common_hashtag6, common_hashtag7
, common_hashtag8, common_hashtag9, common_hashtag, mention_1, mention_2, mention_3, mention_4, mention_5, mention_6
, mention_7, mention_8, mention_9, mention_10, mention_11, mention_12
, mention_13, mention_14, mention_15, mention_16, mention_17, mention_18
, mention_19, mention_20, mention_21, mention_22, mention_23, mention_24
, mention_25, mention_26, mention_27, mention_28, mention_29, mention_30
, mention_31, mention_32, mention_33, mention_34, mention_35, mention_36
, mention_37, mention_38, mention_39, mention_40, mention_41, mention_42
, mention_43, mention_44, common_mention1, common_mention2, common_mention3
, common_mention4, common_mention5, common_mention6, common_mention7, common_mention8
, common_mention9, common_mention10, common_mention11, common_mention12
, common_mention13, url1, url2, url3, url4, url5, url6, url7, common_url1, common_url2
, is_using_URL, mention, list_amp, num_hashtag,
plain_text, year, parti,nohashtag_text ,nomention_text
, nourl_text, nodecode_text, full_text, RT_list, important_letter, full_word
,without_mention_word, without_hashtag_word, without_url_word, plain_word):

    dt.drop('party_id', axis=1, inplace=True)
    dt.drop('year', axis=1, inplace=True)
    dt.drop('full_text', axis=1, inplace=True)
    dt.drop('hashtags', axis=1, inplace=True)

    dt['contain_URL'] = is_using_URL  # add column contain URL
    dt['plain_text'] = plain_text
    dt['nohashtag_len'] = nohashtag_text
    dt['nomention_len'] = nomention_text
    dt['nourl_len'] = nourl_text
    dt['nodecode_text'] = nodecode_text
    dt['years'] = year
    dt['mention'] = mention
    dt['common_hashtags'] = common_hashtag
    dt['hashtag1'] = hashtag_1
    dt['hashtag2'] = hashtag_2
    dt['hashtag3'] = hashtag_3
    dt['hashtag4'] = hashtag_4
    dt['hashtag5'] = hashtag_5
    dt['hashtag6'] = hashtag_6
    dt['hashtag7'] = hashtag_7
    dt['hashtag8'] = hashtag_8
    dt['hashtag9'] = hashtag_9
    dt['hashtag10'] = hashtag_10
    dt['hashtag11'] = hashtag_11
    dt['hashtag12'] = hashtag_12
    dt['hashtag13'] = hashtag_13
    dt['hashtag14'] = hashtag_14
    dt['hashtag15'] = hashtag_15
    dt['hashtag16'] = hashtag_16
    dt['hashtag17'] = hashtag_17
    dt['hashtag18'] = hashtag_18
    dt['mention1'] = mention_1
    dt['mention2'] = mention_2
    dt['mention3'] = mention_3
    dt['mention4'] = mention_4
    dt['mention5'] = mention_5
    dt['mention6'] = mention_6
    dt['mention7'] = mention_7
    dt['mention8'] = mention_8
    dt['mention9'] = mention_9
    dt['mention10'] = mention_10
    dt['mention11'] = mention_11
    dt['mention12'] = mention_12
    dt['mention13'] = mention_13
    dt['mention14'] = mention_14
    dt['mention15'] = mention_15
    dt['mention16'] = mention_16
    dt['mention17'] = mention_17
    dt['mention18'] = mention_18
    dt['mention19'] = mention_19
    dt['mention20'] = mention_20
    dt['mention21'] = mention_21
    dt['mention22'] = mention_22
    dt['mention23'] = mention_23
    dt['mention24'] = mention_24
    dt['mention25'] = mention_25
    dt['mention26'] = mention_26
    dt['mention27'] = mention_27
    dt['mention28'] = mention_28
    dt['mention29'] = mention_29
    dt['mention30'] = mention_30
    dt['mention31'] = mention_31
    dt['mention32'] = mention_32
    dt['mention33'] = mention_33
    dt['mention34'] = mention_34
    dt['mention35'] = mention_35
    dt['mention36'] = mention_36
    dt['mention37'] = mention_37
    dt['mention38'] = mention_38
    dt['mention39'] = mention_39
    dt['mention40'] = mention_40
    dt['mention41'] = mention_41
    dt['mention42'] = mention_42
    dt['mention43'] = mention_43
    dt['mention44'] = mention_44
    dt['url1'] = url1
    dt['url2'] = url2
    dt['url3'] = url3
    dt['url4'] = url4
    dt['url5'] = url5
    dt['url6'] = url6
    dt['url7'] = url7
    dt['common_url1'] = common_url1
    dt['common_url2'] = common_url2

    dt['common_mention1'] = common_mention1
    dt['common_mention2'] = common_mention2
    dt['common_mention3'] = common_mention3
    dt['common_mention4'] = common_mention4
    dt['common_mention5'] = common_mention5
    dt['common_mention6'] = common_mention6
    dt['common_mention7'] = common_mention7
    dt['common_mention8'] = common_mention8
    dt['common_mention9'] = common_mention9
    dt['common_mention10'] = common_mention10
    dt['common_mention11'] = common_mention11
    dt['common_mention12'] = common_mention12
    dt['common_mention13'] = common_mention13
    dt['common_hashtags1'] = common_hashtag1
    dt['common_hashtags2'] = common_hashtag2
    dt['common_hashtags3'] = common_hashtag3
    dt['common_hashtags4'] = common_hashtag4
    dt['common_hashtags5'] = common_hashtag5
    dt['common_hashtags6'] = common_hashtag6
    dt['common_hashtags7'] = common_hashtag7
    dt['common_hashtags8'] = common_hashtag8
    dt['common_hashtags9'] = common_hashtag9
    dt['RT'] = RT_list
    dt['word_len'] =full_word
    dt['no_hashtag_word'] = without_hashtag_word
    dt['no_mention_word'] = without_mention_word
    dt['no_url_word'] = without_url_word
    dt['plain_word'] = plain_word
    dt['full_text'] = full_text
    dt['amp'] = list_amp
    dt['stopwords_count'] = important_letter
    dt['party'] = parti

    return dt