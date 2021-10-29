COMP 5630 - Machine Learning Spring 2021 Final Project
Below is the required information and format per project specs.

appendPAS.py: reads final historical Player Ability Scores, appends to relevant entries in full data-set -AGG

callAPI.py: Scrapes data from Riot Games API to populate dataset -DATA

createScoreCSV.py: easy to interpret and visualize representation of historical player ability scores -AGG

createWinrateDF.py: Scrapes win percentage data from op.gg to populate winrate reference set -DATA

display.py: Pulls in results from scalability trials for each baseline and final algorithm, plots fit vs predict times for each algorithm, maps overall final performance of each algorithm -VIS

nnMLPClassifier.py: Single-runs NN trials, and performs complete scalability trial, outputs results to be used by display -ALGO

NaiveBayes.py: Single-runs NB trials, and performs complete scalability trial, outputs results to be used by display -ALGO

kNearestNeighbors.py: Single-runs kNN trials, and performs complete scalability trial, outputs results to be used by display -ALGO

newerWeights.py: Uses final updated process to assess how weighted each objective and statistics should be in 
    the player ability score calculations. Also assists in data-set review to identify useless features -AGG/DATA

oldWeights.py: Used mainly for initial data-set review to identify chaotic features first implementation of player ability scores used this, abandoned for updated method -AGG/DATA

openAbilityScores.py: Used to retrieve final calculated ability scores -AGG

playerAbility.py: Uses found feature weights and fully populated dataset to calculate historical player scores -AGG

playerDict.py: Used by player ability score calculation to populate the set of represented human players, and manage their scores -AGG

preProcess.py: combines averages of multiple scalability trials for algorithms, outputs final average to file -DATA

decisionTree.py: Single-runs decision tree trials, and performs complete scalability trial, outputs results to be used by display -ALGO

txtToParquet.py: Simply converts test files to parquets, used in exchanging data between team members -DATA

SVM.py: Single-runs SVM trials, and performs complete scalability trial, outputs results to be used by display -ALGO
    
The commands related to feature weighting and aggregative scoring (AGG/DATA) were mostly used in the initial phases of data-review and the tweaking of scoring calculations. These commands must only be called once at product initialization in order to populate weighted lists of features for aggregative scoring, and to clean the dataset for method use.

Aggregative score (AGG) calculation methods are only run once on the data-set to initialize and append these values to the fully populated dataset. Each baseline and the final model (ALGO) are then run independently to parse performance metrics, which in turn were read by display.py (VIS) to produce clear and organized graphing of each of our models in order to identify areas of oppurtunity.


Cao, Hui | Lin, Her-bo | Weeden, Alex | Zhou, Min