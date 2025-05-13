import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './AuthPage.css';

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    password2: ''
  });
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError('');

    const endpoint = isLogin ? '/auth/login/' : '/auth/registration/';
    
    try {
      const response = await fetch(`http://127.0.0.1:8000${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (response.ok) {
        login(data.key);
        navigate('/');
      } else {
        setError(data.message || 'Authentication failed');
      }
    } catch (err) {
      setError('Network error. Please try again.');
    }
  };

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/login');
  };

  return (
    <div className="auth-container">
      {localStorage.getItem('token') ? (
        <div className="logout-section">
          <h2>Вы уверены, что хотите выйти?</h2>
          <button onClick={handleLogout} className="logout-btn">
            Выйти
          </button>
        </div>
      ) : (
        <>
          <h2>{isLogin ? 'Вход' : 'Регистрация'}</h2>
          {error && <div className="error-message">{error}</div>}
          <form onSubmit={handleSubmit}>
            {!isLogin && (
              <div className="form-group">
                <label>Имя пользователя</label>
                <input
                  type="text"
                  name="username"
                  value={formData.username}
                  onChange={handleChange}
                  required
                />
              </div>
            )}
            <div className="form-group">
              <label>Email</label>
              <input
                type="email"
                name="email"
                value={formData.email}
                onChange={handleChange}
                required
              />
            </div>
            <div className="form-group">
              <label>Пароль</label>
              <input
                type="password"
                name="password"
                value={formData.password}
                onChange={handleChange}
                required
                minLength="6"
              />
            </div>
            {!isLogin && (
            <div className="form-group">
            <label>Подтвердите пароль</label>
            <input
              type="password"
              name="password2"
              value={formData.password2}
              onChange={handleChange}
              required
              minLength="6"
            />
            </div>
            )}
            <button type="submit" className="submit-btn">
              {isLogin ? 'Войти' : 'Зарегистрироваться'}
            </button>
          </form>
          <p className="toggle-auth">
            {isLogin ? 'Нет аккаунта? ' : 'Уже есть аккаунт? '}
            <span onClick={() => setIsLogin(!isLogin)}>
              {isLogin ? 'Зарегистрироваться' : 'Войти'}
            </span>
          </p>
        </>
      )}
    </div>
  );
}