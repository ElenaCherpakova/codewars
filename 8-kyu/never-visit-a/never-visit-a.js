function SubtractSum(n){
   const fruits = {
    1: 'kiwi', 2: 'pear', 3: 'kiwi', 4: 'banana', 5: 'melon', 6: 'banana',
    7: 'melon', 8: 'pineapple', 9: 'apple', 10: 'pineapple'
  }
    while(true){
      const sum = n.toString().split("").reduce((acc, num)=> acc + Number(num), 0)
      n = n - sum 
      if (fruits[n]) return fruits[n]
  }
}