
import React from 'react';
import { Container, TextField, Button, Typography } from '@mui/material';

const Login: React.FC = () => {
  return (
    <Container maxWidth="sm" className="mt-5">
      <Typography variant="h4" gutterBottom>Login</Typography>
      <TextField fullWidth label="Email" margin="normal" />
      <TextField fullWidth label="Password" type="password" margin="normal" />
      <Button variant="contained" color="primary" className="mt-3">Login</Button>
    </Container>
  );
};

export default Login;
