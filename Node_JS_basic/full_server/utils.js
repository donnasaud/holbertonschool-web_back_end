import fs from 'fs';

function readDatabase(filePath) {
  return new Promise((resolve, reject) => {
    fs.readFile(filePath, 'utf8', (err, data) => {
      if (err) {
        reject(err);
        return;
      }

      try {
        const lines = data.split('\n').slice(1).filter((line) => line.trim());
        const students = lines
          .map((line) => {
            const parts = line.split(',');
            return { firstname: parts[0], field: parts[parts.length - 1] };
          })
          .filter((student) => student.firstname && student.field);

        const studentsByField = {};
        students.forEach(({ firstname, field }) => {
          if (!studentsByField[field]) {
            studentsByField[field] = [];
          }
          studentsByField[field].push(firstname);
        });

        resolve(studentsByField);
      } catch (error) {
        reject(error);
      }
    });
  });
}

export default readDatabase;
