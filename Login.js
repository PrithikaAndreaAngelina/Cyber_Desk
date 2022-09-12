import React from 'react'
import {Link} from 'react-router-dom';
import logo from './logo.svg';
import './App.css';
function Login () {
  return (
    <div class="min-h-screen min-w-screen flex items-center justify-center bg-black">
      <div class="flex flex-col shadow-xl">
        <div class="py-6 px-14 bg-gradient-to-r from-slate-900 via-purple-900 to-slate-900 rounded-tl-2xl rounded-tr-2xl text-center space-y-8">
          <h4 class="text-white text-center font-bold text-xl">
         Cyber Desk
          </h4>
          <h2 class="text-white text-xs font-base uppercase">Enter your email address to get started</h2>
        </div>
        <div class="flex flex-col py-6 px-8 space-y-5 bg-white">
          <input type="email" placeholder="Email Address" class="px-2 py-2 border-2 rounded-md border-gray-200 focus:outline-none focus:ring-1 focus:ring-purple-700 focus:border-transparent" required />
          <Link to="/home">
          <button class="w-full py-3 bg-purple-600 text-white rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-purple-700 focus:border-transparent shadow-lg hover-bg-purple-700">Get Started</button>
       </Link>
        </div>
      </div>
    </div>
  )
}

export default Login;