import './App.css';
import { Routes, Route } from "react-router-dom";
import Overview from './components/overview/Overview';
import SearchPage from './components/search/SearchPage';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route path="/" element={<SearchPage/>} />
        <Route path="/overview" element={<Overview/>} />
      </Routes>
    </div>
  );
}

export default App;
