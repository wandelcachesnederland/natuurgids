const fs = require('fs');
const path = require('path');

// Read all chunk files and combine into one array
const dataDir = './nature-data';
const chunkFiles = fs.readdirSync(dataDir).filter(f => f.startsWith('reserves-') && f.endsWith('.json'));
let allReserves = [];

console.log('Loading reserve data from chunks...');
chunkFiles.forEach(file => {
  const content = fs.readFileSync(path.join(dataDir, file), 'utf8');
  const reserves = JSON.parse(content);
  allReserves = allReserves.concat(reserves);
});

console.log(`Total reserves loaded: ${allReserves.length}`);

// Sort by id to ensure correct order
allReserves.sort((a, b) => a.id - b.id);

// Create maps for looking up reserves
const reserveById = new Map();
const reserveByNameNL = new Map();
const reserveByNameEN = new Map();

allReserves.forEach(reserve => {
  reserveById.set(reserve.id, reserve);
  // Use the top-level name field if nl.name doesn't exist
  const nlName = (reserve.nl?.name || reserve.name || '').toLowerCase().trim();
  const enName = (reserve.en?.name || reserve.name || '').toLowerCase().trim();
  if (nlName) {
    reserveByNameNL.set(nlName, reserve);
  }
  if (enName && enName !== nlName) {
    reserveByNameEN.set(enName, reserve);
  }
});

// Read all list files
const listsDir = './nature-data/lists';
const listFiles = fs.readdirSync(listsDir).filter(f => f.startsWith('list-') && f.endsWith('.json')).sort();

// Process each list and extract matching reserves
listFiles.forEach(file => {
  const listData = JSON.parse(fs.readFileSync(path.join(listsDir, file), 'utf8'));
  
  // Extract list number from filename
  const match = file.match(/list-(\d+)/);
  if (!match) return;
  
  const listNum = match[1];
  const matchedReserves = [];
  const notFound = [];
  
  // Check if this is the old format (array) or new format (object with reserves array)
  if (Array.isArray(listData)) {
    // Old format: array of {id, number, name}
    listData.forEach(item => {
      if (item.id) {
        const reserve = reserveById.get(item.id);
        if (reserve) {
          matchedReserves.push(reserve);
        } else {
          notFound.push(`${item.id} (${item.name})`);
        }
      }
    });
  } else if (listData.reserves && Array.isArray(listData.reserves)) {
    // New format: object with reserves array of names
    listData.reserves.forEach(name => {
      const normalizedName = name.toLowerCase().trim();
      let reserve = reserveByNameNL.get(normalizedName);
      if (!reserve) {
        reserve = reserveByNameEN.get(normalizedName);
      }
      if (reserve) {
        matchedReserves.push(reserve);
      } else {
        notFound.push(name);
      }
    });
  }
  
  console.log(`List ${listNum}: ${matchedReserves.length} reserves matched${notFound.length > 0 ? `, ${notFound.length} not found` : ''}`);
  if (notFound.length > 0 && notFound.length <= 10) {
    console.log(`  Not found: ${notFound.join(', ')}`);
  } else if (notFound.length > 10) {
    console.log(`  Not found (first 10): ${notFound.slice(0, 10).join(', ')}...`);
  }
  
  // Write the list with full reserve data
  const fileName = `list-${listNum}-full.json`;
  const filePath = path.join(listsDir, fileName);
  
  fs.writeFileSync(filePath, JSON.stringify(matchedReserves, null, 2));
  console.log(`Written: ${fileName} with ${matchedReserves.length} reserves`);
});

console.log('\nReorganization complete!');
