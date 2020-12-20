# Decoding-IPL-Match-Analysis

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

2. **Create_ball_by_ball_dataset.ipynb**: Converts the categorized features (batsman, non-striker and bowler) in deliveries.csv into their corresponding vectors.

3. **Create_variable_balls_dataset.ipynb**: Groups together variable number of balls from the deliveries.csv.

4. **EDA.ipynb**: Contains the Exploratory Data Analysis performed on the collected data. 

5. **HyperparameterTuning_Regression.ipynb**: Regression based models with hyperparameter tuning for the best model.

6. **Player_Embedding_Vectors.ipynb**: Creates player embeddings based on the player-wise performance scraped from IPL's official website.

7. **match_classification.ipynb**: Classification models with hyperparameter tuning for the match result prediction task.                         











  







