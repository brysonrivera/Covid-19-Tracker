import React, { useRef, useState } from 'react';
import PathogenImage from './img/pathogen.jpg'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

const HomePage = () => {

    const [zipCode, setZipCode] = useState();
    const tempZip = useRef();
    const [invalidZip, setInvalidZip] = useState(false);

    const setZIP = (e) => {
        e.preventDefault();
        console.log(tempZip.current.value)
        tempZip.current.value = ''
    }

    return (
        <div>
            <header>
                <h1>COVID-19 Tracker</h1>
                <p>Please enter a ZIP Code to get information about COVID-19 in this area.</p>
            </header>
            <div className='pathogen' style={{
                background: `url(${PathogenImage})`,
                backgroundColor: 'black',
                height: '100vh',
                backgroundSize: 'cover',
                display: 'flex',
                justifyContent: 'center'
            }}>
                <div className='form-outer-container'>
                    <Form.Group className="form-inner-container mb-3" controlId="formBasicEmail">
                        <Form.Label>ZIP Code</Form.Label>
                        <Form.Control type="number" ref={tempZip} placeholder="Enter ZIP Code" />
                        <Form.Text className="text-muted">
                            Submit to get Results
                        </Form.Text>
                        <Button onClick={(e) => setZIP(e)} className='form-item' variant="light" size='lg'>Submit</Button>
                    </Form.Group>
                </div>



            </div>

        </div >
    )
}
export default HomePage;