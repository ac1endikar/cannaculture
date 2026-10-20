const fs = require('fs');
const path = require('path');

const dataPath = path.join(__dirname, '..', 'js', 'data.js');
let code = fs.readFileSync(dataPath, 'utf8');

// Strip export const and convert to executable JS
code = code.replace(/export const /g, 'const ');
code += '\nconsole.log("Total strains in DB:", STRAINS_DATABASE.length);\n';
code += 'const dna = STRAINS_DATABASE.filter(s => s.bank === "DNA Genetics");\n';
code += 'console.log("DNA Genetics count:", dna.length);\n';
code += 'dna.forEach(s => {\n';
code += '  console.log(`  - [${s.species}] ${s.name} (${s.id}) -> img: ${s.image}, yield: ${s.yieldIndoor}/${s.yieldOutdoor}, THC: ${s.thc}%, dominantTerpene: ${s.dominantTerpene}`);\n';
code += '});\n';

fs.writeFileSync(path.join(__dirname, 'test_eval.js'), code, 'utf8');

try {
  require('./test_eval.js');
  console.log('\n✅ JavaScript evaluation of data.js succeeded with zero syntax errors!');
} catch (e) {
  console.error('\n❌ JavaScript evaluation error:', e);
}
