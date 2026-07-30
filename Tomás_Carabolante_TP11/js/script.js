class Tarea {
  constructor(titulo, descripcion) {
    this.titulo = titulo;
    this.descripcion = descripcion;
    this.completada = false;
  }

  marcarCompleta() {
    this.completada = true;
  }

  getNombre() {
    return this.titulo;
  }

  getInfo() {
    const estado = this.completada ? 'completada' : 'pendiente';
    return `Título: ${this.titulo}\nDescripción: ${this.descripcion}\nEstado: ${estado}`;
  }
}

const tareas = [];
const formulario = document.getElementById('formTarea');
const listaTareas = document.getElementById('listaTareas');

formulario.addEventListener('submit', (event) => {
  event.preventDefault();

  const titulo = document.getElementById('titulo').value.trim();
  const descripcion = document.getElementById('descripcion').value.trim();

  if (!titulo || !descripcion) {
    alert('Completá ambos campos para crear una tarea.');
    return;
  }

  const tarea = new Tarea(titulo, descripcion);
  tareas.push(tarea);
  renderTareas();
  formulario.reset();
});

listaTareas.addEventListener('click', (event) => {
  const boton = event.target.closest('button');
  if (!boton) return;

  const indice = Number(boton.dataset.index);
  const tarea = tareas[indice];

  if (!tarea) return;

  if (boton.classList.contains('btn-completar')) {
    tarea.marcarCompleta();
    renderTareas();
  }

  if (boton.classList.contains('btn-info')) {
    alert(tarea.getInfo());
  }
});

function renderTareas() {
  if (tareas.length === 0) {
    listaTareas.innerHTML = '<li class="empty">No hay tareas todavía. Agregá una para empezar.</li>';
    return;
  }

  listaTareas.innerHTML = '';

  tareas.forEach((tarea, index) => {
    const item = document.createElement('li');
    item.className = `tarea ${tarea.completada ? 'tarea-completada' : ''}`;

    item.innerHTML = `
      <div>
        <h3>${escapeHtml(tarea.getNombre())}</h3>
        <p>${escapeHtml(tarea.descripcion)}</p>
      </div>
      <div class="tarea-actions">
        <button class="btn-completar" data-index="${index}" ${tarea.completada ? 'disabled' : ''}>
          ${tarea.completada ? 'Completada' : 'Completar'}
        </button>
        <button class="btn-info" data-index="${index}">Ver información</button>
      </div>
    `;

    listaTareas.appendChild(item);
  });
}

function escapeHtml(texto) {
  return texto
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

renderTareas();
