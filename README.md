<p align="center">
  <img src="https://www.iudigital.edu.co/images/11.-IU-DIGITAL.png" alt="IU Digital" width="350">
</p>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/2/27/MnistExamples.png" alt="MNIST" width="350">
</p>

<p align="center">
  🚀 Aplicación desplegada:  
  <a href="https://tu-usuario-tu-app.streamlit.app/" target="_blank">
    https://mnist-cnn-app.streamlit.app
  </a>
</p>

# 📊 Clasificador de Dígitos Manuscritos (MNIST) con CNN

Este repositorio contiene una **aplicación web** en **Streamlit** que permite subir una imagen de un dígito manuscrito (28×28 en escala de grises) y recibe como respuesta la predicción del dígito (0–9) utilizando una **red neuronal convolucional (CNN)** entrenada con **TensorFlow / Keras**.

---

## 📋 Contenido

* 📖 [Descripción](#-descripción)
* 🛠️ [Tecnologías y Dependencias](#️-tecnologías-y-dependencias)
* 🚀 [Instalación](#-instalación)
* ▶️ [Uso](#️-uso)
* 🔍 [Cómo Funciona](#-cómo-funciona)
* 📂 [Estructura del Proyecto](#-estructura-del-proyecto)
* 🧠 [Arquitectura CNN](#-arquitectura-cnn)
* 📈 [Resultados](#-resultados)

---

## 📖 Descripción

La aplicación carga un modelo CNN (o lo entrena localmente si no existe aún) que clasifica imágenes del dataset MNIST. El usuario sube una foto (PNG/JPG), el sistema la preprocesa y devuelve la predicción del dígito manuscrito en tiempo real.

---

## 🛠️ Tecnologías y Dependencias

* **Python 3.8+**
* **Streamlit** – Interfaz web rápida
* **TensorFlow / Keras** – Definición, entrenamiento y carga del modelo CNN
* **Pillow** – Lectura y procesamiento de imágenes
* **NumPy** – Manipulación de arreglos y datos numéricos

Instala todo con:

```bash
pip install -r requirements.txt
```

---

## 🚀 Instalación

1. **Clona el repositorio**

   ```bash
   https://github.com/Alexis-Machado/mnist-cnn-streamlit.git
   ```

2. **Crea y activa un entorno virtual** (opcional pero recomendado)

   ```bash
   python -m venv venv
   # Linux/Mac
   source venv/bin/activate
   # Windows
   venv\Scripts\activate
   ```

3. **Instala las dependencias**

   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Uso

Ejecuta la aplicación localmente:

```bash
streamlit run app.py
```

* Abre tu navegador en `http://localhost:8501`.
* Sube una imagen (PNG/JPG) de 28×28 px en escala de grises.
* Obtén la predicción del dígito.

---

## 🔍 Cómo Funciona

1. **Carga o Entrena**

   * Si existe `mnist_cnn.h5`, se carga el modelo guardado.
   * Si no, entrena un modelo CNN sencillo 3 épocas sobre MNIST y lo guarda.

2. **Preprocesamiento**

   * La imagen subida se convierte a escala de grises, se redimensiona a 28×28 y se normaliza (0–1).

3. **Predicción**

   * Se hace `model.predict()` y se extrae el dígito con `argmax`.

4. **Interfaz**

   * Streamlit muestra la imagen y la etiqueta predicha al usuario.

---

## 📂 Estructura del Proyecto

```bash
mnist-cnn-streamlit/
├── app.py               # Código principal de Streamlit
├── mnist_cnn.h5         # Modelo CNN guardado (se genera tras el primer entrenamiento)
├── requirements.txt     # Dependencias
└── README.md            # Documentación
```

---

## 🧠 Arquitectura CNN

El modelo utilizado es muy sencillo:

```
Entrada: 28×28×1 (imagen MNIST)
↓ Conv2D(32 filtros, 3×3) + ReLU
↓ MaxPooling2D(2×2)
↓ Flatten → vector 5408
↓ Dense(128 neuronas) + ReLU
↓ Dense(10 neuronas) + Softmax
↓ Salida: vector de probabilidades (10 clases)
```

---

## 📈 Resultados

* **Precisión en test**: \~98.7 %
* **Ventajas**:

  * Rapidez de desarrollo con Keras/Streamlit.
  * Buena generalización gracias a las convoluciones.
* **Observaciones**:

  * Se puede mejorar con más épocas, data augmentation o capas adicionales.

---

¡Listo para reconocer dígitos manuscritos al instante! 🚀
