import streamlit as st
import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
from PIL import Image
import os

MODEL_PATH = "mnist_cnn.h5"

def load_or_train_model():
    if os.path.exists(MODEL_PATH):
        model = tf.keras.models.load_model(MODEL_PATH)
    else:
        # Cargamos y preparamos MNIST
        (x_train, y_train), _ = tf.keras.datasets.mnist.load_data()
        x_train = x_train.astype("float32").reshape(-1,28,28,1) / 255.0
        y_train = y_train.astype("int32")

        # Definimos CNN sencilla
        model = models.Sequential([
            layers.Conv2D(32, (3,3), activation='relu', input_shape=(28,28,1)),
            layers.MaxPooling2D((2,2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(10, activation='softmax')
        ])
        model.compile(
            optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy']
        )

        # Entrenamos y guardamos
        model.fit(x_train, y_train, epochs=3, batch_size=64, verbose=0)
        model.save(MODEL_PATH)
    return model

model = load_or_train_model()

st.title("Clasificador de Dígitos MNIST con CNN")
st.write("Sube una imagen 28×28 en escala de grises; la CNN te dirá qué dígito es.")

uploaded = st.file_uploader("Selecciona una imagen (PNG/JPG)", type=["png","jpg","jpeg"])
if uploaded:
    
    # Preprocesamos la imagen
    img = Image.open(uploaded).convert("L").resize((28,28))
    st.image(img, caption="Imagen subida", width=150)
    x = np.array(img).astype("float32").reshape(1,28,28,1) / 255.0

    # Predecimos
    pred = model.predict(x)
    digit = int(np.argmax(pred, axis=1)[0])
    st.success(f"El modelo predice: **{digit}**")