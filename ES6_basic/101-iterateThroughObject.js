// ES6_basic/101-iterateThroughObject.js
export default function iterateThroughObject(reportWithIterator) {
  const names = [];
  for (const name of reportWithIterator) {
    names.push(name);
  }
  return names.join(' | ');
}

