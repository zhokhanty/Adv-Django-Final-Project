import { useState } from 'react';
import { registerUser } from '../services/auth';

function Register() {
  const [form, setForm] = useState({ email: '', password: '', password2: '' });
  const [message, setMessage] = useState('');

  const handleSubmit = async e => {
    e.preventDefault();
    if (form.password !== form.password2) {
      setMessage('Passwords do not match');
      return;
    }
    const data = await registerUser(form);
    if (data.id || data.email) {
      setMessage('Registration successful!');
    } else {
      setMessage('Registration failed');
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Register</h2>
      <input
        type="email"
        placeholder="Email"
        value={form.email}
        onChange={e => setForm({ ...form, email: e.target.value })}
      /><br />
      <input
        type="password"
        placeholder="Password"
        value={form.password}
        onChange={e => setForm({ ...form, password: e.target.value })}
      /><br />
      <input
        type="password"
        placeholder="Confirm Password"
        value={form.password2}
        onChange={e => setForm({ ...form, password2: e.target.value })}
      /><br />
      <button type="submit">Register</button>
      <p>{message}</p>
    </form>
  );
}

export default Register;
