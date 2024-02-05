import axios from 'axios';
import './Register.css'
import React, {useState} from 'react';


export default function Register()
{
    const [registerData,setRegisterData] = useState({
        username: '',
        email : '',
        password: '',
        confirm_password : ''
        
    })
    const handleInputChange = (e) => {
        setRegisterData({
          ...registerData,
          [e.target.name]: e.target.value,
        });
    };
    
    const handleSubmit = async (e) =>{
        e.preventDefault()
        //aren't we doing it from backend side? or should we do b, yes
        // but its better to do it in the frontend and not do it in the backend
        //sure
        // check if password === confirm_password
        // if password is different than confirm_password, show an error
        if (registerData.confirm_password !== registerData.password) {
            // show an error msg or something...
            return;
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/users/register/', {
            username: registerData.username,
            email: registerData.email,
            password: registerData.password,
            confirm_password : registerData.confirm_password
            });
            console.log(response.data); // Do something with the response
            alert("created")
        } catch (error) {
            console.error('Error submitting the form:', error);
        }
    };
    
    
    return (
        <form onSubmit={handleSubmit}>
            <input type="text" name="username" id="username" placeholder='Username' onChange={handleInputChange}/>
            <input type="email" name="email" id="email" placeholder='Email' onChange={handleInputChange}/>
            <input type="password" name="password" id="password" placeholder='Password' onChange={handleInputChange}/>
            <input type="password" name="confirm_password" id="confirm_password" placeholder='Confirm-Password' onChange={handleInputChange}/>
            <button type="submit" value="Submit">Submit</button>
        </form>
    )
}

