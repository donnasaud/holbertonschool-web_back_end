export default function updateStudentGradeByCity(students, city, newGrades) {
  return students
    // First, filter students by city
    .filter((student) => student.location === city)
    // Then, map each student to add their grade
    .map((student) => {
      // Find the grade for this student
      const gradeObj = newGrades.find((grade) => grade.studentId === student.id);
      
      // Return the student with the new grade (or 'N/A' if no grade found)
      return {
        ...student,
        grade: gradeObj ? gradeObj.grade : 'N/A',
      };
    });
}
