#Author: Brian Contreras
#Date: 4/30/2021
#Update: 5/4/2021
#Description: A file to filter tweets from a search to make it easier to read


#Filters posts searched in the scrapper to the keywords inputted by the user in the UI
def filterMedia(posts, keywords):
    filteredPosts = []
    keyword = parseKeywords(keywords)

    for x in keyword:
        for y in posts:
            if keyword[x] in posts[y].title or keyword[x] in posts[y].description:
                filteredPosts.append(posts[y])
                del posts[y]

#
#    for x in posts:
#        if keyword[0] in posts[x].title or keyword[0] in posts[x].description:
#            filteredPosts.append(posts[y])
#            del posts[y]
#            del keyword[0]

    return filteredPosts



#Parses the user inputted keywords from a string to a list
def parseKeywords(keywords):
    parsedKeywords = keywords.split(", ")
    return parsedKeywords
