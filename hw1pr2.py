#
# hw1pr2 ~ CS181 spring 2021
#

#
# Name(s): Sonia Bliss
#

import requests
import string
import json
import time

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# Problem 2 starter code
#
# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#
#
#



#
# starting function: getting an artist id from a name-lookup
#
def get_id_from_name(artist_name):
    """ This function takes in 
           artist_name:  a string, e.g., "Lizzo" or "Taylor Swift" or ...
           and currently returns an entire json-found dictionary

        Your task is to change it to return only the artist's id#
        Return -1 to signal an error if there was no match.
        There may be many
    """
    # it's good to keep in mind: you don't _have_ to re-download data, if you already have it!

    # a hand-created table of already-found ids (to save API calls)
    # if name == "Taylor Swift": return 159260351
    # if name == "Kendrick Lamar": return 368183298
    # if name == "The Beatles": return 136975    
    # if name == "Lizzo": return 472949623   
    
    # Here, use the itunes search API to get an artist's itunes ID
    search_url = "https://itunes.apple.com/search"
    parameters = {"term":artist_name,"entity":"musicArtist",
                  "media":"music","limit":200}

    result = requests.get(search_url, params=parameters)
    #print(result.url)
    #print(f"result.status_code is {result.status_code}")
    if result.status_code == 200:
        data = result.json()   # this is _ALL_ the data
        #print(f"full url: {result.url}")
        return data['results'][0]['artistId']
        #print("data is", data)

        # you'll want to work with this data at the command-line (or print it here)
    else:
        print("returning {}")
        return {}    # return no data 



#
# Testing the not-quite-correct-yet   get_id_from_name
#
if True:
    print()
    print("Calling for Lizzo:")
    id = get_id_from_name("Lizzo")  # 472949623
    print(f"id is {id}")

    time.sleep(2)

    print()
    print("Calling for Taylor Swift:")
    id = get_id_from_name("Taylor Swift")
    print(f"id is {id}")
    # you'll want to fix the function to return the id only


#
# Then, the second function:    get_albums_from_id(id)
#
#    You'll need to implement this. Here's a single-url example from which to build
#    The itunes documentation (linked in the hw) will help, too
if False:
    pass
    # try pasting this into your browser address bar:
    #     https://itunes.apple.com/lookup?entity=album&id=472949623&limit=200
    #
    # Note: that url does use Lizzo's id...
    # My browser actually downloads the result as a txt file, but it is json
    # You'll need to use the API documentation (and this example) to make this a more general function
    # (Plus, use the first function as a guide...)




def get_albums_from_id(id):
    """takes the id from def_get_id_from_name assembles the url, the parameters into a dictionary for requests, and makes the API call
     return the whole json-obtained dictionary of data
    """
    search_url = "https://itunes.apple.com/lookup"
    parameters = {"entity":"album", "id":id, "limit":200}

    result = requests.get(search_url, params=parameters)

    if result.status_code == 200:
        data = result.json()
        #print(data)
        return data 
    else:
        print("returning {}")
        return {}




# Then, the question-answering function:     more_productive( artist_name1, artist_name2 )

def more_productive( artist_name1, artist_name2 ):
    """Takes two arguments that are two strings of arists names. Looks up the id number for each to make a list of albums for each. Counts the albums
        and returns with artist was more productive (which artist has the higher album count)
    """

    winner = ''
    albums1 =[]
    albums2 = []
    id1 = get_id_from_name(artist_name1)
    id2 = get_id_from_name(artist_name2)
    albumdic1 = get_albums_from_id(id1)
    albumdic2 = get_albums_from_id(id2)
    
    for result in albumdic1["results"]:
        if result["wrapperType"] == 'collection':
            albums1 += [result]
   
    for result in albumdic2["results"]:
        if result["wrapperType"] == 'collection':
            albums2 += [result]

    if len(albums1) > len(albums2):
        winner = artist_name1
    if len(albums2) > len(albums1):
        winner = artist_name2

    print("Who's more productive between", artist_name1, "and", artist_name2,"??")
    print(artist_name1, "had", len(albums1), "results")
    print(artist_name2, "had", len(albums2), "results")
    print(winner, "is more productive!")

    
    



# Finally, ask - and answer - another question using the itunes data from the album lookup...

def another_inquiry( artist_name1, artist_name2 ):
    """Takes two arguments that are two strings of arists names. Looks up the id number for each and gets the album dictinaries for
        an explicit rating. Counts the explicit albums and returns with the artist who has more explicit content
    """
    
    winner = ''
    dirtyalbums1 =[]
    dirtyalbums2 = []
    id1 = get_id_from_name(artist_name1)
    id2 = get_id_from_name(artist_name2)
    albumdic1 = get_albums_from_id(id1)
    albumdic2 = get_albums_from_id(id2)
    
    for result in albumdic1["results"]:
        if result["wrapperType"] == 'collection':
            if result["collectionExplicitness"] == 'explicit':
                dirtyalbums1 += [result]
   
    for result in albumdic2["results"]:
        if result["wrapperType"] == 'collection':
            if result["collectionExplicitness"] == 'explicit':
                dirtyalbums2 += [result]

    if len(dirtyalbums1) > len(dirtyalbums2):
        winner = artist_name1
    if len(dirtyalbums2) > len(dirtyalbums1):
        winner = artist_name2

    print("Who has more explicit music between", artist_name1, "and", artist_name2,"??")
    print(artist_name1, "had", len(dirtyalbums1), "results")
    print(artist_name2, "had", len(dirtyalbums2), "results")
    print(winner, "has more explicit music!")










if True:
    print("\n")
    print("Dictionary of data for queen Megan Thee Stallion:")
    id = get_id_from_name("Megan Thee Stallion")
    get_albums_from_id(id)
    print("\n")
    more_productive( "Cardi B", "Megan Thee Stallion" )
    print("\n")
    another_inquiry( "Kirk Franklin", "Saweetie" )
    print("\n")
    another_inquiry( "Young Thug", "Lil Baby" )
    print("\n")
    another_inquiry( "Amy Winehouse", "Tay Money" )