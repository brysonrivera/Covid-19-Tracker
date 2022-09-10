import React from 'react';
import PathogenImage from './img/pathogen.jpg'

const HomePage = () => {
    return (
        <div>
            <div className='pathogen' style={{
                background: `url(${PathogenImage})`,
                width: '100%',
                height: '100vh',
                backgroundSize: 'cover'
            }} />
        </div>
    )
}
export default HomePage;