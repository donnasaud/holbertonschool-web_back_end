export default function cleanSet(set, startString) {
  // If startString is empty or not a string, return empty string
  if (!startString || typeof startString !== 'string') {
    return '';
  }

  // Filter values that start with startString and remove the prefix
  const filteredValues = [];
  
  for (const value of set) {
    // Check if value is a string and starts with startString
    if (typeof value === 'string' && value.startsWith(startString)) {
      // Remove the startString prefix and add to results
      const suffix = value.slice(startString.length);
      filteredValues.push(suffix);
    }
  }
  
  // Join all filtered values with '-'
  return filteredValues.join('-');
}
