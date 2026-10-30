# Notas de testing exploratorio

**Aplicación:** TurnosYa, versión/build no expuesta en la interfaz  
**Fecha:** 2026-10-30  
**Entorno:** Windows; Chrome/Chromium se registra al ejecutar Selenium. Prueba local en `127.0.0.1:5000`.  
**Duración:** charter propuesto de 35 minutos. La sesión asistida aquí registrada no fue cronometrada de forma fiable; no se afirma haber completado 30-40 minutos reales. Completar una sesión cronometrada antes de la aprobación final.

## Charter de 35 minutos

- 0-5 min: explorar login/registro y mensajes de validación.
- 5-15 min: reservar un turno y revisar persistencia, duplicados y límites visibles.
- 15-23 min: buscar por motivo y revisar aislamiento/listado.
- 23-28 min: cancelar y comprobar el estado resultante.
- 28-35 min: revisar acceso anónimo, administración y funciones visibles no especificadas; consolidar evidencias.

## Observaciones ejecutadas

1. Abrir la raíz redirige a la pantalla “Ingresar”. La navegación ofrece “Ingresar” y “Registrarse”.
2. Registrar una cuenta con nombre, email de prueba y contraseña muestra “Cuenta creada. Ya podés ingresar” y conduce al login.
3. Ingresar con esa cuenta conduce a “Mis turnos”, con campos Fecha, Hora, Duración (min), Motivo, búsqueda y una tabla vacía.
4. Reservar un turno para 2026-11-02 a las 09:00, duración predeterminada 30 y motivo “Control exploratorio” mostró éxito y una fila visible con estado “activo”. Un intento no permite estimar fallos intermitentes.
5. El listado mostró además acciones “Eliminar” y “Exportar a PDF”; no figuran en los requisitos funcionales entregados.

## Hallazgos y seguimiento

- La exploración manual inicial no reprodujo el defecto de reserva (1 de 1); la suite automatizada sí lo reprodujo: 3 de 20 intentos parametrizados en dos series con los valores del formulario verificados. Ver TY-001 en `bugs.md`.
- Un control automatizado cubre la cancelación y acepta el diálogo visible “¿Cancelar este turno?”; la acción actualiza el estado a cancelado.
- Eliminar, PDF y administración quedan como preguntas funcionales, no como defectos hasta recibir definición.
- La cuenta de exploración y su turno son datos creados para la prueba. Antes de continuar se limpiarán solo mediante el endpoint de reset documentado en la instancia local desechable.

## Limitaciones

No se completó exploración cronometrada de 30-40 minutos ni una revisión real de varios navegadores, dispositivos, concurrencia, accesibilidad o rol administrativo. La automatización cubre una parte de los flujos y no sustituye esas actividades.