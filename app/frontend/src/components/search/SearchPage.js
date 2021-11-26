import axios from 'axios'
import React, {useState} from 'react'
import Navbar from '../navbar/Navbar'
import './SearchPage.css'

const url = 'http://127.0.0.1:5000'

const SearchPage = () => {
    const [tweets, setTweets] = useState([])
    const handleFormSubmit = async (e) => {
        e.preventDefault();
        const query=e.target.elements.query?.value;
        const poi=e.target.elements.poi?.value?'&poi='+e.target.elements.poi?.value:'';
        const country=e.target.elements.country?.value?'&country='+e.target.elements.country?.value:'';
        const language=e.target.elements.language?.value?'&language='+e.target.elements.language?.value:'';
        const topic=e.target.elements.topic?.value?'&topic='+e.target.elements.topic?.value:'';
        const params = `query=${query}${poi}${country}${language}${topic}`;
        const encodedUrl = encodeURI(url+'/api/search?'+params);
        const res = await axios.get(encodedUrl);
        if (res.data){
            console.log(res.data.tweets)
            setTweets(res.data.tweets)
        }
        
    }
    return (
        <div>
            <Navbar />
            <form className="form" onSubmit={handleFormSubmit}>
                <div className="formField filters">
                    <div className="filtersText fbox">Filters:</div>
                    <div className="filtersContainer fbox">
                        <select id="poi" className="select">
                            <option value="" selected>POI...</option>
                            <option value="modi">Modi</option>
                            <option value="biden">Biden</option>
                        </select>
                        <select id="country" className="select">
                            <option value="" selected>Country...</option>
                            <option value="india">India</option>
                            <option value="usa">USA</option>
                            <option value="mexico">Mexico</option>
                        </select>
                        <select id="language" className="select">
                            <option value="" selected>Language...</option>
                            <option value="english">English</option>
                            <option value="hindi">Hindi</option>
                            <option value="spanish">Spanish</option>
                        </select>
                        <select id="topic" className="select">
                            <option value="" selected>Topic...</option>
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
            <br/>
            <div className='result'>
                <div className='tweets'>
                    {tweets.map((tweet,index) => (
                        <div className='tweetFields'>
                            <hr/>
                            <div><h4>@{tweet.poi_name}</h4></div>
                            <div>{tweet.tweet_text}</div>
                        </div>
                    ))}
                </div>
                <div class="vl"></div>
                <div className='analysis'>
                    {tweets.length>0?<h3>Analysis</h3>:''}
                </div>
            </div>
        </div>
    )
}

export default SearchPage
