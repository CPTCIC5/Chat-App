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
        setFormData({
          ...formData,
          [e.target.name]: e.target.value,
        });
    };
    
    const handleSubmit = async (e) =>{
        e.preventDefault()
        try {
            const response = await axios.post('http://127.0.0.1:8000/users/register/', {
            username: formData.username,
            email: formData.email,
            password: formData.password,
            confirm_password : formData.confirm_password
            });
            console.log(response.data); // Do something with the response
        } catch (error) {
            console.error('Error submitting the form:', error);
        }
    };
    
    
    return (
        <>
        <form method="post">
        <input type="text" name="username" id="username" placeholder='Username' onChange={handleInputChange}/>
        <input type="email" name="email" id="email" placeholder='Email' onChange={handleInputChange}/>
        <input type="password" name="password" id="password" placeholder='Password' onChange={handleInputChange}/>
        <input type="password" name="confirm_password" id="confirm_password" placeholder='Confirm-Password' onChange={handleInputChange}/>
        <button type="submit" value="Submit">Submit</button>
        </form>
        </>
    )
}

