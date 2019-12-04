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

A total of 3,442 songs were scraped from just the top 3 artists per region due to time constraints on this project.

Here's the line up - pretty solid if you ask me:

West Coast
- Kendrick Lamar
- Snoop Dogg
- Tupac

East Coast
- Jay-Z
- 50 Cent
- Notorious BIG

South
- 2 Chainz
- J. Cole
- Lil' Wayne

Mid West
- Kanye West
- Eminem
- Big Sean

### Raw Data
![raw](/images/lyrics_raw.png)

### Initially Cleaned Data
![cleaned](/images/lyrics_cleaned.png)


### Text Pre-Processing

Lyrics for each song were processed through the Gensim Library to remove stopwords and lemmetize the words to their roots to reduce complexity.

Went from 1,972,066 individual words to 784,528 individual words

### TF-IDF time:

These words were then inputted into SideKick Learn's Count Vectorizer function to combine the data into 25,212 unique words and produce the TF (Term Frequency) matrix

Math was implemented to create the IDF (Inverse Document Frequency) matrix

With these two matricies, SKLearn's TFIDF Vectorizer was able to generate a vector for each song in terms of the entire corpus of vocabulary captured in the data.

Now we have a mathematical vector representation of each song, we can start looking at commonalities between rappers inside their own region and comparted to rappers outside their region.

# Commonalities of Songs 

### Similarity to Self

The Cosine Similartiy equation was implemented to determine how similar two songs are by determining how "aligned" their vectors are.  The results are between 0 and 1, with 1 being songs that are identical.

Below is the distribution of song similarities among the discographies of each artist individually.  This gives us a glimpse of the diversity of lyrical similarity between songs for a particular artist.

![self_similarity](/images/cosine_similarity/self/Rappers_Self_Similarity_Distribution.png)

Kanye West seems to have the highest average of similarity across all his songs with 95.8% similarity and J. Cole having the least similart (most divese) songs with a similarity of 89.8%

### Similarity Inside Own's Region (Intra-Regional)

Now let's compare the body of work for each artist to the other artists in the same region:

WEST COAST:


![wc_similarity](/images/cosine_similarity/individual/west_coast_similarity.png)

EAST COAST:


![ec_similarity](/images/cosine_similarity/individual/east_coast_similarity.png)


DOWN SOUTH:


![ds_similarity](/images/cosine_similarity/individual/south_similarity.png)


MID WEST:


![mw_similarity](/images/cosine_similarity/individual/midwest_similarity.png)



Interestingly enough, West Coast and Mid West rappers have an intra similarity scores floating around 94-95% whereas East Coast and Southern rappers have an intra similarity score of 92-93%.



### Similartiy Compared to Other Regions in the US (Inter-Regional)

Now we layer on top the distribution of similarities the work for each artist against the songs coming from the other three regions of the US:

WEST COAST:


![wc_inter_similarity](/images/cosine_similarity/combined/westcoastcomparison.png)


EAST COAST:


![ec_inter_similarity](/images/cosine_similarity/combined/eastcoastcomparison.png)

DOWN SOUTH:


![ds_inter_similarity](/images/cosine_similarity/combined/southcomparison.png)

MID WEST:


![mw_inter_similarity](/images/cosine_similarity/combined/midwestcomparison.png)

Even more interestingly enough - it seems that for 3 of the 4 regions, songs by rappers are more similar to the rest of the country than to their particular region.

Only the West Coast has a higher homogeny to itself than to others.

As they say, West Coast is the Best Coast

# CONCLUSIONS

Based on the scope of this project - there is no conclusive evidence of unique regionality solely based on the lyrics of a rap artist.

However this project is pretty narrow in it's scope.  There is much additional processing of the rap lyrics that can be done to further tune the models.

Other features of songs such as style of beats, rap cadence, lyricism, and many others might be a better indicator of regionality rather than the lyrics alone.

One love.







# Extra
### Regional Relevancy Over Time

Another point of interest is the rise and falls of popularity for each region over time.

Relevance is quantified by looking at Google Trends data per rapper over time combined with popularity numbers from Spotify and Soundcloud.

![relevance](/images/relevance.png)






