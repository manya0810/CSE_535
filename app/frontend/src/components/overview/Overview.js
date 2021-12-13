import React from 'react'
import BarGraphGen, { BarGraphStacked } from '../../utils/BarGraphs'
import { countries, covidRate, englishTopics, englishTopicsMulti, englishTopicsMulti2, hindiTopics, hindiTopicsMulti, languages, misInfoEng, misInfoEsp, poi, poiCovidInd, poiCovidMex, poiCovidUS, sentimentAll, spanishTopics, spanishTopicsMulti, tweetsPerDay, vaccHesEng, vaccHesEsp, vaccination } from '../../utils/Data'
import { DateLineChart, SingleLineChart, TripleLineChart } from '../../utils/LineCharts'
import PieChartGen from '../../utils/PieChart'
import TreeMapGen, { TreeMapDefault } from '../../utils/TreeMaps'
import Navbar from '../navbar/Navbar'
import './Overview.css'

const Overview = () => {
    return (
        <div>
            <Navbar />
            <div className='overview' style={{paddingBottom: '50px'}}>
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
                <h3 style={{marginTop:'60px'}}>Effect on vaccination rate with POI tweets</h3>
                <h3>USA</h3>
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>POI Tweets</h3>
                        <BarGraphStacked data={poiCovidUS} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='usa' />
                    </div>
                </div>
                <h3>India</h3>
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>POI Tweets</h3>
                        <BarGraphStacked data={poiCovidInd} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='india'/>
                    </div>
                </div>
                <h3>Mexico</h3>
                <div style={{width:'80%', display:'flex'}}>
                    <div>
                        <h3>POI Tweets</h3>
                        <BarGraphStacked data={poiCovidMex} />
                    </div>
                    <div style={{width:'50%'}}>
                        <h3>Vaccination Rate</h3>
                        <SingleLineChart data={vaccination} country='mexico'/>
                    </div>
                </div>
                <div>
                    <h3 style={{marginTop:'60px'}}>Sentiment of all tweets</h3>
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
                <h3 style={{marginTop:'60px'}}>Misinformation</h3>
                <div className='topics'>
                    <div>
                        <h3>English</h3>
                        <TreeMapGen data={misInfoEng} />
                    </div>
                    <div style={{marginLeft: '32px'}}>
                        <h3>Spanish</h3>
                        <TreeMapGen data={misInfoEsp} />
                    </div>
                </div>
                <h3 style={{marginTop:'60px'}}>Vaccine Hesitancy</h3>
                <div className='topics'>
                    <div>
                        <h3>English</h3>
                        <TreeMapGen data={vaccHesEng} />
                    </div>
                    <div style={{marginLeft: '32px'}}>
                        <h3>Spanish</h3>
                        <TreeMapGen data={vaccHesEsp} />
                    </div>
                </div>
            </div>
            
        </div>
    )
}

export default Overview
