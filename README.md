<p align="center"> <img width="299" alt="Screen Shot 2022-06-11 at 3 47 29 PM" src="https://user-images.githubusercontent.com/98676400/173204357-6cdd455f-daec-480f-9cc0-0fcc33533950.png"> </p>

# Project_Team_2 - Machine Learning Project 
Final project for discovering the omponents that must be combined to determine a popular or not popular song applying Machine Learning

## Self Assesment
The group project 002 -work together to develop this Machine Learning Project,The team was conformed by three members with different roles as described below:
* Robby Rangel - Triangle Role :The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project step
* Aktug Cilekci - Square Role : The team member in the square role will be responsible for the repository.
* Julian Flores - Circle Role :The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project.
The team work togeteher, very supportive and I learned a lot from the other team memebers, the main challenge was keep the speed and technicallity applied for our team to develop the complete project. but all was very well managed via our slack communications and our sesions during class, each member apport individual contributions, extensively discussed in our sessions as well.
The project team used the following resources:
* Data : Top Hits Spotify from 2000-2019
* Software/Languages: Jupyter Notebook, Google Colab. PostgresSql. Heroku
Python, PgAdmin ,
* Libraries:  Pandas; Numpy, SqlAlchemy, Psycopg2; Streamlite; Joblib; Tensorflow, Scikit-learn; Seaborn, Matplotlib and Plotly.

## Team Assessment

### Our Team

* Aktug Cilekci - Square Role : The team member in the square role will be responsible for the repository.
* Robby Rangel - Triangle Role :The member in the triangle role will create a mockup of a machine learning model. This can even be a diagram that explains how it will work concurrently with the rest of the project step
* Julian Flores - Circle Role :The member in the circle role will create a mockup of a database with a set of sample data, or even fabricated data. This will ensure the database will work seamlessly with the rest of the project.

### Our Project: 2000-2019 (20 Years in Music)

### Our Goal : What Makes a Song Popular ?

With our Machine Learning Model, we want to predict/calculate the popularity of a song with given features such as its "danceability" , "key" and "tempo" etc.

## Summary of Project

We started with datasets that were comprised of 2000 rows and 18 columns. Most columns , such as danceability, liveness, tempo, and song duration were already in integer format and did not need any feature engineering. Some columns did have to be encoded., such as : Explicit had to be converted to numeric , popularity converted to categorical, and genre needed to be encoded.

### Description of how data was split into training and testing sets:

* The data was split on 20% test to 80% training.

### Explanation of model choice, including limitations and benefits:

* Neural Network: 2 Hidden Layers with 200 and 100 nodes respectively and activation function as ‘Relu’ – accuracy: 0.63

* Random Forest Classifier: accuracy: 0.63

* Support Vector Model: accuracy: 0.518

* Logistic Regression: accuracy: 0.50
