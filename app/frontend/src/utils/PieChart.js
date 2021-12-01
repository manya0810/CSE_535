import React from 'react'
import { PieChart, Pie, Tooltip, Cell } from 'recharts';

const data = [
    { name: 'Group A', value: 400 },
    { name: 'Group B', value: 300 },
    { name: 'Group C', value: 300 },
    { name: 'Group D', value: 200 },
    { name: 'Group E', value: 278 },
    { name: 'Group F', value: 189 },
  ];

const customLabel = entry => `${entry.name} - ${entry.value}`

const PieChartGen = () => {
    return (
        <div>
            <PieChart width={1000} height={400}>
                <Pie
                    dataKey="value"
                    data={data}
                    cx={200}
                    cy={200}
                    outerRadius={80}
                    label={customLabel}
                >
                    {data.map((entry, index) => (
                    // <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                    <Cell key={`cell-${index}`} fill={'#'+(Math.random()*0xFFFFFF<<0).toString(16)} />
                    ))}
                </Pie>
                <Tooltip />
            </PieChart>
        </div>
    )
}

export default PieChartGen
