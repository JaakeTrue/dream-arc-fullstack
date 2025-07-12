ython
import os
from pathlib import Path
from datetime import datetime

PROJECT_TEMPLATES = {
    # ========================
    # CORE STRUCTURE
    # ========================
    "README.md": """# Dream ARC - Professional Education Platform

## Features
- Student performance dashboard
- Game Changer learning modules
- AI-powered analytics

## Quick Start
```bash
cd frontend && npm install
cd ../backend && npm install
""",

text
".gitignore": """node_modules/
.env
dist/
*.log
""",

text
# ========================
# FRONTEND (Professional UI)
# ========================
"frontend/src/index.html": """<!DOCTYPE html>
<html lang="en"> <head> <meta charset="UTF-8"> <meta name="viewport" content="width=device-width, initial-scale=1.0"> <title>Dream ARC | Professional Education</title> <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap"> </head> <body> <div id="root"></div> </body> </html>""",
text
"frontend/src/main.tsx": """import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './styles/global.css';

ReactDOM.createRoot(document.getElementById('root')!).render(
<React.StrictMode>
<App />
</React.StrictMode>
);""",

text
"frontend/src/App.tsx": """import { BrowserRouter } from 'react-router-dom';
import AppRoutes from './routes';
import { ThemeProvider } from './contexts/ThemeContext';
import Layout from './components/Layout';

export default function App() {
return (
<ThemeProvider>
<BrowserRouter>
<Layout>
<AppRoutes />
</Layout>
</BrowserRouter>
</ThemeProvider>
);
}""",

text
"frontend/src/components/Layout.tsx": """import { Outlet } from 'react-router-dom';
import Navbar from './Navbar';
import Footer from './Footer';

export default function Layout() {
return (
<div className="app-container">
<Navbar />
<main className="content">
<Outlet />
</main>
<Footer />
</div>
);
}""",

text
"frontend/src/components/Navbar.tsx": """export default function Navbar() {
return (
<nav className="navbar">
<div className="logo">Dream ARC</div>
<div className="nav-links">
<a href="/dashboard">Dashboard</a>
<a href="/game-changer">Game Changer</a>
</div>
</nav>
);
}""",

text
"frontend/src/styles/global.css": """:root {
--primary: #4361ee;
--background: #f8f9fa;
--text: #212529;
}

body {
font-family: 'Inter', sans-serif;
margin: 0;
}

.navbar {
background: white;
box-shadow: 0 2px 4px rgba(0,0,0,0.1);
padding: 1rem 2rem;
}""",

text
# ========================
# STUDENT DASHBOARD (Enhanced)
# ========================
"frontend/src/pages/Dashboard.tsx": """import StudentPerformance from '../components/students/PerformanceSection';
import RecentActivity from '../components/students/ActivityFeed';

export default function Dashboard() {
return (
<div className="dashboard">
<h1>Professional Dashboard</h1>
<StudentPerformance />
<RecentActivity />
</div>
);
}""",

text
"frontend/src/components/students/ActivityFeed.tsx": """interface Activity {
id: string;
action: string;
timestamp: string;
}

export default function RecentActivity() {
const activities: Activity[] = [
{ id: '1', action: 'Completed Math Quiz', timestamp: new Date().toISOString() }
];

return (
<div className="activity-feed">
<h3>Recent Activity</h3>
{activities.map(activity => (
<div key={activity.id} className="activity-card">
<p>{activity.action}</p>
<small>{new Date(activity.timestamp).toLocaleString()}</small>
</div>
))}
</div>
);
}""",

text
# ========================
# BACKEND (Professional Setup)
# ========================
"backend/src/config/database.ts": """import mongoose from 'mongoose';
export const connectDB = async () => {
try {
await mongoose.connect(process.env.MONGO_URI!);
console.log('Database connected');
} catch (error) {
console.error('Database connection failed:', error);
process.exit(1);
}
};""",

text
"backend/src/middleware/auth.ts": """import { Request, Response, NextFunction } from 'express';
import jwt from 'jsonwebtoken';

export const authenticate = (req: Request, res: Response, next: NextFunction) => {
const token = req.header('Authorization')?.split(' ')[1];
if (!token) return res.status(401).send('Access denied');

try {
const verified = jwt.verify(token, process.env.JWT_SECRET!);
req.user = verified;
next();
} catch (err) {
res.status(400).send('Invalid token');
}
};""",

text
# ========================
# GAME CHANGER FILES
# ========================
"frontend/src/game/GameEngine.tsx": """import { useEffect, useRef } from 'react';
import Phaser from 'phaser';

export default function GameEngine() {
const gameContainer = useRef<HTMLDivElement>(null);

useEffect(() => {
const config: Phaser.Types.Core.GameConfig = {
type: Phaser.AUTO,
parent: gameContainer.current!,
width: 800,
height: 600,
physics: { default: 'arcade' }
};

text
const game = new Phaser.Game(config);
return () => game.destroy(true);
}, []);

return <div ref={gameContainer} className="game-container" />;
}""",

text
# ========================
# DOCUMENTATION
# ========================
"docs/ARCHITECTURE.md": """# System Architecture
Frontend