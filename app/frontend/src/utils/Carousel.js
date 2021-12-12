import React from 'react';
import Carousel from 'react-material-ui-carousel'
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import CardMedia from '@mui/material/CardMedia';
import Typography from '@mui/material/Typography';
import { CardActionArea } from '@mui/material';

function CarouselGen({ items })
{   
    return (
        <Carousel autoPlay={false} animation="slide" indicators={false}>
            {
                items.map( (item, i) => <Item key={i} item={item} /> )
            }
        </Carousel>
    )
}

function Item({ item })
{
    return (

        <Card sx={{ margin: '8px', height: '250px' }}>
            <CardActionArea onClick={()=>window.open(item.url, '_blank')}>
                <CardMedia
                    component="img"
                    height="80"
                    image={item.urlToImage}
                />
                <CardContent>
                    <Typography gutterBottom component="div">
                        {item.description}
                    </Typography>
                    <Typography variant="body2" color="text.secondary">
                        {item.source.name}
                    </Typography>
                </CardContent>
            </CardActionArea>
        </Card>
    )
}

export function VideoCarousel({ items })
{   
    return (
        <Carousel autoPlay={false} navButtonsAlwaysVisible animation="slide" indicators={false}>
            {
                items.map( (item, i) => <VideoItem key={i} item={item} /> )
            }
        </Carousel>
    )
}

function VideoItem({ item })
{
    return (

        <Card sx={{ margin: '8px', height: '250px' }}>
            <CardActionArea onClick={()=>window.open(item, '_blank')}>
                <CardMedia
                    component="img"
                    height="250px"
                    image={`https://img.youtube.com/vi/${item.substring(item.length-11)}/0.jpg`}
                />
            </CardActionArea>
        </Card>
    )
}

export default CarouselGen;
