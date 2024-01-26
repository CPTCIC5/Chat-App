import React from 'react';
import Navbar from './components/Navbar.jsx';
import Footer from './components/Footer.jsx';
import Login from './components/login.jsx';
import Register from './components/Register.jsx'

function Logout() {
  console.log("logged out");
}

function App({ loggedIn }) {
  return (
    <>
     <Navbar />
      {loggedIn ? <Logout /> : (
        <>
          <Login />
      
          <Register />
        </>
      )}

     
      <Footer />
    </>
  );
}

App.defaultProps = {
  loggedIn: false
};

export default App;
