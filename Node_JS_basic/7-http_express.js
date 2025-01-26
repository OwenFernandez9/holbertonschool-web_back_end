const express = require('express');
const fs = require('fs').promises;

const app = express();

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

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  const path = process.argv[2];
  res.type('text/plain');
  res.write('This is the list of our students\n');
  try {
    const studentData = await countStudents(path);
    res.send(studentData);
  } catch (error) {
    res.status(500).send(error.message);
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
