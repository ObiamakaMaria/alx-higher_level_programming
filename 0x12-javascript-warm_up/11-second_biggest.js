#!/usr/bin/node

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {

  const sortedUniqueArgs = Array.from(new Set(args)).sort((a, b) => b - a);
  
  console.log(sortedUniqueArgs[1]);
}
