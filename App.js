import React from "react";
import logo from './logo.svg';
import Home from './Home';
import Main from './Main';
import Login from "./Login";
import {BrowserRouter , Routes , Route } from 'react-router-dom';
import './App.css';
function App() {
  return (
      <Routes>
              <Route path="/" element={<Login/>}/>
              <Route path="/home" element={<Home/>}/>
              <Route path="/main" element={<Main/>}/>
                </Routes>
  )
}
export default App;