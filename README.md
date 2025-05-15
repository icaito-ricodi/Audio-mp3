# Text-to-Speech App

https://form-icaito.onrender.com
https://forms.gle/BDHXrtLWut9Uy8Qe8

Esta es una sencilla aplicación en Python que convierte un texto dado en un archivo de audio (formato MP3). Utiliza la librería `gTTS` (Google Text-to-Speech) para realizar la síntesis de voz.

## Adjunto archivo

Copiar Ctrl+C y Pega en tu Navegador C:\Users\PC\Downloads\Todas Descargas\python\texto.mp3

## Cómo usar

1.  Asegúrate de tener Python instalado en tu sistema.
2.  Instala la librería `gTTS` si aún no la tienes. Puedes hacerlo usando pip:
    ```bash
    pip install gTTS
    ```
3.  Guarda el código Python que proporcionaste en un archivo, por ejemplo, `texto_a_audio.py`.
4.  Ejecuta el script desde tu terminal:
    ```bash
    python texto_a_audio.py
    ```
5.  Se generará un archivo de audio llamado `texto.mp3` en el mismo directorio. La aplicación intentará abrir automáticamente este archivo para que lo escuches.

## Dependencias

* [gTTS](https://pypi.org/project/gTTS/): Librería de Google Text-to-Speech.

## Notas

* El texto que se convertirá a voz está definido directamente en el script (`text = "..."`). Para convertir otro texto, simplemente modifica el valor de esta variable.
* El idioma de la voz se define con la variable `language` (actualmente configurado en español de Estados Unidos: `"es-us"`). Puedes cambiar esto a otros códigos de idioma soportados por `gTTS`.
* El código incluye comentarios de otras librerías (`playsound`, `pyttsx3`) que también se utilizan para la funcionalidad de texto a voz, aunque en este script actual se está utilizando `gTTS`.
