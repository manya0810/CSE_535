import React, {useState} from 'react'
import { Box, Button, Card, CardActions, CardContent, Paper, Tooltip, Typography } from '@mui/material'
import SentimentNeutralIcon from '@mui/icons-material/SentimentNeutral';
import SentimentSatisfiedAltIcon from '@mui/icons-material/SentimentSatisfiedAlt';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';

const getSentimentIcon = (sentiment, score) => {
    if (sentiment){
        if (sentiment == 'Neutral'){
            return (<Tooltip title={`${sentiment} : ${score}`}>
                <SentimentNeutralIcon color="primary"/>
                </Tooltip>) 
        } else if (sentiment == 'Positive'){
            return (<Tooltip title={`${sentiment} : ${score}`}>
                    <SentimentSatisfiedAltIcon color="success"/>
                </Tooltip>) 
        }  else if (sentiment == 'Negative'){
            return (<Tooltip title={`${sentiment} : ${score}`}>
                    <SentimentVeryDissatisfiedIcon sx={{ color: 'red' }}/>
                </Tooltip>) 
        }
    }
}

const options = {month: 'short', day: 'numeric' };

const dateFormatter = date => {
    return (new Date(date)).toLocaleDateString("en-US", options);
};

const Tweet = ({ tweet }) => {
    const [show, setShow] = useState(false);
    return (
        <Card sx={{ margin: '2px' }} raised>
            <CardContent>
                <Typography gutterBottom component="div">
                    {tweet.poi_name?<div style={{textAlign: 'left'}}><b>@{tweet.poi_name}</b></div>:''}
                    <p style={{textAlign: 'left'}}>{tweet.tweet_text}</p>
                </Typography>
                <Box sx={{ display: 'inline-flex',  flexDirection: 'row' }}>
                    <Typography sx={{width:'125px'}} variant="body2" color="text.secondary">
                        {tweet.country?`${tweet.country} | `:``} {tweet.tweet_date?`${dateFormatter(tweet.tweet_date)} | `:``}
                    </Typography>
                    <Typography sx={{width:'20px'}} >
                        {getSentimentIcon(tweet.sentiment, tweet.sentiment_score)}
                    </Typography>
                </Box>
                <CardActions>
                    {tweet.replies?<Button size="small" onClick={()=>{setShow(!show)}}>{show?"Hide Replies":"View Replies"}</Button>:""}
                </CardActions>
                <Paper style={{maxHeight: 400, overflow: 'auto'}}>
                    {show?tweet.replies?.map((tweet,index) => (
                        <Tweet tweet={tweet} />
                    )):""}
                </Paper>
            </CardContent>
        </Card>
    )
}

export default Tweet
