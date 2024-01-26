import './Register.css'
import React from 'react';

export default function Register()
{
    return (
        <>
        <form method="post">
        <input type="text" name="username" id="username" placeholder='Username' />
        <input type="" name="email" id="email" placeholder='Email' />
        <input type="password" name="password" id="password" placeholder='Password' />
        <input type="password" name="confirm_password" id="confirm_password" placeholder='Confirm-Password' />
        <button type="submit" value="Submit">Submit</button>
        </form>
        </>
    )
}