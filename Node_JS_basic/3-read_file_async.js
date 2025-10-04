const fs = require('fs');

function countStudents(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(Error('Cannot load the database'));
        return;
      }

      const lines = data.toString().split('\n').filter((line) => line.trim() !== '');
      const students = lines.map((line) => line.split(','));

      const response = [];
      const totalStudents = students.length > 1 ? students.length - 1 : 0;
      const totalMsg = `Number of students: ${totalStudents}`;
      console.log(totalMsg);
      response.push(totalMsg);

      const fields = {};

      // Skip header row
      for (const student of students.slice(1)) {
        const [firstName, , , field] = student;
        if (!fields[field]) fields[field] = [];
        fields[field].push(firstName);
      }

      for (const [field, names] of Object.entries(fields)) {
        const msg = `Number of students in ${field}: ${names.length}. List: ${names.join(', ')}`;
        console.log(msg);
        response.push(msg);
      }

      resolve(response);
    });
  });
}

module.exports = countStudents;
