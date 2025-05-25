#!/usr/bin/env python3
"""
Simple test script to demonstrate calling a single ISS telemetry tool
"""

import asyncio
import json
from fastmcp import Client

async def test_environmental_data():
    """Test the ISS environmental data tool"""
    
    client = Client("iss_mcp_server.py")
    
    async with client:
        print("🌍 Testing ISS Environmental Data Tool")
        print("=" * 40)
        
        # Call the environmental data tool
        result = await client.call_tool("get_iss_environmental_data")
        
        # Extract and parse the response
        if hasattr(result, 'content') and result.content:
            content = result.content[0].text
            data = json.loads(content)
            
            print("\n📊 Current ISS Environmental Conditions:")
            print(f"🌡️  Cabin Temperature: {data['cabin_temperature']['value']}°C")
            print(f"🫁 Cabin Pressure: {data['cabin_pressure']['value']} mmHg")
            print(f"💧 Humidity: {data['humidity']['value']}%")
            print(f"🌬️  CO2 Level: {data['co2_level']['value']} ppm")
            print(f"🫁 Oxygen Level: {data['oxygen_level']['value']}%")
            
            print(f"\n⏰ Last Updated: {data['cabin_temperature']['timestamp']}")
            print(f"✅ All systems: {data['cabin_temperature']['status']}")
        
        print("\n🚀 Test completed successfully!")

if __name__ == "__main__":
    asyncio.run(test_environmental_data()) 