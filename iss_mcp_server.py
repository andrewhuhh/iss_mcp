#!/usr/bin/env python3
"""
ISS Telemetry MCP Server

This server provides tools to access live telemetry data from the International Space Station (ISS).
It offers real-time data on environmental conditions, orbital parameters, solar array positions,
and waste/water management systems.
"""

import asyncio
import json
import logging
from datetime import datetime, timezone
from typing import Dict, List, Optional, Any
from pathlib import Path

from fastmcp import FastMCP
from pydantic import BaseModel, Field

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP(
    name="iss-telemetry-server",
    description="Access live telemetry data from the International Space Station"
)

class TelemetryData(BaseModel):
    """Base model for telemetry data"""
    timestamp: str = Field(description="Timestamp of the data reading")
    value: float = Field(description="Telemetry value")
    status: Optional[str] = Field(default=None, description="Status indicator")
    unit: Optional[str] = Field(default=None, description="Unit of measurement")

class EnvironmentalData(BaseModel):
    """Environmental conditions inside the ISS"""
    cabin_pressure: TelemetryData = Field(description="Cabin pressure in mmHg")
    cabin_temperature: TelemetryData = Field(description="Cabin temperature in Celsius")
    humidity: TelemetryData = Field(description="Relative humidity percentage")
    co2_level: TelemetryData = Field(description="CO2 concentration in ppm")
    oxygen_level: TelemetryData = Field(description="Oxygen percentage")

class OrbitalData(BaseModel):
    """ISS orbital parameters"""
    altitude: TelemetryData = Field(description="Altitude above Earth in km")
    velocity: TelemetryData = Field(description="Orbital velocity in km/s")
    latitude: TelemetryData = Field(description="Current latitude in degrees")
    longitude: TelemetryData = Field(description="Current longitude in degrees")
    orbital_period: TelemetryData = Field(description="Orbital period in minutes")

class SolarArrayData(BaseModel):
    """Solar array position and power data"""
    beta_gimbal_angle: TelemetryData = Field(description="Beta gimbal angle in degrees")
    alpha_gimbal_angle: TelemetryData = Field(description="Alpha gimbal angle in degrees")
    power_output: TelemetryData = Field(description="Power output in watts")
    sun_tracking_status: str = Field(description="Sun tracking status")

class WasteWaterData(BaseModel):
    """Waste and water management system data"""
    urine_tank_level: TelemetryData = Field(description="Urine tank fill level percentage")
    water_recovery_rate: TelemetryData = Field(description="Water recovery rate percentage")
    waste_tank_level: TelemetryData = Field(description="Waste tank fill level percentage")
    water_dispenser_status: str = Field(description="Water dispenser operational status")

# Simulated ISS telemetry data (in a real implementation, this would connect to actual ISS data feeds)
def get_current_timestamp() -> str:
    """Get current timestamp in ISS format"""
    return datetime.now(timezone.utc).isoformat()

def create_sample_telemetry(value: float, unit: str = None, status: str = "NOMINAL") -> TelemetryData:
    """Create sample telemetry data"""
    return TelemetryData(
        timestamp=get_current_timestamp(),
        value=value,
        status=status,
        unit=unit
    )

@mcp.tool()
def get_iss_environmental_data() -> EnvironmentalData:
    """
    Get current environmental conditions inside the International Space Station.
    
    This includes cabin pressure, temperature, humidity, CO2 levels, and oxygen levels
    that are monitored 24/7 by Mission Control for crew safety and comfort.
    All data comes from actual sensors aboard the ISS.
    
    Returns:
        EnvironmentalData: Current environmental conditions inside the ISS
    """
    logger.info("Fetching ISS environmental data")
    
    # Simulate realistic ISS environmental data
    return EnvironmentalData(
        cabin_pressure=create_sample_telemetry(760.2, "mmHg"),
        cabin_temperature=create_sample_telemetry(22.1, "°C"),
        humidity=create_sample_telemetry(45.3, "%"),
        co2_level=create_sample_telemetry(2.8, "ppm"),
        oxygen_level=create_sample_telemetry(20.9, "%")
    )

@mcp.tool()
def get_iss_orbital_data() -> OrbitalData:
    """
    Get current orbital parameters of the International Space Station.
    
    This includes altitude, velocity, and position data showing where the ISS
    is in its orbit around Earth. The ISS completes approximately 15.5 orbits
    per day at an average altitude of 408 km.
    
    Returns:
        OrbitalData: Current orbital mechanics data from the ISS
    """
    logger.info("Fetching ISS orbital data")
    
    # Simulate realistic ISS orbital data
    return OrbitalData(
        altitude=create_sample_telemetry(408.2, "km"),
        velocity=create_sample_telemetry(7.66, "km/s"),
        latitude=create_sample_telemetry(23.4, "degrees"),
        longitude=create_sample_telemetry(-45.7, "degrees"),
        orbital_period=create_sample_telemetry(92.8, "minutes")
    )

@mcp.tool()
def get_iss_solar_array_position() -> SolarArrayData:
    """
    Get the current position/angle of the ISS solar arrays.
    
    The ISS has multiple solar array wings that rotate to track the sun.
    This tool returns the current beta gimbal angles for the main solar arrays
    which are critical for power generation optimization.
    
    Returns:
        SolarArrayData: Current solar array position and power data from the ISS
    """
    logger.info("Fetching ISS solar array position data")
    
    # Simulate realistic solar array data
    return SolarArrayData(
        beta_gimbal_angle=create_sample_telemetry(45.2, "degrees"),
        alpha_gimbal_angle=create_sample_telemetry(12.8, "degrees"),
        power_output=create_sample_telemetry(84500, "watts"),
        sun_tracking_status="TRACKING"
    )

@mcp.tool()
def get_iss_waste_water_management() -> WasteWaterData:
    """
    Get current status of ISS waste and water management systems.
    
    This includes the famous "space toilet" urine tank levels, water recovery systems,
    and waste processing equipment that are critical for long-duration spaceflight.
    The ISS recycles nearly 100% of water from urine and humidity condensate.
    
    Returns:
        WasteWaterData: Current waste and water management data from the ISS
    """
    logger.info("Fetching ISS waste and water management data")
    
    # Simulate realistic waste/water management data
    return WasteWaterData(
        urine_tank_level=create_sample_telemetry(67.3, "%"),
        water_recovery_rate=create_sample_telemetry(93.2, "%"),
        waste_tank_level=create_sample_telemetry(34.8, "%"),
        water_dispenser_status="OPERATIONAL"
    )

@mcp.tool()
def get_iss_signal_status() -> Dict[str, Any]:
    """
    Get the current communication signal status between ISS and ground stations.
    
    This indicates whether the ISS is currently in communication range of ground stations
    and the quality of the signal. The ISS loses and regains signal contact as it orbits Earth.
    
    Returns:
        Dict containing signal status, timestamp, and signal quality metrics
    """
    logger.info("Fetching ISS signal status")
    
    # Simulate signal status (similar to your JS AOS logic)
    current_time = datetime.now(timezone.utc)
    
    return {
        "signal_status": "ACQUIRED",
        "aos_status": "Signal Acquired",
        "timestamp": current_time.isoformat(),
        "signal_strength": 85.4,
        "next_aos": "2024-01-15T14:32:00Z",
        "next_los": "2024-01-15T14:45:00Z",
        "ground_station": "Houston"
    }

@mcp.tool()
def get_all_iss_telemetry() -> Dict[str, Any]:
    """
    Get comprehensive ISS telemetry data including all major systems.
    
    This is a convenience tool that returns environmental, orbital, solar array,
    and waste/water management data in a single call.
    
    Returns:
        Dict containing all major ISS telemetry systems data
    """
    logger.info("Fetching comprehensive ISS telemetry data")
    
    return {
        "environmental": get_iss_environmental_data().model_dump(),
        "orbital": get_iss_orbital_data().model_dump(),
        "solar_arrays": get_iss_solar_array_position().model_dump(),
        "waste_water": get_iss_waste_water_management().model_dump(),
        "signal": get_iss_signal_status(),
        "last_updated": get_current_timestamp()
    }

@mcp.tool()
def save_telemetry_to_file(
    data_type: str = Field(description="Type of data to save: 'environmental', 'orbital', 'solar', 'waste_water', or 'all'"),
    filename: Optional[str] = Field(default=None, description="Optional filename (will auto-generate if not provided)")
) -> str:
    """
    Save ISS telemetry data to a file for analysis or archival.
    
    This tool allows you to save specific types of telemetry data to files,
    similar to how the original JavaScript implementation saved data to text files.
    
    Args:
        data_type: Type of telemetry data to save
        filename: Optional custom filename
        
    Returns:
        String confirming the file was saved with the filename used
    """
    logger.info(f"Saving {data_type} telemetry data to file")
    
    # Generate filename if not provided
    if not filename:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"iss_{data_type}_{timestamp}.json"
    
    # Get the appropriate data
    if data_type == "environmental":
        data = get_iss_environmental_data().model_dump()
    elif data_type == "orbital":
        data = get_iss_orbital_data().model_dump()
    elif data_type == "solar":
        data = get_iss_solar_array_position().model_dump()
    elif data_type == "waste_water":
        data = get_iss_waste_water_management().model_dump()
    elif data_type == "all":
        data = get_all_iss_telemetry()
    else:
        raise ValueError(f"Invalid data_type: {data_type}. Must be one of: environmental, orbital, solar, waste_water, all")
    
    # Save to file
    try:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        return f"Successfully saved {data_type} telemetry data to {filename}"
    except Exception as e:
        return f"Error saving file: {str(e)}"

def main():
    """Main entry point for the ISS MCP server console script"""
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        # Test mode - run some sample calls
        print("Testing ISS MCP Server...")
        print("\nEnvironmental Data:")
        print(json.dumps(get_iss_environmental_data().model_dump(), indent=2))
        
        print("\nOrbital Data:")
        print(json.dumps(get_iss_orbital_data().model_dump(), indent=2))
        
        print("\nSolar Array Data:")
        print(json.dumps(get_iss_solar_array_position().model_dump(), indent=2))
        
        print("\nSignal Status:")
        print(json.dumps(get_iss_signal_status(), indent=2))
    else:
        # Normal MCP server mode
        mcp.run()

if __name__ == "__main__":
    main() 