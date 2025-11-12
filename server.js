// server.js - Signaling Server for Web Remote Control
const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

// Serve static files from public directory
app.use(express.static('public'));

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'client.html'));
});

// Handle socket connections
io.on('connection', (socket) => {
  console.log('User connected:', socket.id);

  // Relay signaling data between peers
  socket.on('signal', (data) => {
    console.log('Signal from', socket.id, 'to', data.to);
    io.to(data.to).emit('signal', { 
      from: socket.id, 
      signal: data.signal 
    });
  });

  // Broadcast list of connected clients
  socket.on('request-peers', () => {
    const rooms = Array.from(io.sockets.sockets.keys());
    socket.emit('peer-list', rooms.filter(id => id !== socket.id));
  });

  socket.on('disconnect', () => {
    console.log('User disconnected:', socket.id);
  });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
  console.log(`Signaling server running on http://localhost:${PORT}`);
});
