# Urban-Adventure
An app to find the best locations for restaurants, nightlife, and more!

###How it works
We used a large amounts of Twitter, Instagram, Yelp, and Uber data to find you the best places. 

__Yelp__: We used the Yelp API to store their top picks of locations relevant to our search location and theme.

__Twitter__ & __Instagram__: We stored megabytes of tweets and instagram posts that had geolocation tags. We then processed them with a clustering algorithm to find the busiest businesses by location. 

__Indico__: We performed topic modeling to weigh the tweets and instagram posts based on if they, for example, pertained to our search for "bars". On top of that, we ran sentiment analysis to judge whether they had positive or negative themes (E.g. Positive tweet about food = good sign for business in that area)!

__Uber__: Uber is used as part of our weigting for posts. We utilized the 'available services' access point to calculate a measure of 'urbanness' for different locations identified by earlier steps in our pipline.  

### Overview

Once we combined these components, we got an awesome search engine algorithm powered by social media and data analysis! For more information, check out our [Devpost](http://devpost.com/software/urban-adventure) or [video demo](https://www.youtube.com/watch?v=bs2WjugDjAg). 

*Built in 36 hours at Hack the North 2015*