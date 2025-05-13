import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import CoursesPage from "./pages/Courses";
import Challenges from "./pages/Challenges";
import { AuthProvider } from "./pages/AuthPage/AuthContext";
import AuthPage from "./pages/AuthPage/AuthPage";
import Layout from "./components/Layout/Layout";
import LessonsPage from "./pages/Lessons";

export default function App() {
  return (
    <AuthProvider>
    <Routes>
      <Route element={<Layout />}>
        <Route path="/" element={<Home />} />
        <Route path="/courses" element={<CoursesPage />} />
        <Route path="/courses/:course_id/lessons" element={<LessonsPage />} />
        <Route path="/challenges" element={<Challenges />} />
      </Route>
      <Route path="/auth" element={<AuthPage />} />
    </Routes>
    </AuthProvider>
  );
}
