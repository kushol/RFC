# import bottle
from bottle import Bottle, route, post, run, request, template, static_file
from ClassifierWebTemplates import root_template, result_template

# import sklearn modules
from sklearn import tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# import all other necessary modules
import pandas as pd
import sys


# initialize bottle
app = Bottle()


# define folder path for static files
@app.route('/static/<filename:path>', name='static')
def serve_static(filename):
    return static_file(filename, root='static')


# route to the home page
@app.route('/')
def root():
    return root_template


# route to the result page (after applying classifier)
@app.post('/')
def do_upload():
    data = request.files.get('data')

    # check if file uploaded
    if data is not None:        
        filename = data.filename

        # handle exception if cannot read file  successfully (empty file, bad format)
        try:
            df_data = pd.read_csv(filename)
        except:
            print("Unexpected error:", sys.exc_info()[0])
            return root()

        # remove null values
        df_data = clean_dataset(df_data)

        # process data and split
        df_X, df_y, features, targets = process_data(df_data)        
        X_train, X_test, y_train, y_test = train_test_split(df_X, df_y, test_size = 0.2, random_state = 1)

        # initialize and train the model
        model = RandomForestClassifier(n_estimators=10)
        model.fit(X_train, y_train)
        y_predicted = model.predict(X_test)
        model_accuracy = metrics.accuracy_score(y_test, y_predicted)

        # generate trees to view
        result_tree_text = generate_tree(model, df_data.columns[:-1])
             
        return template(result_template,
                        file_name = filename,
                        data_count = len(df_data.index),
                        features = features,
                        targets = targets,
                        accuracy=round(model_accuracy, 2),
                        result_trees=result_tree_text)
    
    return "You missed a field."


# process data: data, target, feature names, target names
def process_data(df_data):
    cols = df_data.columns
    cols_X = cols[:-1]
    col_y = cols[-1]
    df_X = df_data[[]]
    features = ''

    # separate data from target and populate feature names string
    for col in cols_X:
        df_X = pd.concat([df_X, pd.get_dummies(df_data[[col]])], axis=1)
        if len(features) > 0:
            features = features + ', '            
        features = features + col
    df_y = df_data[col_y]

    return df_X, df_y, features, cols[-1]

# generate all trees from model estimators
def generate_tree(model, cols_X):
    result_tree_text = ""
    for ti, est in enumerate(model.estimators_):
        result_tree_text = result_tree_text + "<div style='background-color:Orange;width:100%;'>Tree: " + str(ti+1) + "</div><br />"
        result_tree_text = result_tree_text + tree.export_text(est)
        result_tree_text = result_tree_text.replace("\n", "<br />")

        # place actual feature names
        for i, col in enumerate(cols_X):
            result_tree_text = result_tree_text.replace("feature_" + str(i), col)

        # place actual target names
        for i, cls in enumerate(model.classes_):
            result_tree_text = result_tree_text.replace("class: " + str(i+0.0), "class: " + str(cls))
      
        result_tree_text = result_tree_text + "<br /><br />"

    return result_tree_text

# clean data: remove all rows that contain null values
def clean_dataset(data):
    for x in data.columns:
        data.dropna(subset=[x], inplace=True)

    return data


# main function
if __name__ == "__main__":
    # Run the web application
    run(app, host='localhost', port=8080)
