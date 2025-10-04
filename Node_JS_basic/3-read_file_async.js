const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Cannot load the database'));
        return;
      }

      // Split file into lines and remove empty lines
      const lines = data.trim().split('\n').filter((line) => line.length > 0);

      // Remove header row
      const students = lines.slice(1);

      console.log(`Number of students: ${students.length}`);

      const fields = {};

      // Process each line
      for (const line of students) {
        const [firstname, lastname, age, field] = line.split(',');
        if (!fields[field]) {
          fields[field] = [];
        }
        fields[field].push(firstname);
      }

      // Print results for each field
      for (const [field, names] of Object.entries(fields)) {
        console.log(`Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`);
      }

      resolve();
    });
  });
}

module.exports = countStudents;

