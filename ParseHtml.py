from bs4 import BeautifulSoup
import os
import FriendCrawl
import json


def getFriends(html):
    friends = {}
    soup = BeautifulSoup(html, 'html.parser')
    # main_list = soup.find('div', {'id':"pagelet_timeline_medley_friends"})

    for li in soup.find_all("li"):
        # print(li.encode('utf-8'))
        try:
            name = li.find('img').attrs['aria-label']
            friends[name] = {
                'name': name,
                'image': li.find('img').attrs['src'],
                'profile': li.find('a').attrs['href'],
            }
        except:
            continue
    
    # return {k: str(v).encode("utf-8") for k,v in friends.items()}
    return friends

def getGroups(html):
    groups = {}
    soup = BeautifulSoup(html, 'html.parser')
    # main_list = soup.find('div', {'id':"pagelet_timeline_medley_groups"})
    try:
        for link in soup.find_all("a"):
            if (not link.text) or ("groups" not in link.attrs['href']):
                continue
            # print(li.encode('utf-8'))
            name = link.attrs['href']
            groups[name] = str(link.text)
            
    except:
        pass
    
    # return {k: str(v).encode("utf-8") for k,v in friends.items()}
    return groups

if __name__ == '__main__':
    profile = "https://www.facebook.com/profile.php?id=100010532354193"
    crawler = FriendCrawl.FacebookCrawler(login='checkptransfer@hotmail.com', password='d95-ggF-HFs-c7u',)

    friends = getFriends(crawler.goToFriends(profile))

    with open('friends.json', 'w') as fp:
        json.dump(friends, fp)

    groups = getGroups(crawler.goToGroups(profile))

    with open('groups.json', 'w') as fp:
        json.dump(groups, fp)

    crawler.quit()

    # crawler.goToGroups(profile)

