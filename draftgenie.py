import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

train_data = pd.read_csv("train_draft_data.csv")
#train_data = train_data.dropna(axis=0)
#print(train_data)

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

features = ["MPG","PPG","RPG","APG","WS","BPM","VORP"]
X = train_data[features]
y = train_data.Pk

#train_model = DecisionTreeRegressor(random_state=1)
#train_model.fit(X,y)
#train_pred = train_model.predict(X)
#print(train_pred)

test_X = [15,15,4,3,1,.5,0]
#test_pred = train_model.predict(test_X)
#print(test_pred)
