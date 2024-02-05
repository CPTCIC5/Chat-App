import React from 'react';
import Navbar from './components/Navbar.jsx';
import Footer from './components/Footer.jsx';
import Login from './components/login.jsx';
import Register from './components/Register.jsx';
import MessageInputPage from './components/MessageInputPage.jsx';

function Logout() {
  console.log("logged out");
  // react components must return jsx
  return <></>
}

function App({ loggedIn }) {
  return (
    <>
     <Navbar />
      {loggedIn ? 
      <>
      <Logout /> 
      <MessageInputPage />
      </> : (
        <>
          <Login />
          <Register />
        </>
      )}
      <Footer />
    </>
  );
}


//here 
App.defaultProps = {
  loggedIn: false
};

export default App;


/*
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
*/