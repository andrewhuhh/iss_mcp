#!/usr/bin/env python3
"""
Example client for the ISS Telemetry MCP Server

This demonstrates how to connect to and use the ISS MCP server to fetch telemetry data.
"""

import asyncio
import json
from fastmcp import Client

async def run_client_demo():
    """Main client function to demonstrate ISS MCP server usage"""
    
    # Connect to the ISS MCP server
    # In this case, we're connecting to the local server script
    client = Client("iss_mcp_server.py")
    
    async with client:
        print("🚀 Connected to ISS Telemetry MCP Server")
        print("=" * 50)
        
        # List available tools
        print("\n📋 Available Tools:")
        tools = await client.list_tools()
        for tool in tools:
            print(f"  • {tool.name}: {tool.description}")
        
        print("\n" + "=" * 50)
        
        # Get environmental data
        print("\n🌍 ISS Environmental Data:")
        env_data = await client.call_tool("get_iss_environmental_data")
        # Extract content from MCP response
        if hasattr(env_data, 'content') and env_data.content:
            content = env_data.content[0].text if hasattr(env_data.content[0], 'text') else str(env_data.content[0])
            try:
                parsed_data = json.loads(content)
                print(json.dumps(parsed_data, indent=2))
            except json.JSONDecodeError:
                print(content)
        else:
            print(json.dumps(env_data, indent=2, default=str))
        
        # Get orbital data
        print("\n🛰️  ISS Orbital Data:")
        orbital_data = await client.call_tool("get_iss_orbital_data")
        if hasattr(orbital_data, 'content') and orbital_data.content:
            content = orbital_data.content[0].text if hasattr(orbital_data.content[0], 'text') else str(orbital_data.content[0])
            try:
                parsed_data = json.loads(content)
                print(json.dumps(parsed_data, indent=2))
            except json.JSONDecodeError:
                print(content)
        else:
            print(json.dumps(orbital_data, indent=2, default=str))
        
        # Get solar array position
        print("\n☀️ Solar Array Position:")
        solar_data = await client.call_tool("get_iss_solar_array_position")
        if hasattr(solar_data, 'content') and solar_data.content:
            content = solar_data.content[0].text if hasattr(solar_data.content[0], 'text') else str(solar_data.content[0])
            try:
                parsed_data = json.loads(content)
                print(json.dumps(parsed_data, indent=2))
            except json.JSONDecodeError:
                print(content)
        else:
            print(json.dumps(solar_data, indent=2, default=str))
        
        # Get signal status
        print("\n📡 Communication Signal Status:")
        signal_data = await client.call_tool("get_iss_signal_status")
        if hasattr(signal_data, 'content') and signal_data.content:
            content = signal_data.content[0].text if hasattr(signal_data.content[0], 'text') else str(signal_data.content[0])
            try:
                parsed_data = json.loads(content)
                print(json.dumps(parsed_data, indent=2))
            except json.JSONDecodeError:
                print(content)
        else:
            print(json.dumps(signal_data, indent=2, default=str))
        
        # Save data to file
        print("\n💾 Saving telemetry data to file...")
        save_result = await client.call_tool("save_telemetry_to_file", {
            "data_type": "all",
            "filename": "iss_telemetry_complete.json"
        })
        if hasattr(save_result, 'content') and save_result.content:
            content = save_result.content[0].text if hasattr(save_result.content[0], 'text') else str(save_result.content[0])
            print(content)
        else:
            print(save_result)
        
        print("\n✅ ISS Telemetry MCP Server demonstration complete!")

def main():
    """Console script entry point for the ISS MCP client example"""
    asyncio.run(run_client_demo())

if __name__ == "__main__":
    main() 