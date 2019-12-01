# What We Talkin' Bout

## Lyrical Analysis of Rap Music in America

I wanted to look into the commonalities / differences of lyrics produced by songs of rappers from different regions across America to see if the uniqueness of each region can be quantified.

Historically there has always been the West Coast vs East Coast rap beef but in the recent years there has been the boom of artists from the Mid West as well as Down South.

![rappers](/images/rappers.png)

Now we just need to identify the representatives of each region.

## Who's It Gonna Be

The top 25 artists for each region was identified via polls on www.Ranker.com - a website that implements open sourced polls on various topics to crowdsource the widely accepted leaders of the category.

![ranker](/images/ranker.png)



## Getting Hands on the Lyrics

Lyrical information for songs from all these artists can be found at www.azlyrics.com

![azlyrics](/images/azlyrics.png)

I developed a webscraping tool to crawl through the website to gather the raw HTML per track, clean it to get the lyrical data, and store it into a MongoDB database for future processing.

### Raw Data
![raw](/images/lyrics_raw.png)

### Cleaned Data
![cleaned](/images/lyrics_cleaned.png)


CLEAN EACH SONG
TFIDF PER SONG
VECTORIZE EACH SONG
COMBINED VECTORS PER ARTIST
COMBINED ARTISTS PER REGION

COMPARISON OF REGIONS

CONCLUSIONS








## Relevance of Each Region Over Time

Another point of interest is the rise and falls of popularity for each region over time.

Relevance is quantified by looking at Google Trends data per rapper over time combined with popularity numbers from Spotify and Soundcloud.

![relevance](/images/relevance.png)






