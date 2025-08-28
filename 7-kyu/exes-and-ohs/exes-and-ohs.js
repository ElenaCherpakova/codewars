function XO(str) {
  let Xs = 0; let Os = 0;
  const arr = str.toLowerCase()
  for(let char of arr){
    if(char === 'x') Xs++
    if(char === 'o') Os++
  }
  return Xs === Os
}