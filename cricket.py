wheather=['Sunny','Sunny','Overcast','Rainy','Rainy','Rainy','Overcast','Sunny','Sunny',
'Rainy','Sunny','Overcast','Overcast','Rainy']
temp=['Hot','Hot','Hot','mild','cool','cool','cool','mild','cool','mild','mild','mild','Hot','mild']
play=['No','No','Yes','Yes','Yes','No','Yes','No','Yes','Yes','Yes','Yes','Yes','No']
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
wheather_encoded=le.fit_transform(wheather)
print (wheather_encoded)
temp_encoded=le.fit_transform(temp)
label=le.fit_transform(play)
print ("Temp:",temp_encoded)
print ("Play:",label)
features=list(zip(wheather_encoded,temp_encoded))
print(features)
from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
model.fit(features,label)
print (Sunny:-2,overcast:-1,Rainy:-0)
print(Hot:-2,cool:-1,mild:-0)
a=int(input(enter the value for wheather))
b=int(input(enter the value for temperature))
predicted=model.predict([[0,2]])
print("Predicted Value:", predicted)
