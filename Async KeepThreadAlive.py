import asyncio

async def start_task(function_name):
    await asyncio.to_thread(function_name)

# Function to keep the task alive
async def wait_for_exit():
    while True:
        user_input = await asyncio.to_thread(input, "Type 'exit' to quit: ")
        if user_input.lower() == 'exit':
            print("Exiting...")
            break

async def print_test():
    while True:
        print("test")
        await asyncio.sleep(1)

# Create and start the tasks
async def main():
    exit_task = asyncio.create_task(wait_for_exit())
    print_task = asyncio.create_task(print_test())

    # Main thread can continue to do other things if needed
    try:
        while not exit_task.done():
            # Perform other tasks here, if necessary
            await asyncio.sleep(1)
    except KeyboardInterrupt:
        print("Received CTRL+C, exiting...")
        exit_task.cancel()
        print_task.cancel()
        try:
            await exit_task
            await print_task
        except asyncio.CancelledError:
            pass

if __name__ == "__main__":
    asyncio.run(main())
