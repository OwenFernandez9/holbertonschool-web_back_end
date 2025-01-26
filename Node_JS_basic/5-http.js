const http = require('http');
const fs = require('fs');

function countStudents(pathToFile) {
  return new Promise((resolve, reject) => {
    fs.readFile(pathToFile, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
      } else {
        const lines = data.split('\n').filter((line) => line.trim() !== '');
        const totalStudents = lines.length - 1;
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

        let result = `Number of students: ${totalStudents}\n`;
        Object.keys(fields).forEach((field) => {
          result += `Number of students in ${field}: ${fields[field].length}. List: ${fields[field].join(', ')}\n`;
        });

        resolve(result);
      }
    });
  });
}

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.statusCode = 200;
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    const dbPath = process.argv[2];
    if (!dbPath) {
      res.statusCode = 400;
      res.end('Database file is required');
    } else {
      countStudents(dbPath)
        .then((result) => {
          res.statusCode = 200;
          res.setHeader('Content-Type', 'text/plain');
          res.end(`This is the list of our students\n${result}`);
        })
        .catch((error) => {
          res.statusCode = 500;
          res.end(error.message);
        });
    }
  } else {
    res.statusCode = 404;
    res.end('Not Found');
  }
});

app.listen(1245, () => {
  console.log('Server running at http://localhost:1245/');
});

module.exports = app;
