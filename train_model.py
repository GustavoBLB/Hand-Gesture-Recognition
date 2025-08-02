import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

data_csv = pd.read_csv("database.csv")

coordinates_csv = data_csv.drop("label", axis=1)  
labels_csv = data_csv["label"]

coordinates_csv_train, coordinates_csv_test, labels_csv_train, labels_csv_test = train_test_split(coordinates_csv, labels_csv, test_size=0.2, random_state=42)

model = KNeighborsClassifier(n_neighbors=3)
model.fit(coordinates_csv_train, labels_csv_train) 

# 6. Avaliar o modelo com os dados de teste
labels_csv_pred = model.predict(coordinates_csv_test)

print("Acurácia:", accuracy_score(labels_csv_test, labels_csv_pred) * 100, "%")
print("Relatório de classificação:\n", classification_report(labels_csv_test, labels_csv_pred))
print("Matriz de confusão:\n", confusion_matrix(labels_csv_test, labels_csv_pred))

# # # 7. Salvar o modelo treinado para uso posterior
joblib.dump(model, "model.pkl")
print("Modelo salvo com sucesso como model.pkl")
