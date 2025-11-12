# 🖥️ Web Remote Control

A web-based remote control system that allows you to control a computer remotely through your browser using WebRTC and Socket.io.

## 📋 Features

- Real-time signaling server with Socket.io
- Web-based client interface
- WebRTC peer-to-peer connection support
- Mouse and keyboard event handling
- Remote screen display canvas

## 🚀 Getting Started

### Prerequisites

- Node.js (v14 or higher)
- npm or yarn

### Installation

1. Clone this repository:
```bash
git clone https://github.com/Blazeisodd/web-remote-control.git
cd web-remote-control
```

2. Install dependencies:
```bash
npm install
```

### Running the Server

Start the signaling server:
```bash
npm start
```

For development with auto-restart:
```bash
npm run dev
```

The server will start on `http://localhost:3000`

### Usage

1. Open your browser and navigate to `http://localhost:3000`
2. You'll see the remote control client interface
3. Click "Connect to Remote PC" to establish a connection
4. The remote screen will be displayed in the canvas area

## 📁 Project Structure

```
web-remote-control/
├── server.js           # Signaling server
├── public/
│   └── client.html     # Web client UI
├── package.json        # Dependencies and scripts
├── .gitignore         # Git ignore file
└── README.md          # This file
```

## 🛠️ Technologies Used

- **Node.js** - Server runtime
- **Express** - Web server framework
- **Socket.io** - Real-time bidirectional communication
- **WebRTC** - Peer-to-peer connections
- **HTML5 Canvas** - Remote screen display

## 📝 Next Steps

To complete the remote control functionality, you'll need to:

1. Implement WebRTC peer connection logic in the client
2. Create a host agent (desktop application) that:
   - Captures screen content
   - Sends screen frames to the web client
   - Receives and executes mouse/keyboard commands
3. Add authentication and security features
4. Implement audio streaming (optional)

## 🔧 Development

This is a starter template that provides the foundation for a web-based remote control system. The signaling server and web client are functional, but you'll need to add the screen capture and input control components.

## 📄 License

MIT

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.
