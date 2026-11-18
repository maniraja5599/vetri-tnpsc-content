import asyncio
import websockets
import os

VIDEO_PATH = os.path.abspath('shorts/tnpsc_quiz_short_04.mp4')

async def handler(websocket):
    print("Client connected to WebSocket server")
    try:
        with open(VIDEO_PATH, 'rb') as f:
            data = f.read()
        print(f"Sending video file ({len(data)} bytes)...")
        await websocket.send(data)
        print("Video file sent successfully!")
        # Keep open until client closes
        await websocket.wait_closed()
    except Exception as e:
        print("Error sending video:", e)

async def main():
    print("Starting WebSocket server on localhost:8766...")
    async with websockets.serve(handler, "localhost", 8766):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(main())
