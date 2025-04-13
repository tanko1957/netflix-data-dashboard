const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const app = express();
const PORT = 3000;

app.use(cors());

mongoose.connect('mongodb+srv://Adam:Canada2024@cluster0.reb1ins.mongodb.net/netflixDB?retryWrites=true&w=majority&appName=Cluster0');

const statsSchema = new mongoose.Schema({}, { strict: false });
const Stats = mongoose.model('Stats', statsSchema);

app.get('/stats', async (req, res) => {
  const result = await Stats.findOne({});
  res.json(result);
});

app.listen(PORT, () => console.log(`Server running on http://localhost:${PORT}`));
