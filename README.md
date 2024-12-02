# Bot de Telegram - ¡Ubicación Maestra!

Este proyecto es un bot de Telegram que permite vincular usuarios mediante un `user_id` con una base de datos de Firebase. Una vez vinculados, los usuarios recibirán notificaciones y alertas relacionadas con la aplicación.

## Características
- Responde al comando `/start` para iniciar la vinculación de cuentas.
- Vincula el `chat_id` de Telegram con un `user_id` almacenado en Firebase.
- Proporciona notificaciones a los usuarios vinculados.

## Configuración

### Requisitos
1. **Python 3.7 o superior.**
2. **Credenciales válidas de Firebase.** El archivo JSON con las credenciales de tu base de datos debe ser descargado desde tu consola de Firebase.
3. **Token del bot de Telegram.** Obtenido desde [BotFather](https://core.telegram.org/bots#botfather).

### Estos valores tienen que ser reemplazados por unos validos.

TOKEN = config("TELEGRAM_TOKEN")

cred = credentials.Certificate(config("FIREBASE_CREDENTIALS"))

### Y DESCARGAR LAS CREDENCIALES:
appubicacion-firebase-adminsdk.json
