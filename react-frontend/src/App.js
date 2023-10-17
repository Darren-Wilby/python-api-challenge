import React, { useState } from 'react';
import Typewriter from './components/Typewriter';
import SubmitButton from './components/Button';
import './App.css';

function App() {
  // State variables for name, command, response, and typewriter animation key
  const [name, setName] = useState('');
  const [command, setCommand] = useState('');
  const [response, setResponse] = useState('');
  const [typewriterKey, setTypewriterKey] = useState(0);

  // Function to handle form submission
  const handleSubmit = (e) => {
    e.preventDefault();
    setResponse('')
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

  // JSX structure of the component
  return (
    <div className="App">
      <div className="centered-content">
        <img className="main-image" src="/hal.png" alt="HAL-9000" />
        <br></br><br></br>
        <form onSubmit={handleSubmit}>
          <div className='output'>
            <Typewriter text={response} delay={90} key={typewriterKey} />
          </div>
          <br></br><br></br>
          <input className="custom-inputs" value={name} placeholder="Name..." onChange={(e) => setName(e.target.value)} />
          <br></br>
          <input className="custom-inputs" value={command} placeholder="Command..." onChange={(e) => setCommand(e.target.value)} />
          <br></br>
          <div className='submit-button'>
            <SubmitButton />
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;