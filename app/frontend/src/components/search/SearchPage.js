import axios from 'axios'
import React, {useState} from 'react'
import CarouselGen, { VideoCarousel } from '../../utils/Carousel'
import Navbar from '../navbar/Navbar'
import './SearchPage.css'
import LinearProgress from '@mui/material/LinearProgress';
import Pagination from '@mui/material/Pagination';
import { Card, CardActionArea, CardContent, Typography } from '@mui/material'

const url = 'http://127.0.0.1:5000'

const SearchPage = () => {
    const [tweets, setTweets] = useState([])
    const [news, setNews] = useState([])
    const [wiki, setWiki] = useState("")
    const [videos, setVideos] = useState([])
    // const [page, setPage] = useState(1)
    const [currentItems, setCurrentItems] = useState([])

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
            setTweets(res.data.tweets)
            setNews(res.data.news)
            setWiki(res.data.wiki)
            setVideos(res.data.videos)
            setCurrentItems(res.data.tweets.slice(0,10))
        }
        progressBar.style.display = 'none';
        
    }

    const handlePageChange = v => {
        // setPage(v);
        setCurrentItems(tweets.slice((v-1)*10,v*10))
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
                <div style={{width:'30vw',height:'250px'}}>
                    <h4>News</h4>
                    <CarouselGen items={news}/>
                </div>
                <div style={{width:'30vw',height:'250px'}}>
                    <h4>Videos</h4>
                    <VideoCarousel items={videos}/>
                </div>
                <div style={{width:'40vw',height:'250px'}}>
                    <h4>Wikipedia</h4>
                    <Card sx={{margin: '8px', maxHeight: '250px' }}>
                        <CardContent>
                            <Typography gutterBottom component="div">
                                {wiki}
                            </Typography>
                        </CardContent>
                    </Card>
                </div>
            </div>
            <div className='result'>
                <div className='tweets'>
                    <h3>Tweets</h3>
                    {currentItems.map((tweet,index) => (
                        <Card sx={{maxHeight: '200px', margin: '2px' }}>
                            <CardActionArea>
                                <CardContent>
                                    <Typography gutterBottom component="div">
                                        {tweet.poi_name?<div style={{textAlign: 'left'}}><b>@{tweet.poi_name}</b></div>:''}
                                        <p style={{textAlign: 'left'}}>{tweet.tweet_text}</p>
                                    </Typography>
                                </CardContent>
                            </CardActionArea>
                        </Card>
                        // <div className='tweetFields' key={index}>
                        //     <hr/>
                        //     {tweet.poi_name?<div><h4>@{tweet.poi_name}</h4></div>:''}
                        //     <div>{tweet.tweet_text}</div>
                        // </div>
                    ))}
                </div>
                <div className="vl"></div>
                <div className='analysis'>
                    {tweets.length>0?<h3>Analysis</h3>:''}
                </div>
            </div>
            <Pagination count={5} onChange={(e,v)=>handlePageChange(v)}/>
            </div>
        </div>
    )
}

export default SearchPage
