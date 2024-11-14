export default function appendToEachArrayValue(array, appendString) {
  const resarray = [...array];
  let idx = 0;

  for (const value of array) {
    resarray[idx] = appendString + value;
    idx += 1;
  }

  return resarray;
}
