# Plan de pruebas - TurnosYa

## Objetivo y alcance

Validar desde la interfaz web los requisitos RF-01 a RF-07 de TurnosYa antes de liberar la versión candidata. La prueba es de caja negra: no se inspecciona el código ni la base de datos de la aplicación. Las verificaciones automatizadas interactúan con la UI usando Selenium; el endpoint de limpieza documentado por el proyecto se usa solo en un ambiente local desechable.

Incluye registro, ingreso/salida, control de acceso a turnos, creación, exclusividad de horario, listado, búsqueda y cancelación. Administración, validaciones de campos, límites, PDF, concurrencia, seguridad y accesibilidad requieren criterios de aceptación o entorno de prueba adicionales.

## Prioridad

| Prioridad | Cobertura | Motivo |
| --- | --- | --- |
| P0 | Reserva y persistencia visible; evitar doble reserva; acceso anónimo; cancelación | Riesgo directo de pérdida/doble asignación de turnos y exposición de operaciones |
| P1 | Registro, autenticación, salida, listado y búsqueda | Flujos principales de uso y aislamiento de la información por usuario |
| P2 | Límites y formatos, administración, exportación, accesibilidad, compatibilidad y concurrencia | Requisitos incompletos o funciones visibles sin criterio acordado |

## Estrategia y datos

- Exploración manual guiada por los flujos principales, con registro de ruta, entradas y resultado visible.
- Automatización de regresión con pytest + Selenium, Page Object Model, esperas explícitas y casos parametrizados.
- Cada caso crea una cuenta con email único y los turnos necesarios a través de la UI.
- El fixture limpia los datos antes y después de cada prueba mediante `GET /test/reset`, endpoint documentado en el README de la aplicación. Ejecutar únicamente en una instancia local desechable: la limpieza elimina todos los usuarios y turnos de esa instancia.
- Los fallos de pruebas generan PNG en `reports/screenshots/`; pytest-html produce `reports/reporte.html`.

## Criterios de entrada y salida

Entrada: instancia local accesible en `http://127.0.0.1:5000`, navegador Chrome/Chromium disponible y entorno Python QA instalado.

Salida: todos los P0/P1 pasan o cada fallo queda asociado a un bug reproducible; reporte HTML generado; riesgos sin criterio funcional quedan anotados como preguntas al PO. No se recomienda liberar con fallos P0/P1 abiertos.

## Manual vs. automatizado

Automatizar: registro e ingreso, acceso sin sesión, creación y visibilidad del turno, reserva duplicada, búsqueda, cancelación, regresión de éxito informado pero no persistido y validaciones simples repetibles.

Mantener manual hasta aclarar requisitos o añadir infraestructura: exploración visual y responsive, accesibilidad con teclado/lector, compatibilidad entre navegadores, roles administrativos, exportación PDF, concurrencia real, límites de fecha/horario y seguridad. Selenium de navegador único no reemplaza estas pruebas.

## Riesgos y límites

La versión y el número de build no son visibles; el navegador instalado se registra en ejecución y debe incorporarse al bug report. El endpoint de reset es destructivo y no debe apuntarse a datos compartidos. Una prueba aleatoria puede requerir repetición para estimar frecuencia; registrar intentos y resultados, no inferir frecuencia a partir de una sola ejecución. Los requisitos incompletos no se convierten en defectos sin decisión del PO.