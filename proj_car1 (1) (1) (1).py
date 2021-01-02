import pandas as pd
import numpy as np
data=pd.read_csv("car data.csv")
X=data.iloc[:,1:-1].values
Y=data.iloc[:,8].values
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
A=make_column_transformer((OneHotEncoder(categories="auto"),[0,4,5,6]),remainder="passthrough")
X=A.fit_transform(X)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test= train_test_split(X,Y, test_size=0.20,random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(X_train,Y_train)
y_pred= regressor.predict(X_test)
y_pred1=regressor.predict(X_test)
h=list()
v=str(input("Enter your preferred vehicle/nkindly type exactly same(bike/car):"))
if(v=='bike'):
     h.append(1.0)
     h.append(0.0)
elif(v=='car'):
     h.append(0.0)
     h.append(1.0)
else:
     print("enter proper vehicle type")
f=str(input("Enter fuel type exactly same as(CNG/petrol/diesel) vehicle:"))
if(f=='CNG'):
     h.append(1.0)
     h.append(0.0)
     h.append(0.0)     
elif(f=='petrol'):
     h.append(0.0)
     h.append(1.0)
     h.append(0.0)     
elif(f=='diesel'):
     h.append(0.0)
     h.append(0.0)
     h.append(1.0)
else:
     print("enter proper fuel type")
s=str(input("Enter the seller_type exactly same as(Dealer/Individual):"))     
if(s=='Dealer'): 
     h.append(1.0)
     h.append(0.0)
elif(s=='Individual'):
     h.append(0.0)
     h.append(1.0)
else:
     print("enter proper seller type")
g=str(input("Enter the gear_type exactly same as(Manual/Automatic):"))
if(g=='Automatic'):
     h.append(1.0)
     h.append(0.0)
elif(g=='Manual'):
     h.append(0.0)
     h.append(1.0)
else:
     print("enter proper gear type")
year=int(input("Enter the year: "))     
h.append(year)
present_price=float(input("Enter the present price in lakhs(upto two decimal places: "))
h.append(present_price)
kms_driven=int(input("Enter the kilometers driven: "))
h.append(kms_driven)
y_pred2=regressor.predict([h])
print("The predicted price is : ",y_pred2,"lakhs")
from sklearn.metrics import mean_squared_error
print("Mean Squared Error: ",mean_squared_error(Y_test,y_pred))
print("Accuracy of the model: ",regressor.score(X_test,Y_test))


