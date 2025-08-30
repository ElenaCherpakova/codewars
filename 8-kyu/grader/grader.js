function grader(score) {
  if(score > 1 || score < 0) return 'F'
  return score >= 0.9 ? 'A' : score >= 0.8 ? 'B' : score >= 0.7 ? 'C'
  : score >= 0.6 ? 'D' : 'F'
  
}