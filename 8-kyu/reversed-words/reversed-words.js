function reverseWords(str){
  let res = ''
  let splitToWords = str.split(' ')
  for (let i = splitToWords.length - 1; i >= 0; i--){
    res +=splitToWords[i] + ' '
    }
    return res.trim()
  }