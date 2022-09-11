import React, { useRef, useState, useEffect } from 'react';
import PathogenImage from './img/pathogen.jpg'
import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';
import axios from 'axios';

const covidURL = "http://127.0.0.1:8000/covid"

const HomePage = () => {

    const [zipCode, setZipCode] = useState();
    const [cases, setCases] = useState([]);
    const tempZip = useRef();
    const [invalidZip, setInvalidZip] = useState(false);
    const [message, setMessage] = useState("");

    const setZIP = (e) => {
        e.preventDefault();
        setZipCode(tempZip.current.value);
        tempZip.current.value = '';
    }

    useEffect(() => {
        const getData = async () => {
            try {
                const res = await axios.get(`http://127.0.0.1:8000/covid/casesPer100k?zip_code=${zipCode}`);
                console.log(res);
                setCases(res)
            } catch (error) {
                console.log(error);
                setMessage("Invalid ZIP Code. Please Try Again.");
                setInvalidZip(!invalidZip);
            }

        }
        if (zipCode !== undefined) getData()

    }, [zipCode])


    useEffect(() => {
        console.log(cases)

    }, [cases])

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
            {cases.length > 0 &&
                <div>
                    {
                        cases.map((cas) => {
                            return (
                                <h1>{cas.covid_cases_per_100k}</h1>
                            )
                        })
                    }
                </div>
            }
        </div >
    )
}
export default HomePage;