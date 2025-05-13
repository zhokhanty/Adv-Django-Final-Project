import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../../pages/AuthPage/AuthContext';
import './Header.css';

export default function Header() {
  const { isAuthenticated, logout } = useAuth();

  return (
    <div className="main-container">
      <header className="main-header">
        <nav className="main-nav">
          <Link to="/" className="logo">Skillsphere</Link>
          <div className="nav-links">
            <Link to="/">Home</Link>
            <Link to="/courses">Courses</Link>
            <Link to="/challenges">Challenges</Link>
            {isAuthenticated ? (
              <button onClick={logout} className="login-btn">Logout</button>
            ) : (
              <Link to="/auth" className="login-btn">Login</Link>
            )}
          </div>
        </nav>
      </header>
    </div>
  );
}