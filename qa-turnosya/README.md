# Integrantes

Tomás Baroli, Tomás Carabolante Santiago De Ocaña.

# QA de TurnosYa

Suite de pruebas de caja negra con pytest y Selenium. La automatización usa Page Object Model, fixtures de navegador/datos, pruebas parametrizadas, esperas explícitas y capturas automáticas cuando falla un test.

## Requisitos

- Windows 10/11.
- Python 3.10 o posterior.
- Google Chrome o Chromium instalado. Selenium Manager puede descargar/ubicar el driver correspondiente; se requiere acceso a internet la primera vez si no está disponible localmente.
- La aplicación TurnosYa ejecutándose en una instancia local desechable.

## Instalación

Desde PowerShell, en la carpeta raíz del proyecto:

```powershell
.\venv\Scripts\python.exe -m pip install -r qa-turnosya\requirements-qa.txt
```

Si no existe el entorno `venv`, crear uno e instalar también las dependencias de la aplicación:

```powershell
py -m venv venv
.\venv\Scripts\python.exe -m pip install -r requirements.txt
.\venv\Scripts\python.exe -m pip install -r qa-turnosya\requirements-qa.txt
```

## Iniciar la aplicación

Abrir una terminal PowerShell en la raíz y ejecutar:

```powershell
.\venv\Scripts\python.exe app.py
```

Dejar esa terminal abierta. Por defecto la app queda en `http://127.0.0.1:5000`.

## Ejecutar la suite

Desde la raíz del proyecto:

```powershell
.\venv\Scripts\python.exe -m pytest -c qa-turnosya\pytest.ini -v qa-turnosya\tests --html=qa-turnosya\reports\reporte.html --self-contained-html
```

O, de forma equivalente, entrar primero a `qa-turnosya` y ejecutar:

```powershell
..\venv\Scripts\python.exe -m pytest -v --html=reports\reporte.html --self-contained-html
```

Para mostrar Chrome en lugar de ejecutarlo en modo headless:

```powershell
$env:QA_HEADLESS = "0"
.\venv\Scripts\python.exe -m pytest -c qa-turnosya\pytest.ini -v qa-turnosya\tests --html=qa-turnosya\reports\reporte.html --self-contained-html
```

Para indicar otra URL local:

```powershell
.\venv\Scripts\python.exe -m pytest -c qa-turnosya\pytest.ini -v qa-turnosya\tests --base-url http://127.0.0.1:5000 --html=qa-turnosya\reports\reporte.html --self-contained-html
```

## Datos y seguridad

El fixture llama a `GET /test/reset` antes y después de **cada caso** para no dejar cuentas ni turnos de prueba. Ese endpoint elimina todos los usuarios y turnos de la instancia seleccionada. Por protección, la suite rechaza hosts que no sean `localhost`, `127.0.0.1` o `::1`; de todos modos, usar exclusivamente una instancia local desechable y sin datos que se necesiten conservar. No apuntar la suite a producción ni a una base compartida.

Cada prueba crea su propia cuenta y sus reservas mediante la interfaz. El prefijo de emails es único por corrida. Si el reset no está disponible o el servidor no está arriba, el setup falla antes de ejecutar el caso.

## Resultados

- Reporte HTML: `reports/reporte.html`.
- Capturas de pruebas fallidas: `reports/screenshots/`.
- Plan, preguntas al PO, notas exploratorias y plantilla de bugs: `docs/`.

La aplicación no se modifica con estos artefactos QA. La recomendación de liberación para esta evaluación está en `docs/recomendacion-liberacion.md`; ver también `docs/plan-pruebas.md`, `docs/preguntas-po.md` y `docs/bugs.md`.