# 🛒 Product Price Tracker API

Una API desarrollada en Python con **FastAPI** para hacer seguimiento de precios de productos. Ideal como base para construir microservicios modernos y escalables.

---

## 🚀 Características

- 🔧 **FastAPI** como framework principal
- 🐳 Contenedores con **Docker** y `docker-compose`
- 🔁 **Reload automático** en modo desarrollo
- 📄 **Logs persistentes** en archivo local dentro del contenedor
- 📣 **Notificaciones automáticas a Discord** en errores críticos
- 📦 Variables de entorno centralizadas en archivo `.env`
- 🌐 API REST lista para despliegue en producción

---

## 🧱 Estructura del Proyecto
```
product-price-tracker/
├── app/
│ ├── main.py # Punto de entrada de la API
│ ├── config.py # Configuración con Pydantic
│ ├── logging_config.py # Configuración de logs
│ ├── exception_handlers.py # Manejo de errores globales
│ └── ...
├── logs/ # Carpeta de logs persistentes
├── Dockerfile # Imagen de Docker base
├── docker-compose.yml # Configuración de servicios
├── .env # Variables de entorno
├── requirements.txt # Dependencias
└── README.md # Documentación
```
## ⚙️ Variables de Entorno

Crea un archivo `.env` en la raíz con:

```env
APP_ENV=development
PORT=8000
DISCORD_WEBHOOK_URL=https://discord.com/api/webhooks/.
```

## 🐳 Uso con Docker
```
docker-compose up --build
```
Esto levantará el servidor en http://localhost:8000 con autoreload y bind al puerto definido en .env.


📄 Logs Persistentes

Todos los logs se guardan en la carpeta /logs dentro del contenedor y se montan localmente.
El nombre del archivo incluye la fecha: logs/app_YYYY-MM-DD.log.

Manejo de Errores
La API incluye un manejador global de errores:

Captura excepciones no controladas

Escribe en el log con logger.error(...)

Envía notificaciones a Discord (si se configura DISCORD_WEBHOOK_URL)

Ejemplo de error:
```error
GET /error
```
Respuesta:
```
{
  "detail": "Error interno del servidor"
}
```
🧪 Probar
Abrir en navegador: http://localhost:8000/

Probar error: http://localhost:8000/error

Revisar logs: logs/app_YYYY-MM-DD.log

Verificar notificación en canal de Discord

✅ Requisitos
Python 3.11

Docker & Docker Compose

Cuenta de Discord para configurar un webhook (opcional)
