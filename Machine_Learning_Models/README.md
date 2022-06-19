## Machine Learning Model

### Description of preliminary data preprocessing:

1.	Extract, transform and load:
•	Two datasets were extract from Kaggle.com . 
•	The datasets were merged by using sql inner join query. 
•	The dataset was loaded to notebook by engine via PostGresSql server.

2.	Exploratory Data Analysis:
•	Display Data Types.
•	Determine if there is any Null or Missing Values
•	Display Summary of Statistics
•	Creating Visualization:
i.	Popularity Density Plot with Seaborn.
ii.	Range and Distribution Plots for numerical features.
iii.	Multi-Variate Analysis.
iv.	Histogram Plots for each feature 
v.	Correlation Heatmap.
•	Creating categorical column for ‘popularity’ by qcut function. Below the mean popularity will be 0 and above the mean popularity will 1.
•	Convert binary column ‘explicit’ to numerical datatype. 
•	Export the processed dataset to sql table with PostGres server. 

### Description of preliminary feature engineering and preliminary feature selection, including their decision-making process:

1.	Feature engineering and Preliminary Feature Selection
•	Mode column is indicator of modality of each song such Minor and Major and since encoding removes redundancies from data, this column was encoded as "Minor" and "Major".
•	Using bucketing on column ‘artist, song and genre ‘to improve query performance and sampling then encode mentioned column for removing redundancies. 
•	Upon completion of bucketing and encoding, initial columns dropped from the dataset and ready for splitting as training and testing data. 
•	Since we algorithm is still on early stage we are still discovering on selection of features. However, currently we are keeping every feature from the datasets as of now. 

### Description of how data was split into training and testing sets:

•	The data was split on 20% test to 80% training.
    
 Explanation of model choice, including limitations and benefits:

•	Neural Network: 2 Hidden Layers with 200 and 100 nodes respectively and activation function as ‘Relu’ – accuracy: 0.63 

•	Random Forest Classifier: accuracy: 0.63 

•	Support Vector Model: accuracy: 0.518

•	Logistic Regression:  accuracy: 0.50
At this stage, although Neural Network has the highest accuracy, it comes with a high loss as 1.18. Neural Network provides ways to improve accuracy, but it tends to overfit the data. We are currently working on the model to improve accuracy and decrease loss. 

