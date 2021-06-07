function resolveDependencies(dependenices) {
  
  let map = {}
  
  // create a dependency map
  for (let [base, dep] of dependenices) {
    if (map[dep]) {
      map[dep].push(base)
    } else {
      map[dep] = [base]
    }
  }
  
  let stack = Object.keys(map).map(num => parseInt(num))
  let ans = []
  
  // resolve the dependencies
  while (stack.length) {
    // get the latest number
    let curr = stack.pop()
    
    // if the number has no dependencies add it
    if (!map[curr] || !map[curr].length) {
      // check if it already exists
      if (ans.indexOf(curr) == -1) ans.push(curr)
      continue
    }
    
    // add the number back and add all its dependencies
    stack.push(curr)
    while (map[curr].length) stack.push(map[curr].pop())
  }
  
  return ans
}

const test = [[5,2],[6,2],[7,5],[9,3],[3,6],[8,2],[5,9]]
const ans = [7,5,9,3,6,8,2]
const attempt = resolveDependencies(test)

console.log(`Attempt: ${attempt}`)
console.log(`Answer: ${ans}`)
