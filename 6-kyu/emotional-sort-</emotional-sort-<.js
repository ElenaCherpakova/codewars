function sortEmotions(arr, order) {
    const emotions = {':D': 5, ':)': 4, ':|': 3, ':(': 2, 'T_T': 1}
    const sorted = arr.map((x)=> emotions[x]).sort((a, b)=> order ? b - a : a - b)
    return sorted.map((num)=> Object.keys(emotions).find(key => emotions[key] === num))
  }
  