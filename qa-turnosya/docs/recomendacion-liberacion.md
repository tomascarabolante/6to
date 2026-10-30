# Recomendación de liberación

## Decisión: no liberar esta versión

La prueba automatizada final ejecutó 17 casos: 15 pasaron y 2 fallaron. Los fallos son dos reproducciones del mismo defecto P0: la interfaz confirma una reserva que no aparece en “Mis turnos”. En series automatizadas se observó en 3 de 20 intentos; la prueba manual inicial pasó 1 de 1. Una persona puede confiar en una confirmación y acudir esperando un turno inexistente.

## Condiciones para reevaluar

1. Corregir TY-001 y conservar el mensaje de éxito solo cuando la reserva se haya guardado correctamente.
2. Ejecutar nuevamente la suite en el entorno candidato: cero fallos en los flujos P0/P1 y al menos 30 repeticiones de reserva sin confirmaciones falsas.
3. Completar la sesión exploratoria cronometrada de 30-40 minutos, registrar duración real y actualizar las notas.
4. Resolver con PO las preguntas de alcance de administración, PDF, eliminación, restricciones de fecha/horario y criterios de cancelación.
5. Repetir pruebas de navegador/versión soportados y confirmar la identidad del build candidato.

## Resultado de esta evaluación

- Suite final: 17 casos, 15 pasaron, 2 fallaron.
- Defecto confirmado: TY-001, severidad alta, prioridad sugerida P0.
- Evidencia: `reports/reporte.html` y capturas relacionadas en `reports/screenshots/`.
- Cobertura manual limitada: no satisface la duración mínima de exploración solicitada; queda como pendiente, no se afirma como completada.

Esta recomendación se basa en los requisitos disponibles y el entorno local probado. No equivale a certificación de seguridad, accesibilidad, concurrencia ni compatibilidad amplia.