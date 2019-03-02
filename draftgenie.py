import pandas as pd
import random
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

#1996
train_data = pd.read_csv("train_draft_data.csv")
#print(train_data)

def get_mae(max_leaf_nodes, train_X, val_X, train_y, val_y):
    model = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes, random_state=0)
    model.fit(train_X, train_y)
    preds_val = model.predict(val_X)
    mae = mean_absolute_error(val_y, preds_val)
    return(mae)

null_columns = ["MPG","PPG","RPG","APG","WS/48","BPM","VORP"]

def get_rid_of_nulls(train_data):
	#print(train_data[null_columns])
	for pick in range(1,61):
		check_for_empty = train_data.loc[train_data["Pk"]==pick]
		non_empty = check_for_empty.dropna(axis=0)
	#print(non_empty[null_columns])
		for col in null_columns:
			empty_columns = check_for_empty[check_for_empty[col].isnull()][null_columns]
		#print(non_empty[col].astype(float).describe())
			if len(empty_columns)>0:
				mean = non_empty[col].astype(float).mean()
				empty_columns[col] = mean
				train_data.set_value(empty_columns.index,col,mean)
				#print(empty_columns)
	#print(train_data)
	train_data.to_csv("no_empties.csv")

#get_rid_of_nulls(train_data)
train_data = pd.read_csv("no_empties.csv")
train_data = train_data.dropna(axis=0)

#print(train_data[].describe())

features = ["MPG","PPG","RPG","APG","WS/48","BPM","VORP"]
X = train_data[features]
y = train_data.Pk

train_X,val_X,train_y,val_y = train_test_split(X,y,random_state=0)

###Determine best number of nodes
candidate_max_leaf_nodes =[6,7,8,9,10,11,12,13,14,15]
scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
best_tree_size = min(scores, key=scores.get)
#print(best_tree_size)

train_model = DecisionTreeRegressor(max_leaf_nodes=60,random_state=1)
train_model.fit(X,y)
train_pred = train_model.predict(X)
#print(train_pred)

#train_model = RandomForestRegressor(random_state=1)
#train_model.fit(train_X,train_y)
#train_pred = train_model.predict(val_X)
#print(train_pred)

#train_mae = mean_absolute_error(train_pred,y)
#print(train_mae)

data = pd.read_csv("https://docs.google.com/spreadsheets/u/0/d/1_Ku5z1ZmroFhRuC6Pn37QZrbrMi_71ije-SypV8Woyw/export?format=csv&id=1_Ku5z1ZmroFhRuC6Pn37QZrbrMi_71ije-SypV8Woyw&gid=0")
#print(data)

mpg= data.at[0,"MPG"]
if pd.isnull(data["MPG"].iloc[0]):
	mpg = train_data["MPG"].mean()

ppg= data.at[0,"PPG"]
if pd.isnull(data["PPG"].iloc[0]):
	ppg = train_data["PPG"].mean()

rpg= data.at[0,"RPG"]
if pd.isnull(data["RPG"].iloc[0]):
	rpg = train_data["RPG"].mean()

apg= data.at[0,"APG"]
if pd.isnull(data["APG"].iloc[0]):
	apg = train_data["APG"].mean()

ws48= data.at[0,"WS/48"]
if pd.isnull(data["WS/48"].iloc[0]):
	ws48 = train_data["WS/48"].mean()

bpm=  data.at[0,"BPM"]
if pd.isnull(data["BPM"].iloc[0]):
	bpm = train_data["BPM"].mean()

vorp= data.at[0,"VORP"]
if pd.isnull(data["VORP"].iloc[0]):
	vorp = train_data["VORP"].mean()
####backup
#mpg = (int(input("Enter in minutes per game, range(2,41): ")))
#ppg = (int(input("Enter in points per game, range(0,27): ")))
#rpg = (int(input("Enter in rebounds per game, range(0,10): ")))
#apg = (int(input("Enter in assists per game, range(0,9): ")))
#ws48 = (float(input("Enter in win share per 48 mintues, range(-.5,.5): ")))
#bpm = (int(input("Enter in box plus/minus, range(-23,20): ")))
#vorp = (int(input("Enter in value over replacement player, range(0,10): ")))

print("MPG:{} PPG:{} RPG:{} APG:{} WS:{:.2f} BPM:{} VORP:{} ".format(mpg,ppg,rpg,apg,ws48,bpm,vorp),end="\n\n")
test_X = ([[mpg,ppg,rpg,apg,ws48,bpm,vorp]])
test_pred = train_model.predict(test_X)
print("Projected draft pick number: {}".format(int(test_pred)))
