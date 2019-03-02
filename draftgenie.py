import pandas as pd
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

def get_rid_of_nulls(train_data):
	null_columns = ["MPG","PPG","RPG","APG","WS","BPM","VORP"]
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

features = ["MPG","PPG","RPG","APG","WS","BPM","VORP"]
X = train_data[features]
y = train_data.Pk

train_X,val_X,train_y,val_y = train_test_split(X,y,random_state=0)

###Determine best number of nodes
#candidate_max_leaf_nodes =[5,10,15,25,50,100,250,500]
#scores = {leaf_size: get_mae(leaf_size, train_X, val_X, train_y, val_y) for leaf_size in candidate_max_leaf_nodes}
#best_tree_size = min(scores, key=scores.get) #50
#print(best_tree_size)

train_model = DecisionTreeRegressor(max_leaf_nodes=5, random_state=1)
train_model.fit(train_X,train_y)
train_pred = train_model.predict(val_X)

#train_model = RandomForestRegressor(random_state=1)
#train_model.fit(train_X,train_y)
#train_pred = train_model.predict(val_X)
#print(train_pred)

#train_mae = mean_absolute_error(train_pred,val_y)
#print(train_mae)


test_X = [30,20,5,3,1,.5,0]
test_pred = train_model.predict(test_X)
print(int(test_pred))
