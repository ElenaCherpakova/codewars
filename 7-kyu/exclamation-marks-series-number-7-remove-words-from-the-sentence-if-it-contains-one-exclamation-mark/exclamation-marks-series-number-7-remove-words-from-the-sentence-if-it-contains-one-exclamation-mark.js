function remove (string) {
  return string.split(' ').filter((chr)=> chr.split('!').length !==2).join(' ')
}