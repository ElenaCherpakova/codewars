function sum (numbers) {
  return numbers.length === 0 ? 0 : numbers.reduce((acc, num)=> acc + num, 0)
}