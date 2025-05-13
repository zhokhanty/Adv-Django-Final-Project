import { Link } from "react-router-dom";
import "./Home.css";

export default function Home() {
  return (
    <section className="hero">
      <h1>Добро пожаловать в Skillsphere!</h1>
      <p className="hero-subtitle">Развивайте навыки с персонализированным обучением</p>
      <div className="hero-actions">
        <Link to="/courses" className="btn btn-primary">Начать обучение</Link>
        <Link to="/challenges" className="btn btn-secondary">Принять вызов</Link>
      </div>
    </section>
  );
}