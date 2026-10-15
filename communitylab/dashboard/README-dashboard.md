# CommunityLab — Dashboard de Curaduría v2.1 (Streamlit)

> **"La IA propone — El humano decide — OCI guarda solo lo aprobado."**

Este módulo implementa la interfaz web de revisión humana (*Human-in-the-Loop*) para la curaduría y aprobación de contenidos generados automáticamente por el pipeline de inteligencia de **CommunityLab**.

---

## 🎯 Propósito y Flujo de Estados

El dashboard interactúa directamente con una hoja de **Google Sheets** compartida y se coordina de manera asíncrona con el flujo **WF2 (Curaduría → OCI)** en **n8n**:

```mermaid
flowchart LR
    A[WF1: Ingesta + LLM] -->|Append filas| B[(Google Sheet: Curaduria)]
    B -->|Carga de filas| C[Dashboard Streamlit]
    C -->|APROBAR| D[decision=aprobado<br/>estado_proceso=pendiente_oci]
    C -->|RECHAZAR| E[decision=rechazado<br/>estado_proceso=cerrado_rechazado]
    D -->|Lectura periódica| F[WF2: n8n]
    F -->|PUT Object| G[(OCI Object Storage)]
    F -->|Marca final| H[almacenado_oci ✅]
```

### Flujo de Acciones:
1. **APROBAR**:
   - `decision`: `aprobado`
   - `estado_proceso`: `pendiente_oci`
   - **WF2** detecta el cambio en su ejecución periódica, sube el contenido a **Oracle Cloud Infrastructure (OCI Object Storage)** y actualiza la fila con la URL/ruta del objeto.
2. **RECHAZAR**:
   - `decision`: `rechazado`
   - `estado_proceso`: `cerrado_rechazado`
   - Queda archivado y registrado en la hoja para auditoría; **WF2** lo ignora por filtro.
3. **EDICIÓN HUMANA**:
   - Si el curador ajusta el texto en la interfaz, el campo `contenido` guarda la versión editada por el humano, mientras que `contenido_json` preserva la salida original del LLM como pista de auditoría.

---

## 🛡️ Características de Robustez

- **Rastreo por fila física real (`__row_number`)**: Dado que `asset_id` puede repetirse entre distintas ejecuciones de WF1 (por ejemplo, `asset-001-li` en cada corrida), el dashboard localiza y actualiza la fila posicional exacta en Google Sheets (fila 2 en adelante), evitando colisiones o sobreescritura accidental de registros anteriores.
- **Prevención de condiciones de carrera (Race-Condition Proof)**: El campo `decision` se escribe deliberadamente en último lugar. Como WF2 filtra por `decision=aprobado`, todos los metadatos y textos ya están asegurados en la hoja antes de que el worker en la nube inicie la subida.

---

## 📋 Requisitos Previos

- **Python**: Versión 3.10 o superior (requerido por sintaxis `int | None` y tipado moderno).
- **Google Cloud Platform (GCP)**: Service Account con la API de Google Sheets y Google Drive habilitadas.
- **Google Sheet**: Creado con una pestaña nombrada obligatoriamente `Curaduria`.

---

## 🚀 Instalación y Puesta en Marcha

### 1. Clonar o acceder a la carpeta del dashboard
```bash
cd communitylab/dashboard
```

### 2. Crear y activar entorno virtual
```bash
# En Windows (PowerShell):
python -m venv venv
.\venv\Scripts\Activate.ps1

# En Linux / macOS:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar Credenciales y Secrets
Crea el archivo `.streamlit/secrets.toml` dentro de la carpeta `communitylab/dashboard/` (o en tu directorio de usuario `~/.streamlit/secrets.toml`):

```toml
[gcp_service_account]
type = "service_account"
project_id = "tu-proyecto-gcp"
private_key_id = "clave-id-aqui"
private_key = "-----BEGIN PRIVATE KEY-----\nTU_CLAVE_PRIVADA_AQUI\n-----END PRIVATE KEY-----\n"
client_email = "tu-servicio@tu-proyecto-gcp.iam.gserviceaccount.com"
client_id = "123456789012345678901"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/tu-servicio%40tu-proyecto-gcp.iam.gserviceaccount.com"
spreadsheet_id = "TU_ID_DE_GOOGLE_SHEETS"
worksheet_name = "Curaduria"
```

> ⚠️ **IMPORTANTE:** Comparte tu Google Sheet con el correo `client_email` de tu Service Account otorgándole permisos de **Editor**.

### 5. Estructura de Columnas en Google Sheets (Hoja: `Curaduria`)
La primera fila (encabezados) debe contener las siguientes columnas (el orden no afecta gracias al mapeo por nombre):
- `execution_id`
- `interaction_id`
- `asset_id`
- `canal`
- `autor`
- `tipo_activo`
- `score_final`
- `titulo`
- `contenido`
- `contenido_json`
- `decision`
- `user`
- `comentario_humano`
- `timestamp_decision`
- `estado`
- `estado_proceso`
- `oci_path`

### 6. Ejecutar la aplicación
```bash
streamlit run dashboard_curaduria.py
```

La interfaz se abrirá automáticamente en tu navegador web en `http://localhost:8501`.

---

## 📊 Vistas y Funcionalidades del Dashboard

1. **Panel de Métricas en Tiempo Real**:
   - Activos totales procesados.
   - Cantidad de contenidos pendientes de revisión.
   - Tasa de aprobación y activos persistidos en OCI.
2. **Filtros Dinámicos**:
   - Filtrado por canal de origen (`#logros-y-empleos`, `#ayuda-tecnica`, etc.).
   - Filtrado por tipo de activo (`LinkedIn`, `FAQ`, `Newsletter`).
   - Umbral de puntuación mínima (*Score*).
3. **Editor Interactivo**:
   - Previsualización en formato Markdown del texto a publicar.
   - Campo editable de texto para ajustes de redacción antes de aprobar.
   - Campo de justificación / comentario del curador.
4. **Historial de Auditoría**:
   - Registro visible de quién aprobó o rechazó cada contenido con marca temporal UTC.
