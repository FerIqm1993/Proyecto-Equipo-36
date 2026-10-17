# 📌 Contexto de Continuación: Integración de Curaduría (CommunityLab — Equipo 36)

> **Documento de preservación de estado para retomar el trabajo una vez recibida la información del encargado.**  
> **Fecha de guardado:** 16 de Octubre de 2026

---

## 🎯 1. Resumen Ejecutivo de lo Realizado

1. **Sincronización Git Inicial:**
   - Se bajaron los últimos cambios de `https://github.com/FerIqm1993/Proyecto-Equipo-36.git` (commit `c18bd9e` en `main`).

2. **Integración del Repositorio de Curaduría de Oscar:**
   - Se analizó e implementó la arquitectura de [VelaztiquiOscar/G10-LATAM-EQUIPO-36](https://github.com/VelaztiquiOscar/G10-LATAM-EQUIPO-36.git) (que corre en producción en [g10-latam-equipo-36.streamlit.app](https://g10-latam-equipo-36.streamlit.app/)).
   - **`app.py`:** Se actualizó en la raíz con la aplicación completa v2.1 de Curaduría con Human-in-the-Loop, `gspread`, métricas en vivo, filtros, edición de copys en tiempo real y escritura atómica a prueba de condiciones de carrera con n8n.
   - **`communitylab/dashboard/dashboard_curaduria.py`:** Sincronizado para mantener paridad si se ejecuta dentro del subdirectorio.
   - **`requirements.txt`:** Actualizado con `streamlit>=1.30.0`, `pandas>=2.0.0`, `gspread>=6.0.0`, `google-auth>=2.20.0`, `boto3>=1.34.0`.
   - **`.devcontainer/devcontainer.json`:** Agregado para desarrollo con auto-arranque en GitHub Codespaces / VS Code Containers.
   - **`.streamlit/config.toml` y `.streamlit/secrets.toml.example`:** Configuración de tema visual oscuro y plantilla de secretos.
   - **`index.html` y `README.md`:** Actualizados con enlaces y botones directos a la aplicación en vivo en Streamlit Cloud.

3. **Herramientas Auxiliares Creadas:**
   - **`PLANTILLA_GOOGLE_SHEETS_CURADURIA.csv`:** Plantilla oficial con las 17 columnas y 4 registros realistas para importar a Google Sheets.
   - **`SOLICITUD_PARA_EL_ENCARGADO.md`:** Mensaje y guía paso a paso lista para reenviar al encargado/administrador.
   - **`SECRETS_TEMPLATE.toml`:** Plantilla TOML limpia para rellenar credenciales.
   - **`configurar_secrets.py`:** Asistente interactivo en Python que toma el archivo `.json` de Google Cloud y la URL del Sheet y genera `.streamlit/secrets.toml` automáticamente sin errores de formato en claves RSA.
   - **`FALTANTES_CURADURIA.md`:** Documentación técnica exhaustiva de la arquitectura y requisitos.

4. **Paquete Físico en el Escritorio:**
   - Se copió el kit completo en la carpeta:  
     `C:\Users\LuisFernandoMartínez\Desktop\Paquete_Curaduria_Para_Encargado\`  
     con un archivo `INSTRUCCIONES_RAPIDAS.txt` para su envío directo.

---

## ⏳ 2. Estado Actual: ¿En qué punto estamos detenidos?

La parte del código, interfaz y automatizaciones en el proyecto está **100% terminada y lista**.  
Actualmente estamos en espera de la respuesta del encargado con **2 datos externos**:

1. **El archivo `.json` de la Service Account de Google Cloud:**
   - Debe tener activadas las APIs: *Google Sheets API* y *Google Drive API*.
2. **El enlace o ID de la hoja de cálculo de Google Sheets:**
   - Creada a partir de `PLANTILLA_GOOGLE_SHEETS_CURADURIA.csv`, con la pestaña llamada `Curaduria`, compartida con el `client_email` de la Service Account con rol de **Editor**.

---

## 🚀 3. Guía para Retomar Cuando Llegue la Información (Paso a Paso)

Cuando el encargado te entregue el archivo `.json` y el enlace del Sheet, sigue estos pasos:

### Paso 1: Colocar el JSON en el proyecto
Copia el archivo `.json` que te entregó el encargado dentro de la carpeta:
```text
c:\projects\proyecto-36\
```

### Paso 2: Generar los secretos automáticamente
Abre tu terminal en `c:\projects\proyecto-36` y ejecuta:
```powershell
python configurar_secrets.py nombre_del_archivo.json "PEGA_AQUI_LA_URL_O_ID_DEL_SHEET"
```
*Este script validará la clave privada, escapará los saltos de línea correctamente y creará el archivo `.streamlit/secrets.toml` listo.*

### Paso 3: Probar la aplicación en local
Ejecuta:
```powershell
streamlit run app.py
```
Abre `http://localhost:8501`. La aplicación cargará automáticamente los registros desde Google Sheets. Prueba editando un activo y haciendo clic en **Aprobar** o **Rechazar** para validar la escritura en tiempo real.

### Paso 4: (Opcional) Despliegue en Streamlit Cloud
Si vas a conectar este repositorio (`FerIqm1993/Proyecto-Equipo-36`) en Streamlit Cloud:
1. Ve a [share.streamlit.io](https://share.streamlit.io/).
2. Conecta la app apuntando al archivo principal `app.py`.
3. Ve a **Settings > Secrets** y pega el contenido que generó tu archivo `.streamlit/secrets.toml`.

### Paso 5: Validar el flujo de persistencia OCI (WF2)
1. Importa `communitylab/workflows/WF2-curaduria-oci.json` en n8n.
2. Configura la URL PAR de tu bucket OCI Object Storage Always Free en el nodo *Preparar Paquete OCI*.
3. Ejecuta WF2 para verificar que tome los activos con `decision = aprobado` y `estado_proceso = pendiente_oci`, suba el JSON al bucket y marque `estado_proceso = almacenado_oci`.

---

## 🔗 4. Enlaces y Rutas de Referencia

- **Repositorio Base:** [https://github.com/FerIqm1993/Proyecto-Equipo-36.git](https://github.com/FerIqm1993/Proyecto-Equipo-36.git)
- **Repositorio Curaduría Oscar:** [https://github.com/VelaztiquiOscar/G10-LATAM-EQUIPO-36.git](https://github.com/VelaztiquiOscar/G10-LATAM-EQUIPO-36.git)
- **Despliegue Streamlit Cloud Activo:** [https://g10-latam-equipo-36.streamlit.app/](https://g10-latam-equipo-36.streamlit.app/)
- **Despliegue Portal Netlify:** [https://proyecto-equipo-36.netlify.app/](https://proyecto-equipo-36.netlify.app/)
- **Carpeta en Escritorio:** `C:\Users\LuisFernandoMartínez\Desktop\Paquete_Curaduria_Para_Encargado\`
- **Carpeta del Proyecto:** `c:\projects\proyecto-36\`
