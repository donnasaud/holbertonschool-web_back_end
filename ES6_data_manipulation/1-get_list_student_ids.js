export default function getListStudentIds(students) {
  // Check if the argument is an array
  if (!Array.isArray(students)) {
    return [];
  }

  // Use map to extract the id from each student object
  return students.map((student) => student.id);
}
