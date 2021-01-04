# Decoding IPL: Match Analysis

Our project has two aims. 
1. Predict the
outcome of matches, i.e. the winner of the match, based
on previous years’ data. 
2. Predict the
scores during certain intervals of the game. For example,
the score in overs 1-15, 1-10 or 3-8 etc.

To accomplish this, algorithms such as Decision Trees, Linear
Regression, Random Forest and Support Vector Machines
have been used.

---


The file structure is as follows:

1. **Dataset/**: This directory contains all the data files, stored weights and the embedding matrix. 
    1. **Dataset/Embeddings/**: Contains the embedding matrix 
        1. **emb_player_vec_dict**: contains the embedding matrix and vector information.
        2. **emb_player_stoi_dict**: contains the string to index information for player names.
        3. **del_to_emb_final**: stores the mapping of player names from deliveries.csv to embedding matrix.
        4. **emb_player_vec_dict**: stores the embedding vector player_name wise.
        5. **not_found**: contains the list of players who had different names in both the datasets.
    2. **Dataset/cricksheet_ipl_csv**: Data collected from [Cricsheet's website](https://cricsheet.org/) in .csv format.
    3. **Dataset/cricsheet_ipl_yaml**:  Data collected from [Cricsheet's website](https://cricsheet.org/) in .yaml format.  
    4. **Dataset/ipl_stats**: Data scraped from the [IPL's official website](https://www.iplt20.com/) for season wise player points.
    5. **Dataset/kaggle_data**: contains matches.csv (match-wise information about every IPL season from 2008 to 2020) and deliveries.csv (delivery-wise information about every IPL match).
    6. **Dataset/Ball_by_ball.csv**: contains modified deliveries.csv with 7-dimensional vectors instead of player names.

2. **Reports/**: 
    1. **Project_Presentation.pptx**: Project presentation
    2. **Project_Report.pdf**: A detailed project report

3. **plots/**: Folder containing plots created during Exploratory Data Analysis.

4. **Ball_by_Ball_Regression.ipynb**: Code to perform regression on ball-by-ball dataset. It predicts the score for each ball.

5. **Create_ball_by_ball_dataset.ipynb**: Converts the categorized features (batsman, non-striker and bowler) in deliveries.csv into their corresponding vectors.

6. **Create_variable_balls_dataset.ipynb**: Groups together variable number of balls from the deliveries.csv.

7. **EDA.ipynb**: Contains the Exploratory Data Analysis performed on the collected data. 

8. **HyperparameterTuning_Regression.ipynb**: Regression based models with hyperparameter tuning for the best model.

9. **Player_Embedding_Vectors.ipynb**: Creates player embeddings based on the player-wise performance scraped from IPL's official website.

10. **match_classification.ipynb**: Classification models with hyperparameter tuning for the match result prediction task.                         







  







