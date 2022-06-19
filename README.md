# Project Team 2

<p align="center"> <img width="299" alt="Screen Shot 2022-06-11 at 3 47 29 PM" src="https://user-images.githubusercontent.com/98676400/173204357-6cdd455f-daec-480f-9cc0-0fcc33533950.png"> </p>

<strong>A Machine Learning Final Project for discovering what type of components needs to be combined to create a popular song.</strong>

## Our Team

* <strong>Julian Flores - Circle Role</strong>  :The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project.

* <strong>Robby Rangel - Triangle Role</strong>    :The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project step

* <strong>Aktug Cilekci - Square Role </strong>  : The team member in the square role will be responsible for the repository.


## Our Goal : What Makes a Song Popular ?

With our Machine Learning Model, we want to predict/calculate the popularity of a song with given features such as its "danceability" , "key" and "tempo" etc. The scale that we are using to determine whether a song is popular or not is calculated with 
* <code>pd.qcut(songs_df["popularity"],q=2 ,labels=[0,1] ).astype('int')</code>  
* Then label it as <code> popular =1 </code> and <code> not popular = 0</code> . 


## Description of Our source of Data

The datasets are comprised of 2000 rows and 18 columns from two datasets. We can say that this dataset contains the Top 2000 songs from 2000-2019.
To increase the depth of understanding of the data, we must first understand the content of each column present in the dataset.

## Description of The Data exploration Phase of The project
#### ETL, EDA , Feature Engineering and Data Preprocessing

* We began the project with ETL. We have read the csv files then prepared to export to Pgadmin by dropping <code>duplicated</code> rows .
* Next, we joined two tables by <code>inner</code> join via Pgadmin and exported the joined table as <code> songs_normalized</code>
* We will create variety of plots to discover most correlated features. This step will help us to reduce number of features. 
* Drop <code> Null </code> and <code> Duplicates </code> columns (again) ensure to keep our data clean and this would make our ML model work more efficiently. 
* There are few columns such as "explicit" that we will convert it as  <code>numeric</code> column.
* Conver <code>popularity</code> to cotegorical data. 
* We will need to <code>encode</code> "genre" column as it contains multiple unique values. 
- [Feature Descriptions](https://www.kaggle.com/datasets/paradisejoy/top-hits-spotify-from-20002019) can be found in the link 

- Details can be found in the [ETL_EDA_Data_Preprocessing](https://github.com/aktugchelekche/Project_Team_2/tree/main/ETL_EDA_Data_Preprocessing) folder. 

## Description of The Analysis Phase of The project
###  Machine Learning Model 

[Machine Learning Report ](https://github.com/aktugchelekche/Project_Team_2/blob/main/Machine_Learning_Models): 

 * Description of preliminary data
preprocessing
 * Description of preliminary feature
engineering and preliminary feature
selection, including their decision-making
process
 * Description of how data was split into
training and testing sets
 * Explanation of model choice,

##  Dashboard
[Project Team #2 DashBoard](https://public.tableau.com/app/profile/rarangel/viz/Project_Team_2_Dashboard/Dashboard?publish=yes)


## Communication 

The team members will communicate via Slack and/or Zoom if necessary.

## Resources
* Data : [Top Hits Spotify from 2000-2019](https://github.com/aktugchelekche/Project_Team_2/tree/main/Resources)
* Software/Languages: 
  * Jupyter Notebook, Google Colab. PostgresSql.
  * Python, PgAdmin
* Libraries: 
  * Pandas ,Numpy ,SqlAlchemy, Psycopg2.
  * Tensorflow,Scikit-learn.
  * Seaborn, Matplotlib ,Plotly.
  
