import React from 'react'
import BarGraphGen from '../../utils/BarGraphs'
import { countries, covidRate, englishTopics, hindiTopics, languages, poi, spanishTopics, tweetsPerDay, vaccination } from '../../utils/Data'
import { DateLineChart, TripleLineChart } from '../../utils/LineCharts'
import PieChartGen from '../../utils/PieChart'
import TreeMapGen, { TreeMapDefault } from '../../utils/TreeMaps'
import Navbar from '../navbar/Navbar'
import './Overview.css'

const Overview = () => {
    return (
        <div>
            <Navbar />
            <div className='overview'>
                <div className='topics'>
                    <div>
                        <h3>English Topics</h3>
                        <TreeMapGen data={englishTopics}/>
                    </div>
                    <div>
                        <h3>Hindi Topics</h3>
                        <TreeMapDefault data={hindiTopics} color='#002874'/>
                    </div>
                    <div>
                        <h3>Spanish Topics</h3>
                        <TreeMapDefault data={spanishTopics} color='#00744E'/>
                    </div>
                </div>
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
