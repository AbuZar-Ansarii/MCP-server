from fastmcp import FastMCP
import random
import json

mcp = FastMCP(name='simple calculator server')

@mcp.tool
def add_numbers(a:int, b:int)->int:
    'this tool return sum of two given numbers'
    return a + b

@mcp.tool
def generate_randon_num()->int:
    'this tool generate randon number'
    num = random.randint(1,100)
    return num

mcp.resource('info://server')
def server_info()->str:
    'get infotmation about the server'

    info = {
        'name': 'simple calculator',
        'version': '1.0.0',
        'description': 'a basic mcp server with math tool',
        'tools': ['add','random'],
        'author': 'Mohd Abuzar'
    }
    return json.dumps(info,indent=2)

if __name__ == "__main__":
    mcp.run(transport ='http', host ='0.0.0.0', port =8000)
