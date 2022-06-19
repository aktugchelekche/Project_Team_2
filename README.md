# Project Team 2

<p align="center"> <img width="299" alt="Screen Shot 2022-06-11 at 3 47 29 PM" src="https://user-images.githubusercontent.com/98676400/173204357-6cdd455f-daec-480f-9cc0-0fcc33533950.png"> </p>

<strong>A Machine Learning Final Project for discovering what type of components needs to be combined to create a popular song.</strong>

## Our Team

* <strong>Julian Flores - Circle Role</strong>  :The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project.

* <strong>Robby Rangel - Triangle Role</strong>    :The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project step

* <strong>Aktug Cilekci - Square Role </strong>  : The team member in the square role will be responsible for the repository.


## Our Goal : What Makes a Song Popular ?

With our Machine Learning Model, we want to predict/calculate the popularity of a song with given features such as its "danceability" , "key" and "tempo" etc. The scale that we are using to determine whether a song is popular or not is <code> pd.qcut </code> then label it <code> popular =1 </code> and <code> not popular = 0</code> . 


## Description of Our source of Data

The datasets are comprised of 2000 rows and 18 columns from two datasets. We can say that this dataset contains the Top 2000 songs from 2000-2019.
To increase the depth of understanding of the data, we must first understand the content of each column present in the dataset.

## EDA
* We began the project with ETL. We have read the csv files then prepared to export to Pgadmin by dropping <code>duplicated</code> rows .
* Next, we joined two tables by <code>inner</code> join via Pgadmin and exported the joined table as <code> songs_normalized</code>
* We will create variety of plots to discover most correlated features. This step will help us to reduce number of features. 
* Drop <code> Null </code> and <code> Duplicates </code> columns (again) ensure to keep our data clean and this would make our ML model work more efficiently. 
* There are few columns such as "explicit" that we will convert it as  <code>numeric</code> column.
* We will need to <code>encode</code> "genre" column as it contains multiple unique values. 
* To prepare our dataset for ML model, we will remove columns "Artist" , "Song" and "Year"  etc as they are irrelevant for ML model.

*We will update our outline as we face any issues. 

#### Column Descriptions

* <code>artist</code>: Name of the Artist.
* <code>song</code>: Name of the Track.
* <code>duration_ms</code>: Duration of the track in milliseconds.
* <code>explicit</code>: The lyrics or content of a song or a music video contain one or more of the criteria which could be considered offensive or unsuitable for children.
* <code>year</code>: Release Year of the track.
* <code>popularity</code>: The higher the value the more popular the song is.
* <code>danceability</code>: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* <code>energy</code>: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
* <code>key</code>: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
* <code>loudness</code>: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
* <code>mode</code>: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* <code>speechiness</code>: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* <code>acousticness</code>: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* <code>instrumentalness</code>: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* <code>liveness</code>: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* <code>valence</code>: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
* <code>tempo</code>: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* <code>genre</code>: Genre of the track

##  Machine Learning Model 

[Machine Learning Report ](https://github.com/aktugchelekche/Project_Team_2/blob/main/Machine_Learning_Models)

## Communication 

The team members will communicate via Slack and/or Zoom if necessary.

## Resources
[Top Hits Spotify from 2000-2019](https://github.com/aktugchelekche/Project_Team_2/tree/main/Resources)
