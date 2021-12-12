import axios from 'axios'
import React, {useState} from 'react'
import CarouselGen, { VideoCarousel } from '../../utils/Carousel'
import Navbar from '../navbar/Navbar'
import './SearchPage.css'
import LinearProgress from '@mui/material/LinearProgress';
import Pagination from '@mui/material/Pagination';
import { Card, CardActionArea, CardContent, Typography } from '@mui/material'
import Tweet from './Tweet'
import PieChartGen from '../../utils/PieChart'

const url = 'http://127.0.0.1:5000'

const formatPieData = ({INDIA, MEXICO, USA}) => ([
    {'name': 'USA', 'value': USA},
    {'name': 'MEXICO', 'value': MEXICO},
    {'name': 'INDIA', 'value': INDIA}
])

const formatReplies = uTweets => {
    let formattedTweets = []
    uTweets.forEach(t=>{
        if (t.replies){
            let i=0
            let temp=t
            let tR=[]
            while(i<t.replies.length){
                let r={}
                r['tweet_lang']=t.replies[i++]
                r['tweet_text']=t.replies[i++]
                r['tweet_date']=t.replies[i++]
                r['sentiment']=t.replies[i++]
                r['sentiment_score']=t.replies[i++]
                tR.push(r)
            }
            temp.replies=tR
            formattedTweets.push(temp)
        } else {
            formattedTweets.push(t)
        }
    })
    console.log(formattedTweets)
    return formattedTweets
}

const SearchPage = () => {
    const [tweets, setTweets] = useState([])
    const [poiTweets, setPoiTweets] = useState([])
    const [news, setNews] = useState([])
    const [wiki, setWiki] = useState("")
    const [wikiUrl, setWikiUrl] = useState("")
    const [videos, setVideos] = useState([])
    const [countryWiseGen, setCountryWiseGen] = useState([])
    const [countryWisePoi, setCountryWisePoi] = useState([])
    const [currentItems, setCurrentItems] = useState([])
    const [currentPoiItems, setCurrentPoiItems] = useState([])

    const Analysis = () =>(
        <div className='analysis'>
            <h3>Analysis</h3>
            <div style={{display: 'flex', justifyContent: 'center'}}>
                <div>
                    <h3>Country wise POI tweets</h3>
                    <PieChartGen data={countryWisePoi} />
                </div>
                <div>
                    <h3>Country wise general tweets</h3>
                    <PieChartGen data={countryWiseGen} />
                </div>
            </div>
        </div>
    )
    
    const NewsComp = () => (
        <div style={{width:'30vw',height:'250px'}}>
            <h4>News</h4>
            <CarouselGen items={news}/>
        </div>
    );

    const VideoComp = () => (
        <div style={{width:'30vw',height:'250px'}}>
            <h4>Videos</h4>
            <VideoCarousel items={videos}/>
        </div>
    );

    const WikiComp = () => (
        <div style={{width:'40vw',height:'250px'}}>
            <h4>Wikipedia</h4>
            <Card sx={{margin: '8px', maxHeight: '250px' }}>
                <CardContent>
                    <Typography gutterBottom component="div">
                        {wiki}
                    </Typography>
                </CardContent>
            </Card>
            <a href={wikiUrl} target="_blank">Read More</a>
        </div>
    );

    const handleFormSubmit = async (e) => {
        e.preventDefault();
        let progressBar = document.getElementById('progressBar');
        progressBar.style.display = 'block';
        const query=e.target.elements.query?.value;
        const poi=e.target.elements.poi?.value?'&poi='+e.target.elements.poi?.value:'';
        const country=e.target.elements.country?.value?'&country='+e.target.elements.country?.value:'';
        const language=e.target.elements.language?.value?'&language='+e.target.elements.language?.value:'';
        const topic=e.target.elements.topic?.value?'&topic='+e.target.elements.topic?.value:'';
        const params = `query=${query}${poi}${country}${language}${topic}`;
        const encodedUrl = encodeURI(url+'/api/search?'+params);
        const res = await axios.get(encodedUrl);
        document.getElementById('searchResults').style.display = 'block';
        if (res.data){
            var formattedTweets = formatReplies(res.data.tweets)
            var formattedPoiTweets = formatReplies(res.data.poi_tweets)
            setTweets(formattedTweets)
            setNews(res.data.news)
            setWiki(res.data.wiki)
            setVideos(res.data.videos)
            setWikiUrl(res.data.wiki_url)
            setPoiTweets(formattedPoiTweets)
            setCountryWiseGen(formatPieData(res.data.gen_counts.country))
            setCountryWisePoi(formatPieData(res.data.poi_counts.country))
            setCurrentItems(formattedTweets.slice(0,10))
            setCurrentPoiItems(formattedPoiTweets.slice(0,10))
        }
        progressBar.style.display = 'none';
        
    }

    const handlePageChange = v => {
        // setPage(v);
        setCurrentItems(tweets.slice((v-1)*10,v*10))
        setCurrentPoiItems(poiTweets.slice((v-1)*10,v*10))
        window.scrollTo(0,document.body.scrollHeight);
    }

    return (
        <div>
            <Navbar />
            <form className="form" onSubmit={handleFormSubmit}>
                <div className="formField filters">
                    <div className="filtersText fbox">Filters:</div>
                    <div className="filtersContainer fbox">
                        <select id="poi" className="select">
                            <option value="">POI...</option>
                            <option value="modi">Modi</option>
                            <option value="biden">Biden</option>
                        </select>
                        <select id="country" className="select">
                            <option value="">Country...</option>
                            <option value="india">India</option>
                            <option value="usa">USA</option>
                            <option value="mexico">Mexico</option>
                        </select>
                        <select id="language" className="select">
                            <option value="">Language...</option>
                            <option value="english">English</option>
                            <option value="hindi">Hindi</option>
                            <option value="spanish">Spanish</option>
                        </select>
                        <select id="topic" className="select">
                            <option value="">Topic...</option>
                            <option value="covid">Covid</option>
                            <option value="vaccine">Vaccine</option>
                        </select>
                    </div>
                </div>
                <div className="formField search">
                    <input type='text' id='query' className="searchBar" placeholder="Search Tweets" required/>
                    <button  className="searchButton">Search</button>
                </div>
            </form>
            <div id='progressBar' style={{display: 'none'}}>
                <LinearProgress />
            </div>
            <div id='searchResults' style={{display:'none'}}>
            <div className='extras' style={{height:'350px'}}>
                {news.length>0?<NewsComp/>:''}{videos.length>0?<VideoComp/>:''}{wiki?<WikiComp/>:''}
            </div>
            <div className='result'>
                <div className='tweets'>
                    <h3>POI Tweets</h3>
                    {currentPoiItems.map((tweet,index) => (
                        <Tweet tweet={tweet} />
                    ))}
                </div>
                <div className="vl"></div>
                <div className='tweets'>
                    <h3>Non-POI Tweets</h3>
                    {currentItems.map((tweet,index) => (
                        <Tweet tweet={tweet} />
                    ))}
                </div>
            </div>
            <Pagination count={5} onChange={(e,v)=>handlePageChange(v)}/>
            </div>
            {tweets.length>0?<Analysis/>:''}
                
        </div>
    )
}

export default SearchPage
