from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import firebase_admin
from firebase_admin import credentials, firestore

# Configuración de Firebase
cred = credentials.Certificate("appubicacion-419723-firebase-adminsdk-2gcz2-d91f7c63ac.json")
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)
db = firestore.client()

TOKEN = "6861684395:AAHvcC2wktHTsjL1104a7AoM88A6I74yS3E"

# Función que maneja el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Obtenemos el chat_id del usuario que inició la conversación
    chat_id = update.message.chat_id
    
    # Pedir al usuario su user_id para vincular su cuenta
    await update.message.reply_text("Bienvenido al bot !Ubicación Maestra!")
    await update.message.reply_text("Por favor, ingresa tu user_id para vincular tu cuenta.")
    
    # Guardar temporalmente el chat_id en el contexto de usuario
    context.user_data['chat_id'] = chat_id


# Función para guardar el user_id y chat_id en Firebase
async def save_user_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Este método se activa cuando el usuario envía su user_id
    user_id = update.message.text
    chat_id = context.user_data.get('chat_id')

    if chat_id:
        try:
            # Intentamos obtener el documento del usuario con el user_id proporcionado
            user_ref = db.collection('users').document(user_id)

            # Verificamos si el user_id existe en la base de datos
            doc = user_ref.get()

            if doc.exists:
                # Actualizamos el campo chat_id en el documento del usuario
                user_ref.update({'chat_id': chat_id})
                await update.message.reply_text(f"Su cuenta fue vinculada con éxito !! ")
                await update.message.reply_text(f"Desde ahora recibira alertas sobre lo que ocurra en la aplicación!")

                # Borrar el mensaje del user_id enviado por el usuario
                await update.message.delete()

            else:
                await update.message.reply_text("No se encontró una cuenta con ese user_id.")
                await update.message.reply_text("Asegurese de pegar bien el codigo proporcionado.")
        except Exception as e:
            await update.message.reply_text(f"Ocurrió un error al intentar vincular la cuenta: {str(e)}")
    else:
        await update.message.reply_text("Error: No se encontró un chat_id.")

# Configuramos el bot y sus handlers
def main():
    # Construimos la aplicación del bot con el token
    application = ApplicationBuilder().token(TOKEN).build()

    # Añadimos los manejadores de comandos y mensajes
    application.add_handler(CommandHandler("start", start))
    # MessageHandler para capturar el user_id proporcionado por el usuario después del comando /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_user_id))

    # Ejecuta el bot con `run_polling()` que maneja todo el ciclo de vida
    application.run_polling()

if __name__ == '__main__':
    main()