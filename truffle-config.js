contracts_directory: './contracts/',
    contracts_build_directory: './build/contracts/',
        compilers: {
    solc: {
        version: ">=0.6.0 <0.8.0",
            optimizer: {
            enabled: true,
                runs: 200
        }
    }