[![Ask DeepWiki](https://deepwiki.com/badge.svg)](https://deepwiki.com/maocorrea1015/FactusLyn)
# Sistema de Facturación Electrónica – Backend en Flask

**Versión:** 1.0  
**Fecha:** 26 de septiembre de 2025  
**Equipo de Desarrollo:** ProtoDev Labs  
**Responsable Técnico:** Héctor Mauricio Forero Correa

---
<a href="https://git-scm.com/book/es/v2/Ap%C3%A9ndice-C:-Comandos-de-Git-Seguimiento-B%C3%A1sico">Documentacion oficial de git</a>
---
[![Título del Video](https://img.youtube.com/vi/vlCXdvcgiE0/0.jpg)](https://www.youtube.com/watch?v=vlCXdvcgiE0)


## 🧾 Objetivo del Proyecto


Desarrollar una **API REST** en **Flask (Python)** que gestione el ciclo completo de una factura electrónica conforme a la normativa de la **DIAN**. Esta API será consumida por sistemas frontend o integraciones externas.

---

## 🎯 Alcance del Proyecto (Backend)

### Incluye:

- Gestión de autenticación y autorización (usuarios, roles).
- Endpoints REST para:
  - Creación de clientes.
  - Registro de productos y servicios.
  - Generación de facturas electrónicas.
  - Generación de XML en formato UBL 2.1.
  - Firma digital de la factura.
  - Envío automático a la DIAN.
  - Registro del acuse de recibo y estado de la factura.
- Endpoints para consulta y descarga (PDF, XML).
- Logs de auditoría.
- Seguridad de la API (token JWT, HTTPS).
- Estructura modular y escalable.

### No incluye:

- Desarrollo frontend (web o móvil).
- Interfaz de usuario.
- Infraestructura de despliegue (DevOps, nube).
- Aplicaciones POS, nómina o notas crédito/débito (en esta versión).

---

## 🧱 Arquitectura General

- **Arquitectura:** Desacoplada, API RESTful consumible por otros sistemas.
- **Tecnologías:** Python 3.11+, Flask, SQLAlchemy, JWT, Celery (para tareas asincrónicas).
- **Base de datos:** PostgreSQL o SQLite (según entorno).
- **Firma digital:** Integración con proveedor autorizado por la DIAN.
- **Interfaz con DIAN:** API REST según resolución 000042.

---

## ✅ Requerimientos Funcionales

| ID   | Descripción                                                                 |
|------|------------------------------------------------------------------------------|
| Pd-1 | La API debe permitir autenticación vía tokens JWT.                          |
| Pd-2 | Debe existir un CRUD para clientes y productos.                             |
| Pd-3 | El sistema debe generar XML conforme al estándar UBL 2.1 exigido por DIAN.  |
| Pd-4 | El XML debe firmarse digitalmente con un certificado válido.                |
| Pd-5 | La API debe enviar el XML a la DIAN y registrar la respuesta.               |
| Pd-6 | Debe haber un endpoint para consultar el estado de una factura en la DIAN.  |
| Pd-7 | La API debe generar una representación gráfica de la factura (PDF).         |
| Pd-8 | Endpoints para consultar, filtrar y descargar facturas emitidas.            |

---

## ⚙️ Requerimientos No Funcionales

| ID   | Descripción                                                                 |
|------|------------------------------------------------------------------------------|
| Pd-1 | La API debe estar documentada con Swagger/OpenAPI.                          |
| Pd-2 | Todo acceso a la API debe realizarse por HTTPS.                             |
| Pd-3 | Se debe registrar toda operación relevante en un sistema de logs.           |
| Pd-4 | El sistema debe manejar errores y reintentos ante fallos con la DIAN.       |
| Pd-5 | Cumplimiento con Ley 1581 (protección de datos personales en Colombia).     |

---

## 🔐 Seguridad y Control

- **Autenticación:** JWT con roles diferenciados (admin, operador).
- **Validación de datos:** con `pydantic` o `marshmallow`.
- **Trazabilidad:** Logs de eventos como envío, errores, accesos y respuestas DIAN.
- **Acceso:** Limitado por token y nivel de usuario.

---

## 🔗 Endpoints Principales

```http
POST   /api/auth/login
GET    /api/clientes/
POST   /api/clientes/
GET    /api/facturas/
POST   /api/facturas/
GET    /api/facturas/<id>/
GET    /api/facturas/<id>/pdf
GET    /api/facturas/<id>/xml
POST   /api/facturas/<id>/enviar-dian
GET    /api/facturas/<id>/estado-dian
```
--- 
## 📐 Arquitectura de la App Web
- Esquema en construcción.

---
## 🧭 Diagrama de Flujo (Simplificado)
- En proceso de diseño. Incluirá: autenticación → generación de factura → firma → envío DIAN → consulta estado.

---
## 📦 Entregables
- API funcional (Flask, Python).

- Esquema de base de datos.

- Documentación técnica (Swagger/OpenAPI, instalación, despliegue).

- Scripts de generación de XML UBL 2.1.

- Función de firma digital.

- Manual de uso para los endpoints.

- Guía de integración con la DIAN.

---

## 📝 Observaciones
- Usar el entorno de pruebas de la DIAN antes de producción.

- Cumplir con la estructura XML UBL oficial provista por la DIAN.

- El CUFE debe ser generado correctamente y el XML firmado antes del envío.

© 2025 ProtoDev Labs

