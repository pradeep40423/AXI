// src/App.tsx
import React from 'react';
import { Routes, Route, Link } from 'react-router-dom';
import Login from './pages/Login';
import Signup from './pages/Signup';
import { Container, Button } from '@mui/material';

const App: React.FC = () => {
  return (
    <Container className="text-center mt-5">
      <h1>Welcome to AXI</h1>
      <div className="mb-4">
        <Button variant="outlined" component={Link} to="/login" className="me-2">Login</Button>
        <Button variant="outlined" component={Link} to="/signup">Sign Up</Button>
      </div>

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </Container>
  );
};

export default App;
