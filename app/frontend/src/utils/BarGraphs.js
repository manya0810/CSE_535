import React from 'react'
import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ReferenceLine,
    Cell,
    Legend,
  } from "recharts";

const BarGraphGen = ({ data }) => {
    let f=false;
    if(data.length>25){
        data=data.slice(0,25);
        f=true;
    }
    return (
        <div>
            <BarChart
                width={f?60*data.length:500}
                height={300}
                data={data}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" allowDataOverflow={false} interval={0} tickFormatter={e=>f?e.substr(0,6):e}/>
                <YAxis dataKey="value"/>
                <Tooltip />
                <ReferenceLine y={0} stroke="#000" />
                <Bar dataKey="value" fill="#8884d8" >
                    {data.map((entry, index) => (<Cell key={`cell-${index}`} fill={'#'+(Math.random()*0xFFFFFF<<0).toString(16)} />))}
                </Bar>
                {/* <Bar dataKey="uv" fill="#82ca9d" /> */}
            </BarChart>
            
        </div>
    )
}

export const BarGraphSingle = data => {
    return (
        <div>
            <BarChart
                width={500}
                height={300}
                data={data}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
            >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <ReferenceLine y={0} stroke="#000" />
                <Bar dataKey="value" fill="#8884d8" />
                {/* <Bar dataKey="uv" fill="#82ca9d" /> */}
            </BarChart>
            
        </div>
    )
}

export const BarGraphStacked = ({data}) => {
    return (
        <div>
            <BarChart
                width={500}
                height={300}
                data={data}
                margin={{
                    top: 20,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" />
                <YAxis />
                <Tooltip />
                <Legend />
                <Bar dataKey="non-covid" stackId="a" fill="#8884d8" />
                <Bar dataKey="covid" stackId="a" fill="#82ca9d" />
            </BarChart>
            
        </div>
    )
}

export default BarGraphGen
