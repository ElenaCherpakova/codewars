function gcd(a, b){
  a = Math.abs(a);
  b = Math.abs(b);
  
  while (b !==0){
    let temp = b;
    b = a % b
    a = temp
    }
  return a;
}
​
​
function solution(numbers) {
   if(numbers.length === 0){
  return 0;
  }
  let result = numbers[0];
  for(let i = 1; i < numbers.length; i++){
  result = gcd(result, numbers[i])
  }
  return result * numbers.length;
}