import React, { useState } from 'react';
import axios from 'axios';

function MessageInputPage() {
  const [messages, setMessages] = useState({
    text:''
  });

  const handleSendMessage = (newMessageObject) => {
    setMessages({...messages, 
        [newMessageObject.target.name]: newMessageObject.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('ws://127.0.0.1:8000/ws/chat/', {
        text: messages.text,
      });
      console.log(response.data); // Do something with the response
      alert("Msg  Delivered!")
    } catch (error) {
      console.error('Error submitting the form:', error);
    }
  };

  return (
    <form onSubmit={handleSubmit}>
        <input
        type="text"
        id="text"
        name='text'
        placeholder='Text'
        value={messages.text}
        onChange={handleSendMessage}
        />
        <input type="submit" value="Submit" />
    </form>
  );
}

export default MessageInputPage;
