import React, {useState} from 'react'
import { Box, Button, Card, CardActionArea, CardActions, CardContent, Paper, Typography } from '@mui/material'
import SentimentNeutralIcon from '@mui/icons-material/SentimentNeutral';
import SentimentSatisfiedAltIcon from '@mui/icons-material/SentimentSatisfiedAlt';
import SentimentVeryDissatisfiedIcon from '@mui/icons-material/SentimentVeryDissatisfied';

const getSentimentIcon = sentiment => {
    if (sentiment){
        if (sentiment == 'Neutral'){
            return <SentimentNeutralIcon color="primary"/>
        } else if (sentiment == 'Positive'){
            return <SentimentSatisfiedAltIcon color="success"/>
        }  else if (sentiment == 'Negative'){
            return <SentimentVeryDissatisfiedIcon sx={{ color: 'red' }}/>
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
                    <Typography sx={{width:'100px'}} variant="body2" color="text.secondary">
                        {tweet.country?`${tweet.country} | `:``} {tweet.tweet_date?`${dateFormatter(tweet.tweet_date)} | `:``}
                    </Typography>
                    <Typography sx={{width:'20px'}} >
                        {getSentimentIcon(tweet.sentiment)}
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
