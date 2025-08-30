function findAverage(array) {
  if(array.length === 0) return 0
  return array.reduce((acc, count)=> acc + count / array.length, 0)
}