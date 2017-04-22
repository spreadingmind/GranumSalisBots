import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';

import Graph from 'react-graph-vis'

import brace from 'brace';
import AceEditor from 'react-ace';

import 'brace/mode/json';
import 'brace/theme/github';

let example = require('./example').default;


var options = {
    layout: {
        hierarchical: true
    },
    edges: {
        color: "#000000",
        arrows: 'to'
    }
};

var events = {
    select: function(event) {
        var { nodes, edges } = event;
        console.log(event);
    }
}

function onChange(newValue) {
    example = JSON.parse(newValue);
    update();
}


function update() {
    const graph = {
        nodes: example.nodes,
        edges: example.edges.map(({error, ...e}) => ({
            ...e,
            ...(error ? {color: '#f00'} : {}),
        })),
    };
    ReactDOM.render(
        <div style={{display: 'flex', height: '100%'}}>
            <Graph style={{width: '75%'}} graph={graph} options={options} events={events} />
            <AceEditor
                style={{height: '100%'}}
                mode="json"
                theme="github"
                onChange={onChange}
                name="UNIQUE_ID_OF_DIV"
                editorProps={{$blockScrolling: true}}
                value={JSON.stringify(example, null, '  ')}
            />
        </div>,
        document.getElementById('root')
    );
}
update();
