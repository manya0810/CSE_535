import React from 'react'
import { Card, CardActionArea, CardContent, Typography } from '@mui/material'

const Tweet = ({ tweet }) => {
    return (
        <Card sx={{maxHeight: '200px', margin: '2px' }}>
            <CardActionArea>
                <CardContent>
                    <Typography gutterBottom component="div">
                        {tweet.poi_name?<div style={{textAlign: 'left'}}><b>@{tweet.poi_name}</b></div>:''}
                        <p style={{textAlign: 'left'}}>{tweet.tweet_text}</p>
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {`${tweet.country} | ${tweet.tweet_date} | ${tweet.sentiment} | ${tweet.sentiment_score}`}
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
    )
}

export default Tweet
