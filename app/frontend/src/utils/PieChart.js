import React from 'react'
import { PieChart, Pie, Tooltip, Cell } from 'recharts';

const customLabel = entry => `${entry.name} - ${entry.value}`

const colors=['#BA1717','#00744E','#002874']

const PieChartGen = ({ data }) => {
    return (
        <div>
            <PieChart width={500} height={400}>
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
                    <Cell key={`cell-${index}`} fill={colors[index]} />
                    ))}
                </Pie>
                <Tooltip />
            </PieChart>
        </div>
    )
}

export default PieChartGen
