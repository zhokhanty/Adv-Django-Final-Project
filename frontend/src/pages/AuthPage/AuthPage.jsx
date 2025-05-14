import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './AuthPage.css';

export default function AuthPage() {
  const [isLogin, setIsLogin] = useState(true);
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password1: '',
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
  
    const endpoint = isLogin ? '/api/token/' : '/auth/registration/';
    const payload = isLogin
      ? { username: formData.username, password: formData.password1 }
      : formData;
  
    try {
      const response = await fetch(`http://127.0.0.1:8000${endpoint}`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });
  
      const data = await response.json();
      console.log(data);
  
      if (response.ok) {
        if (isLogin) {
          localStorage.setItem('access', data.access);
          localStorage.setItem('refresh', data.refresh);
        } else {
          setIsLogin(true);
        }
        navigate('/');
      } else {
        setError(data.detail || data.message || 'Ошибка авторизации');
      }
    } catch (err) {
      setError('Ошибка сети. Повторите попытку.');
    }
  };
  
  const handleLogout = () => {
    localStorage.removeItem('access');
    localStorage.removeItem('refresh');
    navigate('/auth');
  };

  return (
    <div className="auth-container">
      {localStorage.getItem('access') ? (
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
            {!isLogin && (
              <div className="form-group">
                <label>Email</label>
                <input
                  type="email"
                  name="email"
                  value={formData.email}
                  onChange={handleChange}
                />
              </div>
            )}
            <div className="form-group">
              <label>Пароль</label>
              <input
                type="password"
                name="password1"
                value={formData.password1}
                onChange={handleChange}
                required
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
