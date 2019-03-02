import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

train_data = pd.read_csv("train_draft_data.csv")
train_data = train_data.dropna(axis=0)
#print(train_data)
#print(train_data.loc[15])

features = ["MPG","PPG","RPG","APG","WS","BPM","VORP"]
X = train_data[features]
y = train_data.Pk

train_model = DecisionTreeRegressor(random_state=1)
train_model.fit(X,y)
train_pred = train_model.predict(X)
#print(train_pred)

test_X = [15,15,4,3,1,.5,0]
test_pred = train_model.predict(test_X)
print(test_pred)
