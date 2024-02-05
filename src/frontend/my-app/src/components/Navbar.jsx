import React from 'react';

function Navbar() 
{
  return (
    <header>
      <nav>
        <ul>
          <li>
            <a href="/login">Login</a>
          </li>
          <li>
            <a href="#chat">Chat</a>
          </li>
          <li>
            <a href="/register">Register</a>
          </li>
        </ul>
      </nav>
    </header>
  );
}

export default Navbar;