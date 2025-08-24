// ES6_basic/100-createIteratorObject.js
export default function createIteratorObject(report) {
  const { allEmployees } = report;

  // Return an iterator (also iterable) that yields each employee
  return (function* iterate() {
    for (const employees of Object.values(allEmployees)) {
      for (const employee of employees) {
        yield employee;
      }
    }
  }());
}

