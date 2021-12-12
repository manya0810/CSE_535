import React from 'react'
import BarGraphGen, { BarGraphStacked } from '../../utils/BarGraphs'
import { countries, covidRate, englishTopics, englishTopicsMulti, englishTopicsMulti2, hindiTopics, hindiTopicsMulti, languages, poi, poiCovidInd, poiCovidMex, poiCovidUS, sentimentAll, spanishTopics, spanishTopicsMulti, tweetsPerDay, vaccination } from '../../utils/Data'
import { DateLineChart, SingleLineChart, TripleLineChart } from '../../utils/LineCharts'
import PieChartGen from '../../utils/PieChart'
import TreeMapGen, { TreeMapDefault } from '../../utils/TreeMaps'
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
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>USA</h3>
                        <BarGraphStacked data={poiCovidUS} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='usa' />
                    </div>
                </div>
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>India</h3>
                        <BarGraphStacked data={poiCovidInd} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='india'/>
                    </div>
                </div>
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>Mexico</h3>
                        <BarGraphStacked data={poiCovidMex} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='mexico'/>
                    </div>
                </div>
                <div>
                    <h3>Sentiment of all tweets</h3>
                    <PieChartGen data={sentimentAll} />
                </div>
                <div>
                    <h3>English Topics</h3>
                    <TreeMapGen data={englishTopicsMulti} />
                </div>
                <div className='topics'>
                    <div>
                        <h3>Hindi Topics</h3>
                        <TreeMapGen data={hindiTopicsMulti} />
                    </div>
                    <div style={{marginLeft: '32px'}}>
                        <h3>Spanish Topics</h3>
                        <TreeMapGen data={spanishTopicsMulti} />
                    </div>
                </div>
            </div>
            
        </div>
    )
}

export default Overview
