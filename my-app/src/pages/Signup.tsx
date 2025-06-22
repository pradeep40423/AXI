import React from 'react';
import { Container, TextField, Button, Typography } from '@mui/material';

const Signup: React.FC = () => {
  return (
    <Container maxWidth="sm" className="mt-5">
      <Typography variant="h4" gutterBottom>Sign Up</Typography>
      <TextField fullWidth label="Name" margin="normal" />
      <TextField fullWidth label="Email" margin="normal" />
      <TextField fullWidth label="Password" type="password" margin="normal" />
      <Button variant="contained" color="primary" className="mt-3">Sign Up</Button>
    </Container>
  );
};

export default Signup;
