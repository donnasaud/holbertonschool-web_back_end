export default function getStudentIdsSum(students) {
  // Use reduce to sum all student IDs
  return students.reduce((sum, student) => sum + student.id, 0);
}
