export default {
  nodes: [
      {id: 1, label: 'Node 1'},
      {id: 2, label: 'Node 2'},
      {id: 3, label: 'Node 3'},
      {id: 4, label: 'Node 4'},
      {id: 5, label: 'Node 5'}
    ],
  edges: [
      {from: 1, to: 1, label: 'Loop'},
      {from: 1, to: 2, label: 'label'},
      {from: 1, to: 3, label: 'label'},
      {from: 2, to: 4, label: 'label', error: true},
      {from: 2, to: 5, label: 'label'},
    ]
}
