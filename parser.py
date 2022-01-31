import urllib.request, json

with urllib.request.urlopen("https://api.ampifymusic.com/packs") as url:
    data = json.loads(url.read())
    packs = data['packs']


def sortGenres(x):
    genres = []
    for pack in range (len(x)):
        for genre in x[pack]['genres']:
            if genre not in genres:
                genres.append(genre)
    
    genres.sort()
    return genres


def findHipHopPacks(x):
    hipHop = []
    for pack in range (len(x)):
        for genre in x[pack]['genres']:
            if genre == 'hip-hop':
                hipHop.append(x[pack]['name'])

    hipHop.sort()
    return hipHop


allGenres = sortGenres(packs)
print("ALL GENRES: \n", allGenres)

hipHopPacks = findHipHopPacks(packs)
print("\n PACKS IN GENRE 'HIP-HOP': \n", hipHopPacks)
