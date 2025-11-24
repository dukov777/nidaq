import nidaqmx
from nidaqmx.constants import TerminalConfiguration


def main() -> None:
    with nidaqmx.Task() as write_task, nidaqmx.Task() as read_task:
        # Configure AO channel on Dev1/ao0 for outputting 0-5 V
        write_task.ao_channels.add_ao_voltage_chan("Dev1/ao0", "mychannel", 0, 5)
        # Configure AI channel on Dev1/ai0 in RSE mode for 0-5 V readings
        read_task.ai_channels.add_ai_voltage_chan(
            "Dev1/ai0",
            min_val=0,
            max_val=5,
            terminal_config=TerminalConfiguration.RSE,
        )

        write_task.start()
        read_task.start()

        try:
            while True:
                # Prompt for voltage, validate, then write to AO and read back AI
                user_input = input("Enter voltage to write (0-5 V) or Ctrl+C to exit: ").strip()
                try:
                    voltage = float(user_input)
                except ValueError:
                    print("Invalid number. Please provide a numeric voltage value.")
                    continue

                write_task.write(voltage)
                print(f"Readback: {read_task.read()}")
        except KeyboardInterrupt:
            print("\nStopping on user request (Ctrl+C).")
        finally:
            write_task.stop()
            read_task.stop()


if __name__ == "__main__":
    main()
