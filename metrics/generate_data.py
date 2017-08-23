import json
import random

campaign_id = [100, 101, 102, 103, 104, 105, 106, 107, 108, 109]
ad_id = [1000, 1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010, 1011, 1012, 1013, 1014, 1015, 1016, 1017, 1018, 1019, 1020, 1021, 1022, 1023, 1024, 1025, 1026, 1027, 1028, 1029, 1030]
ad_name = [u'1000_Laura Hughes', u'1001_Virginia Garza', u'1002_Kyle Ahart', u'1003_Robert Lee', u'1004_Evan York', u'1005_George Houghton', u'1006_Kristina Bump', u'1007_Aleta Franks', u'1008_Emma Sims', u'1009_Michael Rodriguez', u'1010_Michelle Miller', u'1011_Nicole Adrian', u'1012_Keith Rodriguez', u'1013_Frank Olivas', u'1014_Matthew Shinabarger', u'1015_George Martinez', u'1016_Alberta Chandler', u'1017_Matthew Goldstein', u'1018_Richard Summers', u'1019_Chris Wilson', u'1020_Mary Pollard', u'1021_Lewis Carr', u'1022_Vern Barton', u'1023_William Conger', u'1024_Gerald Brown', u'1025_Rose Gonzales', u'1026_Howard Risner', u'1027_Philip Barnhart', u'1028_Nancy Faustini', u'1029_Dawn Malone', u'1030_Richard Chynoweth']
campaign_name = [u'100_Steve Hernandez', u'101_Mildred Huynh', u'102_Frank Anderson', u'103_Jeff Amos', u'104_Todd Mathers', u'105_Dorothy Foreman', u'106_Penny Bridges', u'107_James White', u'108_James Belyoussian', u'109_Aaron Querta']
user_name = [u'Peggy Jones', u'William Anteby', u'Brian Outlaw', u'William Cruz', u'Harold Mcelroy', u'Estella Murray', u'James Spencer', u'William Garcia', u'Sean Duenas', u'Lois Barker']


file_name_path = '/Users/arpith/PycharmProjects/analytics/data_index/raw_data_sampled.json'

from random import randrange
from datetime import timedelta, datetime


def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

with open(file_name_path, 'w') as w:
    data = []
    d1 = datetime.strptime('2017-08-15 1:30 PM', '%Y-%m-%d %I:%M %p')
    d2 = datetime.strptime('2017-08-22 1:30 AM', '%Y-%m-%d %I:%M %p')
    for _ in range(500):
        x = {"url": "/foo/bar", "user": random.choice(user_name), "latencyMs": 32,
             "time":random_date(d1, d2).strftime('%Y-%m-%dT%H:%M:%SZ'), "campaignId":random.choice(campaign_id), "campaignName":random.choice(campaign_name),
                     "adId":random.choice(ad_id), "impressions":random.randint(1,100),"clicks":random.randint(1,100),"interactions":random.randint(1,100),
                      "pinches":random.randint(1,100),"touches":random.randint(1,100),
                     "swipes":random.randint(1,100),
                     "adName":random.choice(ad_name)}
        json.dump(x, w)
        w.write('\n')