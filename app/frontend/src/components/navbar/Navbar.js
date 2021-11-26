import React from 'react'
import { Link, useLocation  } from "react-router-dom";

import "./Navbar.css";

const Navbar = () => {
    const location = useLocation();
    let searchClass = "";
    let overviewClass = "";
    if (location.pathname == '/') {
        searchClass = 'selected'
        overviewClass = ''
    } else if (location.pathname == '/overview') {
        searchClass = ''
        overviewClass = 'selected'
    }
    return (
        <div>
            <header className='navbar'>
                <div className='navbar__title'>Arachnids</div>
                <Link to="/" id={searchClass} className='link'>
                    <div className='navbar__item'>Search</div>
                </Link>
                <Link to="/overview"  id={overviewClass} className='link'>
                    <div className='navbar__item'>Overview</div>
                </Link>
            </header>
        </div>
    )
}

export default Navbar
