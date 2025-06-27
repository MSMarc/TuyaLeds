# 🔌 Controlador Smart Plug Tuya

Permite controlar un enchufe inteligente compatible con Tuya directamente desde Python, **sin necesidad del software del fabricante ni de aplicaciones móviles**.
Ideal para automatizar el encendido/apagado del enchufe mediante el **Programador de tareas de Windows**, por ejemplo: al iniciar sesión, a una hora específica, o mediante un acceso directo.

---

## 🧩 Características

- ✅ Enciende o apaga el enchufe según su estado actual (toggle)
- 🔄 Se puede configurar para que siempre apague o siempre encienda
- ⚙️ Compatible con cualquier dispositivo Tuya local
- 🗓️ Pensado para ejecutarse con el Programador de Tareas de Windows

---

## ⚙️ Requisitos

- Python 3.6+
- Dispositivo Tuya configurado para control local
- Conocer DEVICE_ID, IP_ADDRESS y LOCAL_KEY

---

## 🛠 Instalación

1. Clona este repositorio o descarga el código.
   ```bash
   git clone https://github.com/MSMarc/TuyaLeds.git
2. Instala dependencias:
   ```bash
   pip install -r requirements.txt
3. Renombra el archivo `.env.example` como `.env` y cambia el DEVICE_ID, IP_ADDRESS y LOCAL_KEY según tu dispositivo.
4. Crear una tarea programada con el "Programador de tareas" de windows, que lance el script cuando te convenga. Mejor si usas un `.bat`.
5. Para probar mis tareas:
   - Cambiar el usuario (que viene en un ID raro llamado SID) por el tuyo.
   - Cambiar la ruta al script para que apunte donde lo tengas guardado en tu PC.

---

## 🧾 Créditos

[tinytuya](https://github.com/jasonacox/tinytuya)
