import React, { useState } from 'react';
import axios from 'axios';
import './Login.css';

export default function Login() {
  const [formData, setFormData] = useState({
    username: '',
    password: '',
  });

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://127.0.0.1:8000/users/login/', {
        username: formData.username,
        password: formData.password,
      });
      console.log(response.data); // Do something with the response
      alert("Logged In!")
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
  };

  return (
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          name="username"
          id="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleInputChange}
        />
        <input
          type="password"
          name="password"
          id="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleInputChange}
        />
        <input type="submit" value="Submit" />
      </form>
  );
}
