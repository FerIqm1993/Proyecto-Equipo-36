# 🛡️ Guía de Integración y Faltantes: Módulo de Curaduría (Streamlit)

> **Proyecto:** CommunityLab — Hackathon ONE G10 (Oracle & Alura) · **Equipo 36**  
> **Repositorio Base:** [Proyecto-Equipo-36 (FerIqm1993)](https://github.com/FerIqm1993/Proyecto-Equipo-36.git)  
> **Repositorio de Curaduría:** [G10-LATAM-EQUIPO-36 (VelaztiquiOscar)](https://github.com/VelaztiquiOscar/G10-LATAM-EQUIPO-36.git)  
> **Despliegue en Vivo:** [https://g10-latam-equipo-36.streamlit.app/](https://g10-latam-equipo-36.streamlit.app/)

---

## 📋 1. Resumen de la Integración Realizada

Se ha transferido e implementado exitosamente la arquitectura completa de curaduría del repositorio de Oscar (`VelaztiquiOscar/G10-LATAM-EQUIPO-36`) dentro del repositorio principal (`Proyecto-Equipo-36`).

### Archivos integrados y actualizados en el proyecto:

1. **`app.py` (Raíz del proyecto):**
   - Se reemplazó el archivo previo (mock estático de 63 líneas) por la aplicación **Streamlit de Curaduría v2.1** completa.
   - Conexión nativa con **Google Sheets** mediante `gspread` y cuentas de servicio GCP (`google.oauth2.service_account.Credentials`).
   - Sistema de métricas en tiempo real (Total, Pendientes, Aprobados, Rechazados, En OCI).
   - Filtros dinámicos por estado, ejecución (batch de WF1), tipo de activo y score mínimo.
   - Tarjetas de activos con etiquetas por canal (LinkedIn `#0A66C2`, FAQ `#2E7D32`, Newsletter `#E65100`).
   - Edición de copy en línea antes de aprobar, persistencia de comentarios de auditoría humana y nombre del curador.
   - **Compatibilidad dual de encabezados:** Se garantizó que funcione tanto con `decision_at`/`comentario` como con `timestamp_decision`/`comentario_humano`.
   - Orden de escritura atómico a prueba de condiciones de carrera con el workflow de n8n (el campo disparador `decision` se escribe al final).

2. **`communitylab/dashboard/dashboard_curaduria.py`:**
   - Sincronizado exactamente con la misma lógica robusta para mantener consistencia modular si se ejecuta desde la subcarpeta.

3. **`requirements.txt` (Raíz del proyecto):**
   - Actualizado con las dependencias requeridas para producción:
     ```text
     streamlit>=1.30.0
     pandas>=2.0.0
     gspread>=6.0.0
     google-auth>=2.20.0
     boto3>=1.34.0
     ```

4. **`.devcontainer/devcontainer.json`:**
   - Creado a partir del repositorio de Oscar para permitir desarrollo inmediato en VS Code Dev Containers y GitHub Codespaces con arranque automático de Streamlit en el puerto `8501`.

5. **`.streamlit/secrets.toml.example` y `.streamlit/config.toml`:**
   - Creados en la raíz para proporcionar la plantilla de credenciales y el tema visual oscuro glassmorphism optimizado.

6. **`index.html` y `README.md`:**
   - Se agregaron accesos directos al despliegue activo en la nube: `https://g10-latam-equipo-36.streamlit.app/`.

---

## 🔍 2. Diagnóstico: ¿Por qué ya corre en Streamlit Cloud y qué falta para correr en local o en un nuevo despliegue?

La aplicación **ya está corriendo correctamente** en [https://g10-latam-equipo-36.streamlit.app/](https://g10-latam-equipo-36.streamlit.app/) porque el desarrollador Oscar configuró los secretos de Google Cloud directamente dentro del panel de **Streamlit Community Cloud** (`App Settings > Secrets`).

Por motivos estrictos de seguridad, los archivos de secretos (`secrets.toml`, credenciales JSON de GCP) están excluidos en `.gitignore` y **nunca deben subirse al repositorio público de GitHub**.

Por lo tanto, para ejecutar la aplicación en un entorno local, en otra máquina o si se desea clonar el despliegue en otra cuenta de Streamlit Cloud, se requieren los siguientes componentes detallados a continuación.

---

## 🛠️ 3. Lista de Faltantes y Configuración Paso a Paso

### 🔴 Faltante 1: Credenciales de Google Cloud (`.streamlit/secrets.toml`)

Para que la aplicación pueda leer y escribir en Google Sheets, necesita autenticarse mediante una **Cuenta de Servicio (Service Account)** de Google Cloud.

#### Pasos para resolverlo:
1. En la raíz de tu proyecto, copia la plantilla de secretos:
   ```powershell
   copy .streamlit\secrets.toml.example .streamlit\secrets.toml
   ```
2. Abre `.streamlit/secrets.toml` con tu editor.
3. Rellena los valores con los datos de tu cuenta de servicio de GCP:
   ```toml
   [gcp_service_account]
   type = "service_account"
   project_id = "tu-proyecto-gcp"
   private_key_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
   private_key = "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQC...\n-----END PRIVATE KEY-----\n"
   client_email = "communitylab-curador@tu-proyecto-gcp.iam.gserviceaccount.com"
   client_id = "109876543210987654321"
   auth_uri = "https://accounts.google.com/o/oauth2/auth"
   token_uri = "https://oauth2.googleapis.com/token"
   auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
   client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/communitylab-curador%40tu-proyecto-gcp.iam.gserviceaccount.com"

   # ID del documento de Google Sheets
   spreadsheet_id = "TU_SPREADSHEET_ID_AQUI"

   # Nombre exacto de la pestaña donde se alojan los activos
   worksheet_name = "Curaduria"
   ```

> [!IMPORTANT]
> En la clave `private_key`, asegúrate de mantener los saltos de línea codificados como `\n` entre comillas dobles.

---

### 🔴 Faltante 2: Compartir el Google Sheet con la Cuenta de Servicio

Aunque tengas el archivo de secretos, Google Sheets rechazará la conexión con error `403 Forbidden` o `SpreadsheetNotFound` si la hoja no ha sido compartida con el correo del Service Account.

#### Pasos para resolverlo:
1. Abre tu Google Sheet en el navegador:  
   `https://docs.google.com/spreadsheets/d/<SPREADSHEET_ID>/edit`
2. Haz clic en el botón azul **Compartir** (esquina superior derecha).
3. En el campo de invitación, escribe el correo exacto de tu Service Account (campo `client_email` de tu `secrets.toml`):  
   Ejemplo: `communitylab-curador@tu-proyecto-gcp.iam.gserviceaccount.com`
4. Asígnale el rol de **Editor** (indispensable para permitir la escritura de aprobaciones y rechazos).
5. Desmarca "Notificar a los usuarios" y haz clic en **Guardar / Compartir**.

---

### 🔴 Faltante 3: Estructura de la Pestaña `Curaduria` en Google Sheets

La pestaña de la hoja de cálculo debe llamarse exactamente **`Curaduria`** (respetando mayúsculas y sin acento, tal como está definido en los flujos de n8n y en `secrets.toml`).

#### Encabezados obligatorios de la fila 1:
Asegúrate de que la fila 1 de la pestaña `Curaduria` contenga los siguientes nombres de columna:

| Columna | Propósito | Quién la escribe |
| :--- | :--- | :--- |
| `execution_id` | Identificador de lote (ej: `CL-20261014-101`) | n8n (WF1) |
| `interaction_id` | ID de la interacción original (ej: `int-001`) | n8n (WF1) |
| `asset_id` | ID del activo (ej: `asset-001-li`) | n8n (WF1) |
| `canal` | Canal de origen (ej: `#logros-y-empleos`) | n8n (WF1) |
| `autor` | Nombre del usuario (ej: `Mariana Souza`) | n8n (WF1) |
| `tipo_activo` | Formato (`linkedin`, `faq`, `newsletter`) | n8n (WF1) |
| `score_final` | Puntuación numérica determinística (0 - 10) | n8n (WF1) |
| `titulo` | Título generado por IA | n8n (WF1) |
| `contenido` | Copy propuesto / editado por humano | n8n (WF1) / Streamlit |
| `contenido_json` | JSON original del LLM (auditoría técnica) | n8n (WF1) |
| `decision` | Decisión del curador (`pendiente`, `aprobado`, `rechazado`) | Streamlit (al final) |
| `user` | Nombre o email del curador que evaluó | Streamlit |
| `decision_at` | Timestamp ISO de la decisión humana | Streamlit |
| `comentario` | Justificación o notas de auditoría | Streamlit |
| `estado` | Estado espejo (`aprobado`, `rechazado`) | Streamlit |
| `estado_proceso` | Coordinación WF2 (`pendiente_oci`, `almacenado_oci`, `cerrado_rechazado`) | Streamlit / n8n (WF2) |
| `oci_path` | Ruta en OCI Object Storage Always Free | n8n (WF2) |

> [!TIP]
> Tienes un CSV de referencia listo para importar en `communitylab/dashboard/plantilla_curaduria.csv`.

---

### 🔴 Faltante 4: Conexión con Workflow 2 de n8n y Oracle Cloud (OCI)

El dashboard en Streamlit se encarga de la decisión humana (`Human-in-the-Loop`). Una vez que el curador hace clic en **"Aprobar"**:
1. Streamlit actualiza la fila con `decision = "aprobado"` y `estado_proceso = "pendiente_oci"`.
2. Para que ese activo pase a **Oracle Cloud Infrastructure (OCI)**, debe estar en ejecución el **Workflow 2 de n8n** (`communitylab/workflows/WF2-curaduria-oci.json`).

#### Pasos para que el pipeline extremo a extremo funcione:
1. Importa `communitylab/workflows/WF2-curaduria-oci.json` en tu instancia de n8n.
2. En el nodo **"Preparar Paquete OCI"**, configura tu URL PAR (Pre-Authenticated Request) de OCI Object Storage:
   ```javascript
   const PAR_BASE = "https://objectstorage.<REGION>.oraclecloud.com/p/.../n/<TENANCY>/b/<BUCKET>/o/";
   ```
3. En los nodos de Google Sheets de WF2, vincula la credencial de Google OAuth2 / Service Account con tu Document ID.
4. Cuando WF2 se ejecute (manual o por schedule cada 15 min), detectará el activo aprobado, realizará el `PUT` a OCI y marcará `estado_proceso = "almacenado_oci"`.

---

### 🔴 Faltante 5: Configurar Secretos en un nuevo Despliegue de Streamlit Cloud

Si deseas desplegar este repositorio principal (`Proyecto-Equipo-36`) en Streamlit Cloud:

1. Ve a [share.streamlit.io](https://share.streamlit.io/) y conecta tu cuenta de GitHub.
2. Crea una **New App**:
   - **Repository:** `FerIqm1993/Proyecto-Equipo-36`
   - **Branch:** `main`
   - **Main file path:** `app.py`
3. Antes de arrancar, haz clic en **Advanced settings... > Secrets**.
4. Pega el contenido íntegro de tu `.streamlit/secrets.toml` en el recuadro de texto.
5. Haz clic en **Deploy!**.

---

## 🚀 4. Comandos para Ejecución y Prueba Local

Para probar la aplicación en tu entorno local:

```powershell
# 1. Asegúrate de estar en la carpeta del proyecto
cd c:\projects\proyecto-36

# 2. Instala las dependencias
pip install -r requirements.txt

# 3. Verifica que tu archivo .streamlit/secrets.toml exista con credenciales válidas
Test-Path .streamlit/secrets.toml

# 4. Inicia la aplicación Streamlit
streamlit run app.py
```

La aplicación abrirá automáticamente tu navegador en `http://localhost:8501`.

---

## ✅ 5. Checklist de Verificación Final

- [x] Repositorio base `Proyecto-Equipo-36` actualizado con `git pull`.
- [x] Código de curaduría de Oscar (`VelaztiquiOscar/G10-LATAM-EQUIPO-36`) integrado en `app.py`.
- [x] Módulo `communitylab/dashboard/dashboard_curaduria.py` sincronizado.
- [x] Dependencias actualizadas en `requirements.txt` (`gspread`, `google-auth`, `pandas`, `streamlit`, `boto3`).
- [x] Archivo `.devcontainer/devcontainer.json` configurado.
- [x] Plantilla de credenciales `.streamlit/secrets.toml.example` generada en la raíz.
- [x] Enlaces directos a [https://g10-latam-equipo-36.streamlit.app/](https://g10-latam-equipo-36.streamlit.app/) integrados en `index.html` y `README.md`.
- [ ] **Acción del usuario:** Crear `.streamlit/secrets.toml` con las credenciales reales de GCP (para correr en local).
- [ ] **Acción del usuario:** Compartir el Google Sheet con el `client_email` del Service Account con permisos de Editor.
- [ ] **Acción del usuario:** Activar el flujo `WF2-curaduria-oci.json` en n8n con la PAR del Bucket OCI Always Free.
