import { Route, Routes } from "react-router-dom";
import Home from "./pages/Home/Home";
import CoursesPage from "./pages/Courses";
import { AuthProvider } from "./pages/AuthPage/AuthContext";
import AuthPage from "./pages/AuthPage/AuthPage";
import Layout from "./components/Layout/Layout";
import LessonsPage from "./pages/Lesson/Lessons";
import LessonDetailPage from "./pages/Lesson/LessonDetail";
import ChallengesPage from "./pages/Challenge/ChallengesPage";
import MyChallengesPage from "./pages/Challenge/MyChallengesPage";
import QuizzesPage from "./pages/Quiz/Quizzes";


export default function App() {
  return (
    <AuthProvider>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<Home />} />
          <Route path="/courses" element={<CoursesPage />} />
          <Route path="/courses/:courseId/lessons" element={<LessonsPage />} />
          <Route path="/courses/:courseId/lesson/:lessonId" element={<LessonDetailPage />} />
        </Route>
        <Route path="/challenges" element={<ChallengesPage />} />
        <Route path="/my-challenges" element={<MyChallengesPage />} />
        <Route path="/lesson/:lessonId/quizzes" element={<QuizzesPage />} />
        <Route path="/auth" element={<AuthPage />} />
      </Routes>
    </AuthProvider>
  );
}