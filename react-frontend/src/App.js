import React, { useState } from 'react';
import Typewriter from './components/Typewriter';
import SubmitButton from './components/Button';
import Textbox from './components/Textbox';
import './App.css';

function App() {
  const [name, setName] = useState('');
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');
  const [typewriterKey, setTypewriterKey] = useState(0);

  const handleSubmit = (e) => {
    e.preventDefault();
    setTypewriterKey(prevKey => prevKey + 1);

    fetch("/", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        name: e.target[0].value,
        command: e.target[1].value
      })
    })
      .then(response => response.json())
      .then(data => {
        console.log(data);
        setResponse(data.response);
      })
      .catch(error => console.error('Error:', error));
  }



  return (
    <div className="App">
      <div className='left'></div>
      <div className="centered-content">
        <img className="main-image" src="/hal.png" alt="HAL-9000" />
        <form onSubmit={handleSubmit}>
          <div className='output'>
            <Typewriter text={response} delay={100} key={typewriterKey} />
          </div>
          <div className="input">
            <Textbox value={name} placeholder="Name..." onChange={(e) => setName(e.target.value)} />
          </div>
          <div className="input">
            <Textbox value={command} placeholder="Command..." onChange={(e) => setCommand(e.target.value)} />
          </div>
          <div className='submit-button'>
            <SubmitButton />
          </div>
        </form>
      </div>
      <div className='right'></div>
    </div>
  );
}

export default App;