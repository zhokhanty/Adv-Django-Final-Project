import { Outlet } from "react-router-dom";
import Header from "../Header/Header";

export default function Layout() {
  return (
    <div className="flex min-h-screen bg-background text-foreground">
      <Header />
        <main className="p-4">
          <Outlet />
        </main>
    </div>
  );
}
