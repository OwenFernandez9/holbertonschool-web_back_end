const fs = require('fs').promises;

async function countStudents(path) {
  try {
    // Leer el archivo de manera asíncrona
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== ''); // Eliminar líneas vacías

    const totalStudents = lines.length - 1;
    console.log(`Number of students: ${totalStudents}`);

    const fields = {};
    lines.slice(1).forEach((line) => {
      const [firstname, , , field] = line.split(',');
      if (field) {
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }
    });

    // Mostrar los estudiantes por campo de especialidad
    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        console.log(
          `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}`,
        );
      }
    }

    return Promise.resolve(); // Resolver la promesa cuando todo haya terminado
  } catch (err) {
    // Si ocurre un error, lanzar un error con el mensaje solicitado
    return Promise.reject(new Error('Cannot load the database'));
  }
}

module.exports = countStudents;
