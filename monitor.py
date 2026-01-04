import time
import psutil
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel
from rich.live import Live
from rich.table import Table
from rich.align import Align
from rich import box

console = Console()

def get_cpu_panel():
    cpu_percent = psutil.cpu_percent(interval=None)
    cpu_freq = psutil.cpu_freq()
    
    table = Table(show_header=False, expand=True, box=None)
    table.add_column("Key", style="cyan")
    table.add_column("Value", style="green")
    
    table.add_row("Usage", f"{cpu_percent}%")
    table.add_row("Frequency", f"{cpu_freq.current:.2f} Mhz")
    table.add_row("Cores", f"{psutil.cpu_count()}")
    
    return Panel(
        Align.center(table),
        title="[b]CPU Status[/b]",
        border_style="blue",
        box=box.ROUNDED
    )

def get_mem_panel():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    
    table = Table(show_header=False, expand=True, box=None)
    table.add_column("Key", style="magenta")
    table.add_column("Value", style="yellow")
    
    table.add_row("Total", f"{mem.total / (1024**3):.2f} GB")
    table.add_row("Available", f"{mem.available / (1024**3):.2f} GB")
    table.add_row("Used", f"{mem.percent}%")
    table.add_row("Swap Used", f"{swap.percent}%")
    
    return Panel(
        Align.center(table),
        title="[b]Memory Status[/b]",
        border_style="red",
        box=box.ROUNDED
    )

def get_disk_panel():
    disk = psutil.disk_usage('/')
    
    table = Table(show_header=False, expand=True, box=None)
    table.add_column("Key", style="white")
    table.add_column("Value", style="cyan")
    
    table.add_row("Total", f"{disk.total / (1024**3):.2f} GB")
    table.add_row("Used", f"{disk.used / (1024**3):.2f} GB")
    table.add_row("Free", f"{disk.free / (1024**3):.2f} GB")
    table.add_row("Percentage", f"{disk.percent}%")
    
    return Panel(
        Align.center(table),
        title="[b]Disk Status[/b]",
        border_style="green",
        box=box.ROUNDED
    )

def make_layout():
    layout = Layout()
    layout.split_column(
        Layout(name="header", size=3),
        Layout(name="body")
    )
    layout["body"].split_row(
        Layout(name="cpu"),
        Layout(name="mem"),
        Layout(name="disk")
    )
    return layout

def update_layout(layout):
    layout["header"].update(Panel(Align.center("[bold white]SysMonitor - Live System Dashboard[/]"), style="on blue"))
    layout["cpu"].update(get_cpu_panel())
    layout["mem"].update(get_mem_panel())
    layout["disk"].update(get_disk_panel())

def main():
    layout = make_layout()
    
    console.clear()
    console.print("[bold green]Starting SysMonitor... Press Ctrl+C to exit.[/]")
    time.sleep(1)
    
    try:
        with Live(layout, refresh_per_second=4, screen=True):
            while True:
                update_layout(layout)
                time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nExiting SysMonitor. Goodbye!")

if __name__ == "__main__":
    main()
