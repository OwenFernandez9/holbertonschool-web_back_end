const fs = require('fs').promises;

async function countStudents(path) {
  try {
    const data = await fs.readFile(path, 'utf8');
    const lines = data.split('\n').filter((line) => line.trim() !== '');

    const totalStudents = lines.length - 1;
    let response = `Number of students: ${totalStudents}\n`;

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

    for (const field in fields) {
      if (Object.prototype.hasOwnProperty.call(fields, field)) {
        response += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
      }
    }

    return response;
  } catch (err) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
