# Changelog

All notable changes to the ISS Telemetry MCP Server will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-01-15

### Added
- Initial release of ISS Telemetry MCP Server
- Environmental data tool (`get_iss_environmental_data`)
- Orbital data tool (`get_iss_orbital_data`) 
- Solar array position tool (`get_iss_solar_array_position`)
- Waste and water management tool (`get_iss_waste_water_management`)
- Signal status tool (`get_iss_signal_status`)
- Comprehensive telemetry tool (`get_all_iss_telemetry`)
- Data persistence tool (`save_telemetry_to_file`)
- Example client implementation
- Simple test script for single tool testing
- Comprehensive documentation and README
- MIT License
- Python virtual environment support

### Technical Details
- Built with FastMCP SDK (>=2.2.10)
- Pydantic models for data validation
- Simulated ISS telemetry data with realistic values
- Async/await support throughout
- Proper error handling and logging
- Type hints and documentation strings

### Documentation
- Complete README with installation and usage instructions
- Code examples for integration
- Data structure documentation
- Contributing guidelines 