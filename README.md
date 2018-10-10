# news-event-feed

## Dataset 
   
Download ~10K articles containing information about approx 10 events. 
For now consider one event type: earthquakes.

Download from public data sources using Bing API

## Labeling data

Automatically select similar articles by creating word embedding vectors 
for each article and select those that are close using cosine similarity criteria

Select pool of articles that are "close", approx 5000 and use Mechanical Turk service

to label for each 2 articles:

1. articles are about the same event
2. articles are related. 

Use 
same event articles vectors as positive exampels
generate negative examples.

## Model



