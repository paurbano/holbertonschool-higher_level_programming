#!/usr/bin/node

if (process.argv.length === 2) {
  console.error('No argument');
  process.exit(1);
} else if (process.argv.length === 3) {
  console.error('Argument found');
} else {
  console.error('Arguments found');
}
