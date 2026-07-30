function registrarProducto() {
  const nombreEl = document.getElementById('nombre');
  const precioEl = document.getElementById('precio');
  const displayArea = document.getElementById('displayArea');
  const prodName = document.getElementById('prodName');
  const prodPrice = document.getElementById('prodPrice');

  const nombre = nombreEl.value.trim();
  const precio = precioEl.value;

  if (!nombre) {
    alert('El nombre del producto no puede estar vacío.');
    nombreEl.focus();
    return;
  }

  console.log('Nombre del producto:', nombre);
  console.log('Precio:', precio);

  prodName.textContent = nombre;
  prodPrice.textContent = precio || '0.00';

  displayArea.style.display = 'block';
  displayArea.setAttribute('aria-hidden', 'false');
}

function limpiar() {
  const displayArea = document.getElementById('displayArea');
  const prodName = document.getElementById('prodName');
  const prodPrice = document.getElementById('prodPrice');

  prodName.textContent = '';
  prodPrice.textContent = '';
  displayArea.style.display = 'none';
  displayArea.setAttribute('aria-hidden', 'true');
}

function cambiarPagina(pagina) {
  if (!pagina) return;
  window.location.href = pagina;
}
