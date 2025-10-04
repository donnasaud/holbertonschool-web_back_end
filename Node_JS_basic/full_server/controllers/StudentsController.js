import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(request, response) {
    const database = process.argv[2];
    readDatabase(database)
      .then((studentsByField) => {
        response.status(200);
        response.write('This is the list of our students\n');

        const fields = Object.keys(studentsByField).sort();

        for (const field of fields) {
          const students = studentsByField[field];
          response.write(`Number of students in ${field}: ${students.length}. List: ${students.join(', ')}\n`);
        }
        response.end();
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(request, response) {
    const { major } = request.params;

    if (major !== 'CS' && major !== 'SWE') {
      response.status(500).send('Major parameter must be CS or SWE');
      return;
    }

    const database = process.argv[2];
    readDatabase(database)
      .then((studentsByField) => {
        const studentsInMajor = studentsByField[major] || [];
        response.status(200).send(`List: ${studentsInMajor.join(', ')}`);
      })
      .catch(() => {
        response.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
