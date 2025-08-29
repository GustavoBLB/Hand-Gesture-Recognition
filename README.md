# GestureRecognizer — Reconhecimento de Gestos em LIBRAS

🌍 Disponível em: [English](README.en.md) | [Português](README.md)

**LIBRAS** (Língua Brasileira de Sinais) é a língua oficial de sinais usada no Brasil, reconhecida por lei e amplamente adotada para a comunicação pela comunidade surda.

Um protótipo compacto de ponta a ponta que **captura marcos da mão**, **treina um classificador** e **reconhece o alfabeto da LIBRAS em tempo real** através de uma interface desktop simples.

> **Status:** em desenvolvimento — atualmente reconhece **letras**; próximos marcos incluem **gestos/sinais completos** além do alfabeto.

---

## ✨ Funcionalidades
- **Captura** marcos da mão pela webcam (OpenCV + MediaPipe), salvando um **dataset em CSV** (x, y, z para 21 marcos).
- **Treina** um modelo **KNN** (scikit-learn) com acurácia, relatório de classificação e matriz de confusão.
- **Reconhece** letras em tempo real, sobrepondo a previsão no vídeo.
- **Interface Desktop (Tkinter)** com três ações: **Capturar**, **Treinar**, **Reconhecer**.

- **Comportamento de fallback**:
  - Se nenhum `database.csv` for encontrado, o treinamento usa automaticamente `examples/sample_database.csv`.
  - Se nenhum `model.pkl` for encontrado, o reconhecimento solicita que o usuário treine um modelo primeiro.

---

## 🎬 Demonstração

Confira o vídeo completo da demonstração no LinkedIn:

- [Assista à demo aqui](https://www.linkedin.com/seu-video-aqui)

---

## 🗂️ Estrutura do Projeto
    .
    ├─ main.py                   # Janela Tkinter que orquestra: Captura → Treina → Reconhece
    ├─ gesture_capture.py        # Abre a webcam, captura 21 marcos (x,y,z), adiciona linhas ao database.csv
    ├─ train_model.py            # Carrega CSV, treina KNN (scikit-learn), mostra métricas, salva model.pkl
    ├─ gesture_recognition.py    # Inferência ao vivo: desenha marcos e sobrepõe a letra prevista
    ├─ database.csv              # (auto-criado) Dataset de amostras rotuladas
    ├─ model.pkl                 # (auto-criado) Modelo KNN treinado
    ├─ examples/sample_database.csv  # Pequeno dataset de demonstração (usado se não houver database.csv)
    └─ requirements.txt          # Dependências fixadas para Python 3.10

### O que cada arquivo faz
- **main.py** — pequeno controlador (Tkinter) com 3 botões que executam os scripts abaixo.
- **gesture_capture.py** — teclas: `s` salva amostra, `m` entra em multi-salvamento (define o rótulo uma vez, depois pressione `s` repetidamente), `l` sai do multi-salvamento, `q` sai.
- **train_model.py** — separa treino/teste, treina **KNN (k=3)**, imprime **acurácia**, **relatório de classificação**, **matriz de confusão**, e salva **model.pkl**. Se nenhum `database.csv` for encontrado, usa `examples/sample_database.csv`.
- **gesture_recognition.py** — previsão em tempo real; se **probabilidade máxima < 0.9**, mostra **desconhecido** para evitar palpites superconfiantes. Se nenhum `model.pkl` for encontrado, solicita ao usuário treinar o modelo primeiro.

---

## 🧰 Stack Tecnológico
- **Python 3.10** 
- **OpenCV**
- **MediaPipe Hands**
- **NumPy / Pandas**
- **scikit-learn (KNN)**
- **Joblib**
- **Tkinter**

---

## ⚙️ Instalação (Python 3.10 + ambiente virtual)

O MediaPipe nem sempre suporta as versões mais recentes do Python. Use **Python 3.10** em um ambiente virtual para evitar problemas.

### 1) Instalar Python 3.10
- baixe a versão 3.10.x de python.org (marque “Add Python to PATH” durante a instalação).

### 2) Criar e ativar um ambiente virtual

**Windows (PowerShell)**
    py -3.10 -m venv .venv
    .\.venv\Scripts\Activate.ps1
    python -m pip install --upgrade pip

**macOS / Linux**
    python3.10 -m venv .venv
    source .venv/bin/activate
    python -m pip install --upgrade pip

### 3) Instalar dependências

Com o arquivo requirements.txt já incluso no projeto, instale tudo executando:
    pip install -r requirements.txt

### 4) Rodar o app
    python main.py

---

### Início rápido com dataset de demonstração
Se quiser apenas testar sem capturar novos gestos:
1. Execute `train_model.py` → usará `examples/sample_database.csv` se não existir `database.csv`.
2. Execute `gesture_recognition.py` → pedirá `model.pkl`; se não existir, `train_model.py` deve ser executado primeiro.

---

**Dicas**
- Se a câmera no índice 0 falhar, altere `cv2.VideoCapture(0)` para `cv2.VideoCapture(1)` (ou 2, …).
- Na captura: `s` salva, `m` habilita multi-salvamento (define rótulo uma vez), `l` sai do multi-salvamento, `q` fecha.

---

## 🧭 Roadmap
- [ ] Adicionar reconhecimento de **gestos/sinais completos** (além das letras)
- [ ] Melhorar ferramentas de dataset (balanceamento, aumento de dados)
- [ ] Exportar/importar datasets e modelos via interface

---

## 🤝 Agradecimentos
- [MediaPipe Hands](https://developers.google.com/mediapipe)
- [scikit-learn](https://scikit-learn.org/)
