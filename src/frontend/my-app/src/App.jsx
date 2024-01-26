import Login from './components/Login.jsx'
import Register from './components/Register.jsx'
import Navbar from './components/Navbar.jsx';

function Logout(){
  alert("logged out")
}

function App() {
  return (
    <>
      {loggedIn ? <Logout /> : (
        <>
          <Login />
          <Register />
        </>
      )}
    <Navbar />
    <Footer />

    </>
  );
}


App.defaultProps= {
  loggedIn : false
}

export default App
