function logicalCalc(array, op){
  const obj = {
    AND: (a, b)=> a && b,
    OR: (a, b)=> a || b,
    XOR: (a, b)=> a !== b
  }
  return array.reduce(obj[op])
}