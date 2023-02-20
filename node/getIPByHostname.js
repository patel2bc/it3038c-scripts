if (process.argv.length <= 2) {
  console.log("USAGE: " + __filename + " hostname.com")
  process.exit(-1)
}

const hostname = process.argv[2]

console.log(`Checking IP of: ${hostname}`)