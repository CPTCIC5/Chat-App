// Chat.jsx

import React, { useState } from 'react';
import './Chat.css';
import axios from 'axios';



const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');

  const handleSendMessage = () => {
    if (newMessage.trim() !== '') {
      const currentTime = new Date().toLocaleTimeString();
      const newMessageObject = {
        username: 'User', // Replace with the actual username (you can get it from user authentication)
        text: newMessage,
        time: currentTime,
      };

      setMessages([...messages, newMessageObject]);
      setNewMessage('');
    }
  };

  return (
    <div className="chat-container">
      <div className="chat-messages">
        {messages.map((message, index) => (
          <div key={index} className="message">
            <span className="username">{message.username}</span>
            <span className="time">{message.time}</span>
            <p className="text">{message.text}</p>
          </div>
        ))}
      </div>

      <div className="chat-input">
        <input
          type="text"
          placeholder="Type your message..."
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>
    </div>
  );
};

export default Chat;
