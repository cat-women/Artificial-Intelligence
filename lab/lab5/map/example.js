const location = {
  start: { Arad: 0 },
  Arad: {
    Zerind: 75,
    Timisoara: 118,
    Sibiu: 140
  },
  Zerind: { Oradea: 71 },
  Oradea: { Sibiu: 151 },
  Timisoara: { Lugoj: 111 },
  Lugoj: { Mahadia: 70 },
  Mahadia: { Dobreta: 75 },
  Dobreta: { Craiova: 120 },
  Sibiu: {
    Fagaras: 99,
    Rimnicu: 80
  },
  Fagaras: { Bucharest: 211 },
  Rimnicu: { Pitesti: 97, Craiova: 146 },
  Craiova: { Pitesti: 138 },
  Pitesti: { Bucharest: 101 },
  Bucharest: { Urziceni: 85, Giurgiu: 90 },
  Urziceni: { Hirsova: 98, Vaslui: 142 },
  Hirsova: { Eforie: 86 },
  Vaslui: { Lasi: 92 },
  Lasi: { Neamt: 87 }
}
const heristicValues = {
  Arad: 366,
  Bucharest: 0,
  Craiova: 160,
  Dobreta: 242,
  Eforie: 161,
  Fagaras: 178,
  Giurgiu: 77,
  Hirsova: 151,
  Lasi: 226,
  Lugoj: 244,
  Mahadia: 241,
  Neamt: 234,
  Oradea: 380,
  Pitesti: 98,
  Rimnicu: 193,
  Urziceni: 80,
  Vaslui: 80,
  Zerind: 374,
  Timisoara: 329,
  Sibiu: 254
}

module.exports = {heristicValues,location}
