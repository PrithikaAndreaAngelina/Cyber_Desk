import React, { useState } from 'react';
import logo from './logo.svg';
import './App.css';

function Main() {
  return (
    <div class="bg-[#1C1917]">
<div class="font-sans flex h-screen w-full items-center justify-center">
  <div class="mx-auto box-border w-[600px] rounded-lg bg-white p-4">

    <div class="flex items-center justify-between">
       <span class="before:block before:absolute before:-inset-1 before:-skew-y-3 before:bg-purple-600 relative inline-block">
    <span class="relative text-gray-50 text-2xl font-medium">Intrusion Finder!</span>
  </span>
    </div>
    <form>
<div class="grid grid-cols-3 gap-4 mt-6">
        <div>
            <label for="duration" class="block mb-2 text-base text-black font-bold">Duration Time</label>
            <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5"  required/>
        </div>
        <div>
            <label for="src_bytes" class="block mb-2 text-base text-black font-bold">Src_bytes[in bytes]</label>
            <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5" placeholder="Source to destination" required/>
        </div>
        <div>
            <label for="dst_bytes" class="block mb-2 text-base text-black font-bold">Dst_bytes[in bytes]</label>
            <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5" placeholder="Destination to source"  required/>
        </div>
</div>
<div class="grid grid-cols-2 mt-6">
<label for="guest_login" class="block mb-2 text-base font-bold text-black mt-2">Is_Guest_login</label>
<select id="guest_login" class="bg-gray-50 border border-black text-gray-900 text-sm rounded-lg block w-full p-2.5" >
  <option value="zero">0</option>
  <option value="one">1</option>
</select>
<label for="host_login" class="block mb-2 text-base font-bold text-black mt-6">Is_Host_login</label>
<select id="host_login" class="bg-gray-50 border border-black text-gray-900 text-sm rounded-lg block w-full p-2.5 mt-4" >
  <option value="zero">0</option>
  <option value="one">1</option>
</select>
</div>
<div class="grid grid-cols-3 gap-4 mt-6">
<div>
           <label for="diff_srv_rate" class="block mb-2 text-base text-black font-bold">diff_srv_rate</label>
           <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5" placeholder="% connections-different services" required/>{userErr?<span></span>:""}
       </div>
         <div>
             <label for="srv_diff_host_rate" class="block mb-2 text-base text-black font-bold">srv_diff_host_rate</label>
            <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5" placeholder="% connections-different hosts" required/>{passErr?<span></span>:""}
        </div>
       <div>
           <label for="dst_host_count" class="block mb-2 text-base text-black font-bold">dst_host_count</label>
         <input type="number" class="bg-gray-50 border border-black text-black text-sm font-bold rounded-lg block w-full p-2.5" placeholder="number of connections to the same host as the current connection in the past two seconds" required/>
     </div>
</div>
<div class="flex items-center justify-center mt-4">
<button type='submit' class='break-inside bg-purple-600 rounded-xl p-4 mb-4 '>
      <div class='flex items-center space-x-4'>
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="w-6 h-6 text-white">
 <path stroke-linecap="round" stroke-linejoin="round" d="M9.813 15.904L9 18.75l-.813-2.846a4.5 4.5 0 00-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 003.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 003.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 00-3.09 3.09zM18.259 8.715L18 9.75l-.259-1.035a3.375 3.375 0 00-2.455-2.456L14.25 6l1.036-.259a3.375 3.375 0 002.455-2.456L18 2.25l.259 1.035a3.375 3.375 0 002.456 2.456L21.75 6l-1.035.259a3.375 3.375 0 00-2.456 2.456zM16.894 20.567L16.5 21.75l-.394-1.183a2.25 2.25 0 00-1.423-1.423L13.5 18.75l1.183-.394a2.25 2.25 0 001.423-1.423l.394-1.183.394 1.183a2.25 2.25 0 001.423 1.423l1.183.394-1.183.394a2.25 2.25 0 00-1.423 1.423z" />
 </svg>
        <span class='text-base font-medium text-white'>Fetch the attack</span>
      </div>
    </button>
 </div>
</form>
 </div>
 </div>
</div>
   );
 }
export default Main;