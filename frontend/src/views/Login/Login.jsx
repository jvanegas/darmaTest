import './Login.css';
import { useState } from 'react';
import Input from '../../components/Input/Input';
import Button from '../../components/Button/Button';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faUser, faLock } from '@fortawesome/free-solid-svg-icons';

function Login () {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const onClick = () => {
    alert(`Username: ${username}\nPassword: ${password}`);
  }

  return (
    <div className='loginContainer'>
      <div className='loginFormContainer'>
        <h1 className='loginHeader'>Welcome to Darma!</h1>
        <div>
          <FontAwesomeIcon icon={faUser} className='icons'/><Input placeholder="Username" type="text" onChange={e => setUsername(e.target.value)} />
        </div>
        <div>
          <FontAwesomeIcon icon={faLock} className='icons'/><Input placeholder="Password" type="password" onChange={e => setPassword(e.target.value)} />
        </div>
        <Button onClick={onClick}>Login</Button>
      </div>
    </div>
  );
}

export default Login;
