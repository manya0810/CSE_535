import React from "react";
import { Tooltip, Treemap } from "recharts";

const CustomizedContent = (props) => {
    const { root, depth, x, y, width, height, index, name, value } = props;
    return (
      <g>
        <rect
          x={x}
          y={y}
          width={width}
          height={height}
          style={{
            fill:'#'+(Math.random()*0xFFFFFF<<0).toString(16),
            stroke: "#fff",
            strokeWidth: 2 / (depth + 1e-10),
            strokeOpacity: 1 / (depth + 1e-10)
          }}
        />
        {depth === 1 ? (
          <text
            x={x + width / 2}
            y={y + height / 2 + 7}
            textAnchor="middle"
            fill="#fff"
            fontSize='14px'
            fontFamily="Garamond, serif"
          >
            {name}
          </text>
        ) : null}
      </g>
    );
  };

const CustomTooltip = ({ active, payload, label }) => {
    if (active) {
      return (
        <div className="custom-tooltip"  style={{color: 'black',background: 'white'}}>
          <p className="label">{`${payload[0].payload.name} : ${payload[0].value.toFixed(3)}`}</p>
        </div>
      );
    }
  
    return null;
  };

export default function TreeMapGen({data}) {
  let formattedData = []
  data.forEach(d => {
      if(d.value>0.02){
          formattedData.push(d);
      }
  });  
  return (
    <Treemap
      width={400}
      height={200}
      data={formattedData}
      dataKey="value"
      ratio={4 / 3}
      stroke="#fff"
      fill="#8884d8"
      content={<CustomizedContent />}
    >
        {/* <Tooltip content={CustomTooltip}/> */}
    </Treemap>
  );
}

export function TreeMapDefault({data, color}) {
    console.log(color)
    let formattedData = []
    data.forEach(d => {
        if(d.value>0.02){
            formattedData.push(d);
        }
    });  
    return (
      <Treemap
        width={400}
        height={200}
        data={formattedData}
        dataKey="value"
        ratio={4 / 3}
        stroke="#fff"
        fill={color}
      >
          <Tooltip content={CustomTooltip}/>
      </Treemap>
    );
  }
