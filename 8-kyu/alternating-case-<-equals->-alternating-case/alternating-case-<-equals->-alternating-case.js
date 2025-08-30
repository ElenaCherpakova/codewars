String.prototype.toAlternatingCase = function () {
  let result = ''
  for(let i = 0; i < this.length; i++){
    const code = this.charCodeAt(i)
    if(code >= 65 && code <= 90){
        result += String.fromCharCode(code + 32)
    }else if(code >= 97 && code <= 122){
        result += String.fromCharCode(code - 32)
    }else {
      result += this[i]
    }
  }
  return result
}