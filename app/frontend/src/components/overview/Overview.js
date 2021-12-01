import React from 'react'
import BarGraphGen from '../../utils/BarGraphs'
import { countries, languages, poi } from '../../utils/Data'
import PieChartGen from '../../utils/PieChart'
import Navbar from '../navbar/Navbar'
import './Overview.css'

const Overview = () => {
    return (
        <div>
            <Navbar />
            <div className='overview'>
                <div>
                    <h3>POI vs No. of tweets</h3>
                    <BarGraphGen data={poi}/>
                </div>
                <div className='suboverview'>
                    <div>
                        Country wise tweets
                        <BarGraphGen data={countries}/>
                    </div>
                    <div>
                        Language based tweets
                        <BarGraphGen data={languages}/>
                    </div>
                </div>
                <div>
                    <h3>Dummy</h3>
                    <PieChartGen />
                </div>
            </div>
            
        </div>
    )
}

export default Overview
