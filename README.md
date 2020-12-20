# Decoding-IPL-Match-Analysis

The file structure is as follows :

**Dataset/** ---> This directory contains all the data diles, stored weights and embedding matrix 

**Create_ball_by_ball_dataset.ipynb** ---> Convert the categorized features (batsman, non-striker and bowler) in the deliveries.csv into into their corresponding vectors

**HyperparameterTuning_Regression.ipynb** ---> Regression based models with hyperparameter tuning for the best model on the variable number of balls dataset created 

**Create_variable_balls_dataset.ipynb** ---> Groups together variable number of balls from the deliveries.csv 

**match_classification.ipynb** ---> Classification models with hypperparameter tuning for the match result prediction task                         

**Player_Embedding_Vectors.ipynb** ---> Creates player embeddings based on the player-wise performance scraped from IPL's official website 

**EDA.ipynb** ---> Perform Exploratory Data Analysis on the collected data 

**Dataset/Ball_by_ball.csv** ---> containes modified deliveris.csv with 7 dimensional vectors instead of player names 

**Dataset/cricsheet_ipl_yaml** --->  Data collected from Cricksheets website in .yaml format  

**Dataset/ipl_stats** ---> Data scraped from the IPL's official wesite for season wise player points

**Dataset/cricksheet_ipl_csv** ---> Data collected from Cricksheets website in .csv format   

**Dataset/kaggle_data** ---> constains matches.csv (match wise information about every IPL season) and deliveries.csv (delivery wise information about every IPL match)

**Dataset/Embeddings/** ---> Contains the embedding matrix (**emb_player_vec_dict**) and other player to vector information (**emb_player_stoi_dict**) which contains the string to index information for player names , **del_to_emb_final** stores the mapping of player names from deliveries.csv to embedding matriz, **emb_player_vec_dict** stores the player name wise embedding vector, **not_found** has the players wich had different name in both the datasets 




