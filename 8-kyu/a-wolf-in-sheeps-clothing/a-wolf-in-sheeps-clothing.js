function warnTheSheep(queue) {
  const wolfIndx = queue.indexOf('wolf') 
  if(wolfIndx === queue.length - 1){
    return "Pls go away and stop eating my sheep"
  }else {
    const sheepNum = queue.length - wolfIndx - 1
    return `Oi! Sheep number ${sheepNum}! You are about to be eaten by a wolf!`
  }
}