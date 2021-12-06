import React from 'react'
import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    Legend,
    ResponsiveContainer
  } from "recharts";


const options = {month: 'short', day: 'numeric' };
const options2 = {month: 'short', day: 'numeric', year: 'numeric' };

const dateFormatter = date => {
    return (new Date(parseInt(date))).toLocaleDateString("en-US", options);
};

export const DateLineChart = ({ data }) => {
    let formattedData = [];
    let dict={};
    data.forEach(d => {
        let x = (new Date(d.name)).toLocaleDateString("en-US", options2);
        let y = (new Date(x)).getTime();
        if (y in dict){
            dict[y]+=d.value;
        } else {
            dict[y]=d.value;
        }
    });
    for (const date in dict){
        let d={'name':'','value':''};
        d.name=date;
        d.value=dict[date];
        formattedData.push(d);
    }
    formattedData.sort((a, b) => (a.name < b.name) ? 1 : -1)
    formattedData.forEach(d=>{
        d.name=dateFormatter(d.name);
    })
    return (
        <ResponsiveContainer width='100%' height={400}>
            <LineChart
                data={formattedData}
                margin={{
                    top: 5,
                    right: 30,
                    left: 20,
                    bottom: 5
                }}
                >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis dataKey="name" reversed/>
                <YAxis />
                <Tooltip />
                <Line
                    type="monotone"
                    dataKey="value"
                    stroke="#8884d8"
                    activeDot={{ r: 8 }}
                />
            </LineChart>
        </ResponsiveContainer>
    )
}

export const TripleLineChart = ({ data }) => {
    data.forEach(d => {
        let x = (new Date(d.name)).toLocaleDateString("en-US", options)
        // let y = (new Date(x)).getTime()
        // d.name=y
        d.name=x
    });
    return (
        <ResponsiveContainer width='100%' height={400}>
            <LineChart
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
                <Legend />
                <Line
                    type="monotone"
                    dataKey="usa"
                    stroke="red"
                    activeDot={{ r: 8 }}
                />
                <Line
                    type="monotone"
                    dataKey="india"
                    stroke="blue"
                    activeDot={{ r: 8 }}
                />
                <Line
                    type="monotone"
                    dataKey="mexico"
                    stroke="green"
                    activeDot={{ r: 8 }}
                />
            </LineChart>
        </ResponsiveContainer>
    )
}
