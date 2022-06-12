# Project Team 2

<p align="center"> <img width="299" alt="Screen Shot 2022-06-11 at 3 47 29 PM" src="https://user-images.githubusercontent.com/98676400/173204357-6cdd455f-daec-480f-9cc0-0fcc33533950.png"> </p>

<strong>A Machine Learning Final Project for discovering what type of components needs to be combined to create a popular song.</strong>

## Our Team : 

* <strong>Julian Flores -Triangle Role</strong>  :The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project.

* <strong>Robby Rangel -Circle Role </strong>    :The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project step

* <strong>Aktug Cilekci - Square Role </strong>  : The team member in the square role will be responsible for the repository.


## Our Goal : What Makes A Song Popular ?



With our Machine Learning Model, we want predict/calculate the popularity of a song with given features such as its "danceability" , "key" and "tempo" etc.


## Description of Our source of Data :

The datasets are composed of 2000 rows and 18 columns from two datasets. We can say that this dataset contains the Top 2000 songs from the period analyzed.
In order to increase the depth of understanding of the data that we must understand the content of each column present in the dataset.

#### EDA
* We began the project with ETL. We have read the csv files then prepared to export to Pgadmin by dropping <code>duplicated</code> rows .
* After that , we join 2 tables by <code>inner</code> join via Pgadmin then export the joined table as <code> songs_normalized</code>
* We will create variety of plots to discover most correlated features. This step will help us to reduce number of features. 
* Drop <code> Null </code> and <code> Dublicates </code> columns (again) ensure to keep our data clean and this woluld make our ML model work more efficiently. 
* There are few columns such as "explicit" that we will convert it as  <code>numeric</code> column.
* We will need to <code>encode</code> "genre" column as it contains multiple unique values. 
* To prepare our dataset for ML model, we will remove columns "Artist" , "Song" and "Year"  etc as they are irrelevant for ML model.

*We will update our outline as we face any issues. 

##### The description of columns are as follows :

* <strong>artist</strong>: Name of the Artist.
* <strong>song</strong>: Name of the Track.
* <strong>duration_ms</strong>: Duration of the track in milliseconds.
* <strong>explicit</strong>: The lyrics or content of a song or a music video contain one or more of the criteria which could be considered offensive or unsuitable for children.
* <strong>year</strong>: Release Year of the track.
* <strong>popularity</strong>: The higher the value the more popular the song is.
* <strong>danceability</strong>: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity. A value of 0.0 is least danceable and 1.0 is most danceable.
* <strong>energy</strong>: Energy is a measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity.
* <strong>key</strong>: The key the track is in. Integers map to pitches using standard Pitch Class notation. E.g. 0 = C, 1 = C♯/D♭, 2 = D, and so on. If no key was detected, the value is -1.
* <strong>loudness</strong>: The overall loudness of a track in decibels (dB). Loudness values are averaged across the entire track and are useful for comparing relative loudness of tracks. Loudness is the quality of a sound that is the primary psychological correlate of physical strength (amplitude). Values typically range between -60 and 0 db.
* <strong>mode</strong>: Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived. Major is represented by 1 and minor is 0.
* <strong>speechiness</strong>: Speechiness detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words. Values between 0.33 and 0.66 describe tracks that may contain both music and speech, either in sections or layered, including such cases as rap music. Values below 0.33 most likely represent music and other non-speech-like tracks.
* <strong>acousticness</strong>: A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic.
* <strong>instrumentalness</strong>: Predicts whether a track contains no vocals. "Ooh" and "aah" sounds are treated as instrumental in this context. Rap or spoken word tracks are clearly "vocal". The closer the instrumentalness value is to 1.0, the greater likelihood the track contains no vocal content. Values above 0.5 are intended to represent instrumental tracks, but confidence is higher as the value approaches 1.0.
* <strong>liveness</strong>: Detects the presence of an audience in the recording. Higher liveness values represent an increased probability that the track was performed live. A value above 0.8 provides strong likelihood that the track is live.
* <strong>valence</strong>: A measure from 0.0 to 1.0 describing the musical positiveness conveyed by a track. Tracks with high valence sound more positive (e.g. happy, cheerful, euphoric), while tracks with low valence sound more negative (e.g. sad, depressed, angry).
* <strong>tempo</strong>: The overall estimated tempo of a track in beats per minute (BPM). In musical terminology, tempo is the speed or pace of a given piece and derives directly from the average beat duration.
* <strong>genre</strong>: Genre of the track


## Communication 

The team members will communicate via Slack and/or Zoom if necessary.

## Resources
[Top Hits Spotify from 2000-2019](https://github.com/aktugchelekche/Project_Team_2/tree/main/Resources)
