import tkinter as tk
from tkinter import messagebox, ttk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib
import threading

def show_results_window(text: str):
    win = tk.Toplevel(janela)
    win.title("Training Results")
    win.geometry("700x500")

    frm = tk.Frame(win)
    frm.pack(fill="both", expand=True, padx=10, pady=10)

    txt = tk.Text(frm, wrap="none", font=("Consolas", 10))
    txt.insert("1.0", text)
    txt.config(state="disabled")  # read-only
    txt.pack(side="left", fill="both", expand=True)

    yscroll = tk.Scrollbar(frm, orient="vertical", command=txt.yview)
    yscroll.pack(side="right", fill="y")
    txt.config(yscrollcommand=yscroll.set)

def train_model():

    data_csv = pd.read_csv("database.csv")

    coordinates_csv = data_csv.drop("label", axis=1)  
    labels_csv = data_csv["label"]

    coordinates_csv_train, coordinates_csv_test, labels_csv_train, labels_csv_test = train_test_split(coordinates_csv, labels_csv, test_size=0.2, random_state=42)

    model = KNeighborsClassifier(n_neighbors=3)
    model.fit(coordinates_csv_train, labels_csv_train) 

    labels_csv_pred = model.predict(coordinates_csv_test)

    accuracy = accuracy_score(labels_csv_test, labels_csv_pred) * 100
    classification = classification_report(labels_csv_test, labels_csv_pred)

    labels_order = sorted(pd.unique(pd.concat([labels_csv_test, pd.Series(labels_csv_pred)])))
    cm = confusion_matrix(labels_csv_test, labels_csv_pred, labels=labels_order)
    cm_df = pd.DataFrame(cm, index=[f"true_{l}" for l in labels_order],
                         columns=[f"pred_{l}" for l in labels_order])

    joblib.dump(model, "model.pkl")

    result_text =   (
                        f"Model saved as model.pkl\n\n"
                        f"Accuracy: {accuracy:.2f}%\n\n"
                        f"Classification report:\n{classification}\n"
                        f"Confusion matrix:\n{cm_df.to_string()}\n"
                    )

    def finish_ui():
        progress.stop()
        progress.pack_forget()
        status_label.config(text=f"Training finished!")
        show_results_window(result_text)

    janela.after(0, finish_ui)


def start_training():
    botao_treinar.config(state='disabled')
    status_label.config(text=f"Training model...")
    progress.pack(pady=6)
    progress.start(10) 
    threading.Thread(target=train_model).start()


janela = tk.Tk()
janela.title("Model Training")
janela.geometry("480x260")

status_label = tk.Label(janela, text="Click the button to train the model.")
status_label.pack(pady=10)

progress = ttk.Progressbar(janela, mode="indeterminate", length=260)

botao_treinar = ttk.Button(janela, text="Train Model", command=start_training)
botao_treinar.pack(pady=8)

janela.mainloop()

