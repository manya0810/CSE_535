import React from 'react'
import BarGraphGen from '../../utils/BarGraphs'
import { countries, covidRate, languages, poi, tweetsPerDay, vaccination } from '../../utils/Data'
import { DateLineChart, TripleLineChart } from '../../utils/LineCharts'
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
                        <PieChartGen data={countries}/>
                    </div>
                    <div>
                        Language based tweets
                        <PieChartGen data={languages}/>
                    </div>
                </div>
                <div style={{width:'80%'}}>
                    <h3>Covid cases per day</h3>
                    <TripleLineChart data={covidRate} />
                </div>
                <div style={{width:'80%'}}>
                    <h3>Vaccination Rate</h3>
                    <TripleLineChart data={vaccination} />
                </div>
                <div style={{width:'80%'}}>
                    <h3>Tweets per day</h3>
                    <DateLineChart data={tweetsPerDay} />
                </div>
            </div>
            
        </div>
    )
}

export default Overview
