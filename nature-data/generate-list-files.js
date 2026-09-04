const fs = require('fs');
const path = require('path');

const listsDir = path.join(__dirname, 'lists');
const dataDir = __dirname;

// Read all list definition files
const listFiles = fs.readdirSync(listsDir)
  .filter(f => f.startsWith('list-') && f.endsWith('.json') && !f.includes('-full'))
  .sort((a, b) => {
    const numA = parseInt(a.match(/list-(\d+)/)[1]);
    const numB = parseInt(b.match(/list-(\d+)/)[1]);
    return numA - numB;
  });

console.log(`Found ${listFiles.length} list definition files`);

// Load all reserve data from chunk files
let allReserves = [];
const chunkFiles = fs.readdirSync(dataDir).filter(f => f.startsWith('reserves-') && f.endsWith('.json'));

for (const chunkFile of chunkFiles) {
  const chunkPath = path.join(dataDir, chunkFile);
  const chunkData = JSON.parse(fs.readFileSync(chunkPath, 'utf8'));
  if (Array.isArray(chunkData)) {
    allReserves = allReserves.concat(chunkData);
  } else if (chunkData.reserves) {
    allReserves = allReserves.concat(chunkData.reserves);
  }
}

console.log(`Loaded ${allReserves.length} total reserves from chunks`);

// Create a map for quick lookup by name
const reserveMap = new Map();
for (const reserve of allReserves) {
  const normalizedName = (reserve.name || '').toLowerCase().trim();
  reserveMap.set(normalizedName, reserve);
}

// Process each list
for (const listFile of listFiles) {
  const listPath = path.join(listsDir, listFile);
  const listData = JSON.parse(fs.readFileSync(listPath, 'utf8'));
  
  // Handle both formats: simple array or object with reserves array
  let reserveNames = [];
  let listName = listFile.replace('.json', '');
  
  if (Array.isArray(listData)) {
    // Check if it's an array of names (strings) or full reserve objects
    if (listData.length > 0 && typeof listData[0] === 'string') {
      reserveNames = listData;
    } else if (listData.length > 0 && listData[0].name) {
      // Already full reserve data - skip regeneration
      console.log(`\n⏭️  Skipping ${listName} - already contains full reserve data`);
      continue;
    } else {
      reserveNames = listData;
    }
  } else if (listData.reserves && Array.isArray(listData.reserves)) {
    reserveNames = listData.reserves;
    listName = listData.name || listName;
  }
  
  console.log(`\nProcessing ${listName} (${reserveNames.length} reserves)`);
  
  // Find matching reserves
  const matchedReserves = [];
  const unmatchedNames = [];
  
  for (const name of reserveNames) {
    // Skip if not a string
    if (typeof name !== 'string') {
      continue;
    }
    
    const normalizedName = name.toLowerCase().trim();
    const found = reserveMap.get(normalizedName);
    
    if (found) {
      matchedReserves.push(found);
    } else {
      unmatchedNames.push(name);
      console.log(`  ⚠️  Not found: ${name}`);
    }
  }
  
  // Save the full list file
  const fullPath = path.join(listsDir, listFile.replace('.json', '-full.json'));
  fs.writeFileSync(fullPath, JSON.stringify(matchedReserves, null, 2));
  
  console.log(`  ✓ Saved ${matchedReserves.length} reserves to ${path.basename(fullPath)}`);
  if (unmatchedNames.length > 0) {
    console.log(`  ⚠️  ${unmatchedNames.length} reserves not found`);
  }
}

console.log('\n✅ All list files generated!');
