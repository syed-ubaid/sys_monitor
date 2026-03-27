# SysMonitor 🖥️

> A real-time system resource monitoring dashboard for your terminal.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

SysMonitor provides a beautiful, live overview of your system's critical metrics directly in your console. Built with `rich` and `psutil`, it tracks CPU, Memory, and Disk usage with a sleek interface.

## 🚀 Features

*   **Real-time Tracking**: Updates metrics 4 times per second.
*   **Visual Dashboard**: Clean layout with separate panels for CPU, RAM, and Disk.
*   **Disk Usage Breakdown**: Detailed per-drive space reporting (total, used, free, percentage).
*   **Cross-Platform**: Works on Windows, macOS, and Linux.

## 🛠️ Installation

### 🆕 Recent Updates
*   **v1.2**: Added `disk_usage.py` for detailed per-drive disk space reporting.
*   **v1.1**: Improved dashboard layout and color scheme.
*   **Performance**: Optimized refresh rate for lower CPU overhead.

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/sys_monitor.git
    cd sys_monitor
    ```

2.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## 📖 Usage

### Live Dashboard
Run the monitor with a single command:
```bash
python monitor.py
```

Press `Ctrl+C` to exit the dashboard safely.

### Disk Usage Report
Get a quick snapshot of disk space for a specific drive:
```bash
python disk_usage.py
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
