function findAverage(array) {
  return array.length === 0 ? 0 : array.reduce((acc, count)=> acc + count, 0) / array.length
}