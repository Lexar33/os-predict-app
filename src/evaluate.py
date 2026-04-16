# Código de Evaluación - Modelo de Riesgo de Default en un Banco de Corea
############################################################################

import pandas as pd
import pickle
from sklearn import metrics
from sklearn.metrics import (
    confusion_matrix,
    accuracy_score,
    precision_score,
    recall_score,
    classification_report
)
import os
def eval_model(filename):
    current_dir = os.path.dirname(__file__)
    df=pd.read_csv(os.path.join(current_dir,"..","data","processed", filename))
    X_val = df.drop(["clase"], axis=1)
    X_val.columns.values[0] = "ID"
    print(X_val)
    X_val=X_val.drop(["ID"],axis=1)
    y_val= df[["clase"]]
    current_dir = os.path.dirname(__file__)
    package = os.path.join(current_dir,"..","models","best_model.pkl")
    model = pickle.load(open(package, "rb"))
    
    y_pred_val = model.predict(X_val)

    cm_test = confusion_matrix(y_val, y_pred_val)
    print("Matriz de confusion: ")
    print(cm_test)
    cm_metrics= metrics.classification_report(y_val,y_pred_val)
    print("Metricas")
    print(cm_metrics)
    #accuracy_test = accuracy_score(y_val, y_pred_val)
    #print("Accuracy: ", accuracy_test)
    #precision_test = precision_score(y_val, y_pred_val)
    #print("Precision: ", precision_test)
    #recall_test = recall_score(y_val, y_pred_val)
    #print("Recall: ", recall_test)

# Validación desde el inicio
def main():
    eval_model("data_val.csv")
    print("Finalizó la validación del Modelo")


if __name__ == "__main__":
    main()
