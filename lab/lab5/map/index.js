const { heristicValues, location } = require('./example')
class State {
  constructor (node, f, g) {
    this.node = node
    this.f = f // keep adding // path value
    this.g = g // lowest value
  }
}

Astar(location, heristicValues)

function Astar (place, heristic) {
  var openList = ['Arad']
  var closeList = []
  var start = 'start'
  var end = 'Bucharest'
  var goal = {}

  // for start
  var startNode = new State(start, 0, heristic[start])

  var pre = start
  var prevPathValue = [0]
  while (openList.length > 0) {
    var lowestIndex = 0

    goal[start] = Number.MAX_VALUE

    for (var i = 0; i < openList.length; i++) {
      const sum = prevPathValue.reduce((partialSum, a) => partialSum + a, 0);

      goal[openList[i]] =
        sum + location[pre][openList[i]] + heristic[openList[i]]


      if (goal[start] > goal[openList[i]]) {
        goal[start] = goal[openList[i]]
        lowestIndex = i
      }
    }
    prevPathValue.push(location[pre][openList[lowestIndex]])

    pre = openList[lowestIndex]

    var current = openList[lowestIndex]

    if (current == end) {
      console.log('END')
      break
    }

    // remove the current form openLst array
    var openList = removeFromArray(openList, current)
    closeList.push(current)

    var neighbours = addNeighbours(place, current)

    for (var i = 0; i < neighbours.length; i++) {
      openList.push(neighbours[i])
    }
  }
  console.log('openList', openList)
  console.log('closeList', closeList)
  console.log("g(n)",goal[start])
}

function addNeighbours (location, place) {
  var neighbour = []
  for (var j in location[place]) {
    neighbour.push(j)
  }
  return neighbour
}
function removeFromArray (arr, node) {
  const nodeIndex = arr.indexOf(node)
  arr.splice(nodeIndex, 1)
  return arr
}
