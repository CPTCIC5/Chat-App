import React, { useState, useEffect } from 'react';
import axios from 'axios';
// import MessageList from './MessageList'; 

function MessageListPage() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:8000/message/';

    axios.get(apiUrl)
      .then(response => {
        setMessages(response.data);
      })
      .catch(error => {
        console.error('Error fetching messages:', error);
      });
  }, []); 

  return (
    <div className="message-list-page">
      {/* <MessageList messages={messages} /> */}
    </div>
  );
}

export default MessageListPage;
