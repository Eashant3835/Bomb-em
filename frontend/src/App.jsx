import {io} from 'socket.io-client';
import { useEffect } from 'react';

const socket = io('http://localhost:8000',{
  auth: {
    player_id: 'player_1'
  }
});

function App() {
  return (
    <div>
      Hello from backend
    </div>
  )
}

export default App