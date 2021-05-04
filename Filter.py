#Author: Brian Contreras
#Date: 4/30/2021
#Update:
#Description: A file to filter tweets from a search to make it easier to read


#Filters posts searched in the scrapper to the keywords inputted by the user in the UI
def filterMedia(posts, keywords):
    filteredPosts = []
    keyword = parseKeywords(keywords)

    for x in keyword:
        for y in posts:
            if keyword[x] in posts[y]:
                filteredPosts.append(posts[y])
                del posts[y]

    return filteredPosts



#Parses the user inputted keywords from a string to a list
def parseKeywords(keywords):
    parsedKeywords = keywords.split(", ")
    return parsedKeywords