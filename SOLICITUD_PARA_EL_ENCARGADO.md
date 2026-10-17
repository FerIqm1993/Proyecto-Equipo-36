# 📩 Solicitud de Configuración: Google Sheets & Google Cloud Service Account

> **Para:** Encargado / Administrador de Infraestructura de CommunityLab  
> **De:** Equipo de Desarrollo / Curaduría CommunityLab  
> **Objetivo:** Conectar el Dashboard interactivo de Curaduría (Streamlit) con Google Sheets y el pipeline de automatización en n8n y Oracle Cloud (OCI).

---

Hola 👋,

Para poner en funcionamiento la estación de curaduría humana y permitir que el dashboard lea las propuestas generadas por IA y guarde las decisiones en Google Sheets, requerimos que nos facilites **2 elementos**:

1. **Una hoja de Google Sheets** con la pestaña llamada `Curaduria`, cargada con la plantilla oficial.
2. **Las credenciales de una Cuenta de Servicio de Google Cloud (Service Account)** con permisos de Editor sobre la hoja.

A continuación tienes los pasos exactos para crearlo en menos de 5 minutos:

---

## 📄 Paso 1: Crear la Hoja de Google Sheets (30 segundos)

1. Abre [Google Sheets](https://sheets.new) y crea una nueva hoja de cálculo.
2. Renómbrala como: **`CommunityLab - Curaduria`** (o el nombre que prefieras).
3. Asegúrate de que la pestaña inferior se llame exactamente: **`Curaduria`** *(sin acento)*.
4. Ve a **Archivo > Importar > Subir** y sube el archivo adjunto:
   👉 **`PLANTILLA_GOOGLE_SHEETS_CURADURIA.csv`**
5. En la ventana de importación, selecciona:
   - *Ubicación de importación:* **Reemplazar la hoja actual**.
   - Haz clic en **Importar datos**.
6. Copia el **ID de la hoja** desde la barra de direcciones de tu navegador:
   > URL: `https://docs.google.com/spreadsheets/d/`**`1nY40IJ4ludaHQcTEV8nDlHNi6ikl-4x5CUJocvrsHfk`**`/edit`  
   > *(La parte alfanumérica entre `/d/` y `/edit` es el ID)*.

---

## 🔑 Paso 2: Crear la Service Account en Google Cloud (3 minutos)

1. Ingresa a la consola de [Google Cloud Console](https://console.cloud.google.com/) y selecciona tu proyecto.
2. **Habilitar APIs requeridas:**
   - Ve a **APIs y servicios > Biblioteca**.
   - Busca **Google Sheets API** y haz clic en **Habilitar**.
   - Busca **Google Drive API** y haz clic en **Habilitar**.
3. **Crear la Cuenta de Servicio:**
   - Ve a **IAM y administración > Cuentas de servicio**.
   - Haz clic en **+ Crear cuenta de servicio**.
   - Nombre: `communitylab-curador`
   - Haz clic en **Crear y continuar** y luego en **Listo** (no se requieren roles especiales en el proyecto).
4. **Generar la Llave JSON:**
   - En la lista de cuentas de servicio, haz clic sobre el correo de la cuenta recién creada (ej: `communitylab-curador@tu-proyecto.iam.gserviceaccount.com`).
   - Ve a la pestaña **Claves (Keys)**.
   - Haz clic en **Agregar clave > Crear clave nueva**.
   - Selecciona el formato **JSON** y haz clic en **Crear**.
   - Se descargará automáticamente un archivo `.json` en tu equipo (ej: `tu-proyecto-a1b2c3d4e5f6.json`).

---

## 🤝 Paso 3: Compartir la Hoja con la Cuenta de Servicio (30 segundos)

1. Vuelve a la hoja de Google Sheets que creaste en el **Paso 1**.
2. Haz clic en el botón azul **Compartir** (arriba a la derecha).
3. Pega el correo del Service Account:
   > `communitylab-curador@tu-proyecto.iam.gserviceaccount.com`
4. Asígnale el rol de **Editor**.
5. Desmarca la casilla "Notificar a los usuarios" y haz clic en **Guardar / Compartir**.

---

## 📦 ¿Qué debes entregarnos de vuelta?

Elige la opción que te resulte más cómoda:

### ⭐ Opción A (La más rápida y recomendada):
Simplemente entréganos:
1. El archivo **`.json`** que se descargó de Google Cloud (ej: `service_account.json`).
2. El **enlace o ID** de la hoja de Google Sheets.

> *(Nosotros ejecutaremos nuestro asistente automatizado `configurar_secrets.py` que genera la configuración al instante).*

---

### 📝 Opción B (Rellenar la plantilla directamente):
Abre el archivo adjunto **`SECRETS_TEMPLATE.toml`** o [`.streamlit/secrets.toml.example`](file:///c:/projects/proyecto-36/.streamlit/secrets.toml.example), pega los valores correspondientes del archivo JSON y el ID del Sheet, y devuélvenos el archivo guardado como **`secrets.toml`**.

---

¡Muchas gracias! Con esto el módulo de curaduría quedará 100% operativo tanto en desarrollo local como en el despliegue de Streamlit Cloud.
