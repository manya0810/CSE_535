import React from "react";
import { Tooltip, Treemap } from "recharts";

const COLORS = [
    "#a83232",
    "#a87d32",
    "#9ca832",
    "#6fa832",
    "#32a842",
    "#32a87d",
    "#3296a8",
    "#3240a8",
    "#5532a8",
    "#a8328c"
  ];

const CustomizedContent = (props) => {
    const { root, depth, x, y, width, height, index, name, value, colors } = props;
    return (
        <g>
        <rect
          x={x}
          y={y}
          width={width}
          height={height}
          style={{
            fill:
              depth < 2
                ? colors[index]
                : "none",
            stroke: "#fff",
            strokeWidth: 2 / (depth + 1e-10),
            strokeOpacity: 1 / (depth + 1e-10)
          }}
        />
        {/* {depth === 1 ? (
          <text
            x={x + width / 2}
            y={y + height / 2 + 7}
            textAnchor="middle"
            fill="#fff"
            fontSize={14}
          >
            {name}
          </text>
        ) : null} */}
        {depth === 1 ? null : (
          <text
            x={x + width / 2}
            y={y + height / 2 + 7}
            textAnchor="middle"
            fill="#fff"
            fontSize={14}
          >
            {name}
          </text>
        )}
      </g>
    );
  };

const CustomTooltip = ({ active, payload, label }) => {
    if (active) {
      return (
        <div className="custom-tooltip"  style={{color: 'black', background: 'white'}}>
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
      width={600}
      height={300}
      data={data}
      dataKey="value"
      ratio={4 / 3}
      stroke="#fff"
      fill="#8884d8"
      content={<CustomizedContent  colors={COLORS} />}
    >
        {/* <Tooltip content={CustomTooltip}/> */}
    </Treemap>
  );
}

export function TreeMapDefault({data, color}) {
    let formattedData = []
    data.forEach(d => {
        if(d.value>0.02){
            formattedData.push(d);
        }
    });  
    return (
      <Treemap
        width={600}
        height={300}
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
