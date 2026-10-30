# Reportes de bugs

## TY-001 - La reserva confirma éxito pero no aparece en Mis turnos

- **Entorno:** Google Chrome 155.0.8059.85, Windows 10 22H2 (build 19045), instancia local `127.0.0.1:5000`; versión/build de la aplicación no visible.
- **Pasos para reproducir:**
  1. Abrir la app y registrar una cuenta nueva.
  2. Ingresar con esa cuenta.
  3. Completar fecha futura, hora disponible, duración 30 y un motivo único.
  4. Pulsar “Reservar”.
  5. Comprobar el mensaje y la tabla “Mis turnos”.
- **Resultado esperado:** la UI informa éxito solo si la reserva queda guardada y la fila aparece en “Mis turnos”.
- **Resultado obtenido:** en la corrida final, los intentos 5 y 6 de 10 mostraron “Turno reservado correctamente”, pero la tabla quedó en “No tenés turnos”. Las capturas muestran el formulario limpio y la tabla vacía.
- **Frecuencia:** a veces, 2 de 10 intentos en la corrida final y 1 de 10 en una serie independiente; 3 de 20 en conjunto. La exploración manual inicial pasó 1 de 1. Requiere seguimiento en más corridas y entorno representativo para afinar la tasa.
- **Severidad:** alta.
- **Prioridad sugerida:** P0, corregir antes de liberar porque afecta la operación principal y puede hacer que una persona crea que tiene turno cuando no lo tiene.
- **Evidencia:** `reports/screenshots/test_success_message_is_backed_by_visible_booking[5].png`, `reports/screenshots/test_success_message_is_backed_by_visible_booking[6].png`; reporte HTML `reports/reporte.html`.

## TY-002 - La cancelación pide confirmación nativa del navegador

- **Estado:** observación de interfaz, no reportada como defecto.
- **Detalle:** al cancelar aparece “¿Cancelar este turno?”. Selenium confirma el diálogo y verifica estado `cancelado`. No hay criterio de producto que indique si esa confirmación es correcta o si la cancelación debe ser inmediata; consultar al PO.

## Plantilla

### [ID] Título breve y específico

- **Entorno:** navegador y versión; sistema operativo; versión/build de la aplicación.
- **Pasos para reproducir:**
  1. 
  2. 
  3. 
- **Resultado esperado:**
- **Resultado obtenido:**
- **Frecuencia:** siempre / N de M intentos / una sola vez.
- **Severidad:** crítica / alta / media / baja.
- **Prioridad sugerida:** P0 / P1 / P2 / P3.
- **Evidencia:** ruta a captura/video, consola/reporte asociado.

## Severidad sugerida

- **Crítica:** pérdida/exposición extensa de datos o imposibilidad total de operar, sin alternativa.
- **Alta:** flujo esencial incorrecto, riesgo de doble asignación o acceso indebido con impacto importante.
- **Media:** función secundaria o workaround disponible; impacto acotado.
- **Baja:** defecto cosmético o de bajo impacto.

La severidad final se confirma con impacto de negocio; la prioridad sugerida indica el orden de corrección, no sustituye la decisión del equipo.