#Import scikit-learn dataset library
import sklearn
from sklearn import datasets
from sklearn.model_selection import train_test_split
import pandas as pd
#Import svm model
from sklearn import svm
from sklearn import metrics

# Used to save and load the model
import pickle


def generate_save_model():
    scikit_ver = sklearn.__version__
    print(scikit_ver)
    #Load dataset
    dryness = pd.read_csv('Filtered.csv', delimiter=',')
    x = dryness[['temp', 'humidity', 'fan_speed','elapsed_time']]
    y = dryness['is_dry']

    # Split dataset into training set and test set
    X_train, X_test, y_train, y_test = train_test_split(x,y,  test_size=0.3,random_state=109) # 70% training and 30% test

    #Create a svm Classifier
    clf = svm.SVC(kernel='linear') # Linear Kernel

    #Train the model using the training sets
    clf.fit(X_train, y_train)

    #Predict the response for test dataset
    y_pred = clf.predict(X_test)

    # Model Accuracy: how often is the classifier correct?
    print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

    # Model Precision: what percentage of positive tuples are labeled as such?
    print("Precision:",metrics.precision_score(y_test, y_pred))

    # Model Recall: what percentage of positive tuples are labelled as such?
    print("Recall:",metrics.recall_score(y_test, y_pred))

    print("Saving model...")

    # Save the model
    with open('model_svm_' + scikit_ver, 'wb') as f:
        pickle.dump(clf, f)
    
    print("Model saved successfully!")


def prediction(data):
    # Convert dictionary key-value pair to dataframe
    df = pd.DataFrame(data)

    # Open the saved model
    with open('model_svm_0.24.2', 'rb') as f:
        model = pickle.load(f)
    
    # Predict the dryness label
    y_pred = model.predict(df)

    return y_pred


# generate_save_model()
data = {'temp': [30], 'humidity': [70], 'fan_speed':[0], 'elapsed_time':1500}
data_two = {'temp': [64], 'humidity': [3], 'fan_speed':[1], 'elapsed_time':200}
print((prediction(data))[0])
print((prediction(data_two))[0])

